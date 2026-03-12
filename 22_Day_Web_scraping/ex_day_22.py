import json
import re
import requests
from bs4 import BeautifulSoup

URL = "http://www.bu.edu/president/boston-university-facts-stats/"


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_number_and_label(text: str):
    """
    Exemple:
    'Student Body 37,557' -> ('Student Body', '37,557')
    """
    match = re.match(r"^(.*?)([\d,+:.$]+\s*[A-Za-z]*)$", text.strip())
    if match:
        label = clean_text(match.group(1))
        value = clean_text(match.group(2))
        return label, value
    return text, None


def scrape_bu_facts():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "url": URL,
        "title": None,
        "summary": None,
        "highlights": {},
        "community": {},
        "campus": {},
        "academics": {}
    }

    # Titre principal
    h1 = soup.find("h1")
    if h1:
        data["title"] = clean_text(h1.get_text())

    # Petit résumé sous le titre
    summary_tag = soup.find("h4")
    if summary_tag:
        data["summary"] = clean_text(summary_tag.get_text())

    # Récupérer tous les titres h3/h4 et leur contenu proche
    h3_tags = soup.find_all("h3")
    h4_tags = soup.find_all("h4")

    # 1) Highlights principaux (Research Expenditures, etc.)
    # On cherche les h3 avant la section Community
    for h3 in h3_tags:
        title = clean_text(h3.get_text())

        if title in ["Research Expenditures", "Study Abroad Programs", "Sponsored Research Awards",
                     "Classrooms", "Buildings", "Laboratories", "Libraries", "Campus Area (acres)"]:
            # Chercher le prochain texte utile
            next_tag = h3.find_next_sibling()
            while next_tag and clean_text(next_tag.get_text()) == "":
                next_tag = next_tag.find_next_sibling()

            if next_tag:
                value = clean_text(next_tag.get_text())
                if title in ["Classrooms", "Buildings", "Laboratories", "Libraries", "Campus Area (acres)"]:
                    data["campus"][title] = value
                else:
                    data["highlights"][title] = value

    # 2) Sections h4 avec listes
    for h4 in h4_tags:
        section_name = clean_text(h4.get_text())

        ul = h4.find_next_sibling("ul")
        if not ul:
            continue

        items = {}
        for li in ul.find_all("li"):
            text = clean_text(li.get_text())
            label, value = extract_number_and_label(text)
            items[label] = value if value is not None else text

        if section_name == "Community":
            data["community"] = items
        elif section_name == "Academics":
            data["academics"] = items

    return data


if __name__ == "__main__":
    result = scrape_bu_facts()

    with open("bu_facts_stats.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("Fichier JSON créé : bu_facts_stats.json")
    print(json.dumps(result, indent=4, ensure_ascii=False))


    URL = "https://archive.ics.uci.edu/datasets"


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def scrape_uci_datasets():
    response = requests.get(URL, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "url": URL,
        "datasets": []
    }

    # La page expose chaque dataset avec un titre ## dans le contenu parsé
    # On récupère les liens /dataset/... qui correspondent aux fiches datasets
    dataset_links = soup.find_all("a", href=re.compile(r"^/dataset/"))

    seen = set()

    for link in dataset_links:
        name = clean_text(link.get_text())
        href = link.get("href")

        if not name or href in seen:
            continue

        seen.add(href)

        # On part du bloc parent le plus proche
        block = link.find_parent()

        # On récupère un peu de texte autour du lien
        block_text = clean_text(block.get_text(" ", strip=True)) if block else ""

        # On essaie d'extraire les infos visibles
        # Exemple attendu :
        # Iris A small classic dataset... Classification Tabular 150 Instances 4 Features
        task_match = re.search(
            r"(Classification(?:,\s*Regression)?|Regression|Clustering|Classification,\s*Clustering)",
            block_text
        )
        data_type_match = re.search(
            r"(Tabular|Multivariate(?:,\s*Sequential,\s*Time-Series)?|Sequential|Time-Series|Text|Image|Audio|Video)",
            block_text
        )
        instances_match = re.search(r"([\d.]+[KMB]?)\s+Instances", block_text)
        features_match = re.search(r"([\d.]+[KMB]?)\s+Features", block_text)

        dataset = {
            "name": name,
            "link": f"https://archive.ics.uci.edu{href}",
            "task": task_match.group(1) if task_match else None,
            "data_type": data_type_match.group(1) if data_type_match else None,
            "instances": instances_match.group(1) if instances_match else None,
            "features": features_match.group(1) if features_match else None,
            "raw_text": block_text
        }

        data["datasets"].append(dataset)

    return data


if __name__ == "__main__":
    result = scrape_uci_datasets()

    with open("uci_datasets.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("JSON file created: uci_datasets.json")
    print(f"Datasets extracted: {len(result['datasets'])}")


URL = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
OUTPUT_FILE = "us_presidents.json"


def clean_text(text: str) -> str:
    if not text:
        return ""

    # Supprime les références Wikipédia du style [1], [a], [note 2]
    text = re.sub(r"\[[^\]]*\]", "", text)

    # Remplace les espaces multiples / retours ligne
    text = re.sub(r"\s+", " ", text).strip()

    return text


def get_presidents_table(soup: BeautifulSoup):
    # Wikipédia utilise généralement "wikitable" pour ce genre de tableau
    tables = soup.find_all("table", class_="wikitable")

    for table in tables:
        headers = [clean_text(th.get_text(" ", strip=True)).lower() for th in table.find_all("th")]
        header_text = " | ".join(headers)

        # On repère la bonne table grâce à quelques colonnes caractéristiques
        if "vice president" in header_text and "party" in header_text and "term" in header_text:
            return table

    return None


def extract_cell_text(cell):
    # On récupère le texte visible en gardant un séparateur pour éviter tout coller
    text = cell.get_text(" ", strip=True)
    return clean_text(text)


def scrape_presidents():
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = get_presidents_table(soup)
    if table is None:
        raise ValueError("Impossible de trouver la table des présidents.")

    rows = table.find_all("tr")

    presidents = []
    headers = []

    for i, row in enumerate(rows):
        ths = row.find_all("th")
        tds = row.find_all("td")

        # Ligne d'en-tête
        if i == 0:
            headers = [extract_cell_text(th).lower() for th in ths]
            continue

        # On saute les lignes vides ou bizarres
        if not tds and not ths:
            continue

        cells = row.find_all(["th", "td"])

        # La vraie table contient normalement 7 colonnes utiles
        # No. | Portrait | Name | Term | Party | Election | Vice President
        if len(cells) < 7:
            continue

        row_data = [extract_cell_text(cell) for cell in cells[:7]]

        president = {
            "number": row_data[0],
            "portrait": row_data[1],   # souvent vide ou peu utile, tu peux la supprimer si tu veux
            "name": row_data[2],
            "term": row_data[3],
            "party": row_data[4],
            "election": row_data[5],
            "vice_president": row_data[6],
        }

        presidents.append(president)

    return presidents


def main():
    presidents = scrape_presidents()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(presidents, file, indent=4, ensure_ascii=False)

    print(f"{len(presidents)} presidents saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()