import ast
import json
import os
import re
from collections import Counter
from pathlib import Path


def count_number_of_lines_and_words(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return "Nombre de lignes: {}, Nombre de mots: {}".format(len(lines), len(lines[0].split()))
    
print(count_number_of_lines_and_words('./data/obama_speech.txt'))
print(count_number_of_lines_and_words('./data/michelle_obama_speech.txt'))
print(count_number_of_lines_and_words('./data/donald_speech.txt'))
print(count_number_of_lines_and_words('./data/melina_trump_speech.txt'))

def most_spoken_languages(file_name, top_n):
    with open(file_name, 'r', encoding='utf-8') as file:
        countries = json.load(file)

    language_counts = Counter()
    for country in countries:
        language_counts.update(country.get('languages', []))

    sorted_languages = sorted(
        ((count, language) for language, count in language_counts.items()),
        reverse=True
    )

    if top_n <= 0:
        return []

    return sorted_languages[:top_n]
    
print(most_spoken_languages('./data/countries_data.json', 10))


def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)

    sorted_countries = sorted(
        countries,
        key=lambda country: country.get('population', 0),
        reverse=True
    )

    if top_n <= 0:
        return "[]"

    result = [
        {'country': country['name'], 'population': country['population']}
        for country in sorted_countries[:top_n]
    ]

    lines = ["["]
    for country in result:
        lines.append(f"\t{country},")
    lines.append("]")
    return "\n".join(lines)


print(most_populated_countries(filename='./data/countries_data.json', top_n=3))


def extract_emails(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', content)
    return "\n".join(emails)

print(extract_emails('./data/email_exchanges_big.txt'))

def first_most_common_words(file_name, top_n):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    words = re.findall(r'\b\w+\b', content)
    common_words = Counter(words).most_common(top_n)
    lines = ["["]
    for word, count in common_words:
        lines.append(f"\t({count}, '{word}'),")
    lines.append("]")
    return "\n".join(lines)

print(first_most_common_words('./data/obama_speech.txt', 10))
print(first_most_common_words('./data/michelle_obama_speech.txt', 10))
print(first_most_common_words('./data/donald_speech.txt', 10))
print(first_most_common_words('./data/melina_trump_speech.txt', 10))


def load_stop_words(file_name='./data/stop_words.py'):
    path = Path(file_name)
    if not path.is_file():
        path = Path(__file__).resolve().parent.parent / 'data' / 'stop_words.py'

    content = path.read_text(encoding='utf-8')
    match = re.search(r"stop_words\s*=\s*(\[.*\])", content, re.S)
    if not match:
        return set()
    return set(ast.literal_eval(match.group(1)))


STOP_WORDS = load_stop_words()

def _read_text(source):
    if isinstance(source, (str, os.PathLike)) and os.path.isfile(source):
        with open(source, 'r', encoding='utf-8') as file:
            return file.read()
    return str(source)


def clean_text(source):
    text = _read_text(source).lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def remove_support_words(source):
    text = clean_text(source)
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word not in STOP_WORDS]
    return filtered_tokens


def check_text_similarity(source1, source2):
    words1 = set(remove_support_words(source1))
    words2 = set(remove_support_words(source2))

    union = words1 | words2
    if not union:
        return 0.0

    intersection = words1 & words2
    return round((len(intersection) / len(union)) * 100, 2)


similarity = check_text_similarity(
    './data/michelle_obama_speech.txt',
    './data/melina_trump_speech.txt'
)
print(f"Michelle vs Melina similarity: {similarity}%")


def ten_most_repeated_words(file_name):
    words = remove_support_words(file_name)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)

    lines = ["["]
    for word, count in most_common_words:
        lines.append(f"\t({count}, '{word}'),")
    lines.append("]")
    return "\n".join(lines)

print(ten_most_repeated_words('./data/romeo_and_juliet.txt'))


def count_hacker_news_mentions(file_name):
    python_pattern = re.compile(r'python', re.IGNORECASE)
    javascript_pattern = re.compile(r'javascript', re.IGNORECASE)
    java_pattern = re.compile(r'\bjava\b', re.IGNORECASE)

    python_count = 0
    javascript_count = 0
    java_not_js_count = 0

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            has_python = bool(python_pattern.search(line))
            has_javascript = bool(javascript_pattern.search(line))
            has_java = bool(java_pattern.search(line))

            if has_python:
                python_count += 1
            if has_javascript:
                javascript_count += 1
            if has_java and not has_javascript:
                java_not_js_count += 1

    return {
        'python': python_count,
        'javascript': javascript_count,
        'java_not_javascript': java_not_js_count,
    }


hacker_news_counts = count_hacker_news_mentions('./data/hacker_news.csv')
print(f"Python/Python lines: {hacker_news_counts['python']}")
print(f"JavaScript/javascript/Javascript lines: {hacker_news_counts['javascript']}")
print(f"Java and not JavaScript lines: {hacker_news_counts['java_not_javascript']}")
