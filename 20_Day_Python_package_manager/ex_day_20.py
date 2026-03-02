import statistics
import re
import json
from collections import Counter, defaultdict
from pathlib import Path

import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


CATS_API = "https://api.thecatapi.com/v1/breeds"
COUNTRIES_APIS = [
    "https://restcountries.com/v3.1/all",
    "https://restcountries.com/v2/all",
    "https://restcountries.eu/rest/v2/all",
]
UCI_URL = "https://archive.ics.uci.edu/ml/datasets.php"


def fetch_json(urls, timeout=30):
    headers = {"User-Agent": "Mozilla/5.0"}
    last_error = None
    for url in urls:
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            response.raise_for_status()
            return response.json(), url
        except requests.RequestException as exc:
            last_error = exc
    raise RuntimeError(f"Impossible de lire les URLs: {urls}") from last_error


def load_local_countries():
    path = Path(__file__).resolve().parents[1] / "data" / "countries_data.json"
    if not path.is_file():
        raise RuntimeError("Fichier local countries_data.json introuvable.")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file), str(path)


def parse_range(value):
    if not value:
        return None
    numbers = [float(n) for n in re.findall(r"\d+(?:\.\d+)?", str(value))]
    if len(numbers) >= 2:
        return min(numbers[0], numbers[1]), max(numbers[0], numbers[1])
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    return None


def get_nested_value(item, key_path):
    value = item
    for key in key_path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def range_stats(items, key):
    ranges = []
    for item in items:
        parsed = parse_range(get_nested_value(item, key))
        if parsed:
            ranges.append(parsed)

    if not ranges:
        return {"min": None, "max": None, "mean": None, "median": None, "std_dev": None}

    centers = [(low + high) / 2 for low, high in ranges]
    return {
        "min": min(low for low, _ in ranges),
        "max": max(high for _, high in ranges),
        "mean": round(statistics.mean(centers), 2),
        "median": round(statistics.median(centers), 2),
        "std_dev": round(statistics.pstdev(centers), 2),
    }


def cats_country_frequency(breeds):
    countries = defaultdict(list)
    for breed in breeds:
        country = breed.get("origin") or breed.get("country_code") or "Unknown"
        breed_name = breed.get("name", "Unknown")
        countries[country].append(breed_name)

    table = []
    for country, breed_names in countries.items():
        sorted_breeds = sorted(set(breed_names))
        table.append((country, len(sorted_breeds), sorted_breeds))
    return sorted(table, key=lambda row: (-row[1], row[0]))


def country_name(country):
    name = country.get("name")
    if isinstance(name, dict):
        return name.get("common") or name.get("official") or "Unknown"
    return name or "Unknown"


def country_area(country):
    area = country.get("area")
    if isinstance(area, (int, float)):
        return float(area)
    return 0.0


def country_population(country):
    population = country.get("population")
    if isinstance(population, (int, float)):
        return float(population)
    return 0.0


def country_languages(country):
    langs = country.get("languages")

    if isinstance(langs, dict):
        return [v for v in langs.values() if isinstance(v, str)]

    if isinstance(langs, list):
        values = []
        for lang in langs:
            if isinstance(lang, str):
                values.append(lang)
            elif isinstance(lang, dict):
                name = lang.get("name") or lang.get("nativeName")
                if name:
                    values.append(name)
        return values

    return []


def ten_largest_countries(countries):
    top = sorted(countries, key=country_area, reverse=True)[:10]
    return [(country_name(c), country_area(c)) for c in top]


def ten_most_populated_countries(countries):
    top = sorted(countries, key=country_population, reverse=True)[:10]
    return [(country_name(c), country_population(c)) for c in top]


def language_stats(countries):
    lang_counter = Counter()
    for country in countries:
        lang_counter.update(set(country_languages(country)))
    return lang_counter.most_common(10), len(lang_counter)


def scrape_uci(url):
    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    html = response.text

    if BeautifulSoup is not None:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.get_text(strip=True) if soup.title else "No title"
        dataset_links = soup.select("a[href*='dataset']") or soup.select("a[href*='DataSet']")
        dataset_names = sorted(
            {
                link.get_text(" ", strip=True)
                for link in dataset_links
                if link.get_text(" ", strip=True)
            }
        )
    else:
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "No title"
        links = re.findall(
            r"<a[^>]+href=['\"][^'\"]*dataset[^'\"]*['\"][^>]*>(.*?)</a>",
            html,
            flags=re.IGNORECASE | re.DOTALL,
        )
        dataset_names = sorted(
            {
                re.sub(r"<[^>]+>", "", link).strip()
                for link in links
                if re.sub(r"<[^>]+>", "", link).strip()
            }
        )

    return {
        "title": title,
        "dataset_link_count": len(dataset_names),
        "sample_datasets": dataset_names[:15],
    }


def print_section(title):
    print(f"\n{'=' * 20} {title} {'=' * 20}")


def main():
    print_section("CATS API")
    try:
        cats, cats_url = fetch_json([CATS_API])
        print(f"Source: {cats_url}")

        weight_stats = range_stats(cats, "weight.metric")
        lifespan_stats = range_stats(cats, "life_span")

        print("Weight (metric):", weight_stats)
        print("Lifespan (years):", lifespan_stats)

        print("\nFrequency table: country -> breeds")
        for country, count, breeds in cats_country_frequency(cats):
            print(f"{country}: {count} breeds")
            print(", ".join(breeds))
    except Exception as exc:
        print(f"Erreur Cats API: {exc}")

    print_section("COUNTRIES API")
    try:
        countries, countries_url = fetch_json(COUNTRIES_APIS)
    except RuntimeError:
        countries, countries_url = load_local_countries()

    print(f"Source: {countries_url}")
    has_area = any(country_area(country) > 0 for country in countries)
    if has_area:
        print("\n10 largest countries (by area):")
        for name, area in ten_largest_countries(countries):
            print(f"{name}: {area}")
    else:
        print("\nArea indisponible. 10 largest countries (fallback by population):")
        for name, population in ten_most_populated_countries(countries):
            print(f"{name}: {population}")

    most_spoken, total_languages = language_stats(countries)
    print("\n10 most spoken languages:")
    for language, frequency in most_spoken:
        print(f"{language}: {frequency} countries")

    print(f"\nTotal number of languages: {total_languages}")

    print_section("UCI DATASETS")
    try:
        uci_data = scrape_uci(UCI_URL)
        print(f"Title: {uci_data['title']}")
        print(f"Detected dataset links: {uci_data['dataset_link_count']}")
        print("Sample datasets:")
        for name in uci_data["sample_datasets"]:
            print(f"- {name}")
    except Exception as exc:
        print(f"Erreur UCI: {exc}")


if __name__ == "__main__":
    main()
