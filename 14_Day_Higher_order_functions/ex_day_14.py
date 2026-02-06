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
