countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.

# A map is a function that takes a function and an iterable as parameters.
# A filter is a function that takes a function and an iterable as parameters.
# A reduce is a function that takes a function and an iterable as parameters.

# The difference between map, filter, and reduce is that map returns a new iterable, filter returns a filter object, and reduce returns a single value.


# Explain the difference between higher order function, closure and decorator

# A higher-order function is a function that takes a function as an argument or returns a function as a return value.
# A closure is a function that has access to variables defined in its parent function, even after the parent function has returned.
# A decorator is a function that takes a function as an argument and returns a new function

# The difference between higher order function, closure and decorator is that a higher-order function returns a function, a closure returns a value, and a decorator returns a new function

def to_upper(text):
    return text.upper()

upper_countries = list(map(to_upper, countries))
print(upper_countries)

def has_land(country):
    return "land" in country.lower()

land_countries = list(filter(has_land, countries))
print(land_countries)

from functools import reduce

def add_numbers(acc, curr):
    return acc + curr

sum_numbers = reduce(add_numbers, numbers, 0)
print(sum_numbers)

def print_list(list):
    for item in list:
        print(item)

print_list(countries)
print_list(names)
print_list(numbers)


def concat_countries(country_list):
    return reduce(
        lambda acc, cur: f"{acc}, and {cur}" if cur == country_list[-1] else f"{acc}, {cur}",
        country_list[1:],
        country_list[0]
    )

north_europe_sentence = concat_countries(countries) + " are north European countries"
print(north_europe_sentence)


from countries_data import countries_data

def categorize_countries(countries_list, patterns=("land", "ia", "island", "stan")):
    patterns = tuple(p.lower() for p in patterns)
    return [
        country["name"]
        for country in countries_list
        if any(pat in country["name"].lower() for pat in patterns)
    ]

print(categorize_countries(countries_data),"\n")

def dictionary_countries(countries_list):
    return {
        country["name"][0]: country["name"]
        for country in countries_list
    }

print(dictionary_countries(countries_data), "\n")

def get_first_ten_countries(countries_list):
        return [country["name"] for country in countries_list][:10]

print(get_first_ten_countries(countries_data), "\n")

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries_list):
    return [country["name"] for country in countries_list][-10:]

print(get_last_ten_countries(countries_data),"\n")

    #Sort countries by name, by capital, by population
    #Sort out the ten most spoken languages by location.
    #Sort out the ten most populated countries.

def sort_countries_name_capital_population():
    return sorted(countries_data, key=lambda x: (x["name"], x["capital"], x["population"]), reverse=True)

print(sort_countries_name_capital_population(),"\n")

def sort_languages_ten():
    ten_most_spoken_languages = {}
    for country in countries_data:
        for langue in country['languages']:
            if langue in ten_most_spoken_languages:
                ten_most_spoken_languages[langue] += 1
            else:
                ten_most_spoken_languages[langue] = 1
    ten_most_spoken_languages = sorted(ten_most_spoken_languages.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)
    print(ten_most_spoken_languages[:10],"\n")

sort_languages_ten()

def sort_countries_ten():
    ten_most_populated_countries = {}
    for country in countries_data:
        if country['name'] not in ten_most_populated_countries:
            ten_most_populated_countries[country['name']] = country['population']
    ten_most_populated_countries = sorted(ten_most_populated_countries.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)
    print(ten_most_populated_countries[:10],"\n")

sort_countries_ten()



