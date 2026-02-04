def addd_two_numbers(a, b):
    return a + b

print(addd_two_numbers(1, 2))

def area_of_circle(radius):
    return 3.14 * radius ** 2

print(area_of_circle(10))

def add_all_nums(*nums):
    total = 0
    for i, num in enumerate(nums, start=1):
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            return f"Argument {i} ('{num}') is not a valid number."
        total += num
    return total

print(add_all_nums(1, 2, 3, 4.5))
print(add_all_nums(1, "2", 3))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))

def check_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"

print(check_season("December")) # Winter
print(check_season("June")) # Summer

def calcultate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calcultate_slope(2, 2, 6, 10)) # 2

def solve_quadratic_eqn(a, b, c):
    solution_1 = (-b + ((b**2) - (4 * a * c))**0.5) / (2 * a)
    solution_2 = (-b - ((b**2) - (4 * a * c))**0.5) / (2 * a)
    return solution_1, solution_2

print(solve_quadratic_eqn(1, 2, 1)) # (-1.0, -1.0)

def print_list(list):
    for item in list:
        print(item)

print_list([1, 2, 3, 4, 5]) # 1
          # 2
          # 3
          # 4
          # 5
# using loops
def reverse_list(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]

def reverse_list(list):
    return list[::-1]

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]

def capitalize_list_items(list):
    capitalized_list = []
    for item in list:
        capitalized_list.append(item.upper())
    return capitalized_list

print(capitalize_list_items(["apple", "banana", "cherry"])) # ['APPLE', 'BANANA', 'CHERRY']

def add_item(list, item):
    list.append(item)
    return list

print(add_item([1, 2, 3], 4)) # [1, 2, 3, 4]

def remove_item(list, item):
    list.remove(item)
    return list

print(remove_item([1, 2, 3, 4], 3)) # [1, 2, 4]

def sum_of_list(list):
    total = 0
    for item in list:
        total += item
    return total

print(sum_of_list([1, 2, 3, 4, 5])) # 15

def sum_of_odds(list):
    total = 0
    for item in list:
        if item % 2 != 0:
            total += item
    return total

print(sum_of_odds([1, 2, 3, 4, 5])) # 9

def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(number + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}. The number of evens are {evens}."

print(evens_and_odds(100)) # The number of odds are 50. The number of evens are 51.

def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total

print(factorial(5)) # 120

def is_empty(list):
    if not list:
        return True
    else:
        return False

print(is_empty([])) # True
print(is_empty([1, 2, 3])) # False

def _is_number_list(values):
    if not isinstance(values, list) or len(values) == 0:
        return False
    for value in values:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return False
    return True

def calculate_mean(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    return sum(values) / len(values)

def calculate_median(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    sorted_values = sorted(values)
    mid = len(sorted_values) // 2
    if len(sorted_values) % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]

def calculate_mode(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    modes = [value for value, count in counts.items() if count == max_count]
    if len(modes) == 1:
        return {"mode": modes[0], "count": max_count}
    return {"mode": modes, "count": max_count}

def calculate_range(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    return max(values) - min(values)

def calculate_variance(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    mean_value = calculate_mean(values)
    return sum((value - mean_value) ** 2 for value in values) / len(values)

def calculate_std(values):
    if not _is_number_list(values):
        return "Please provide a non-empty list of numbers."
    return calculate_variance(values) ** 0.5

sample_data = [1, 2, 2, 3, 4, 5]
print(calculate_mean(sample_data)) # 3
print(calculate_median(sample_data)) # 3
print(calculate_mode(sample_data)) # {'mode': 2, 'count': 2}
print(calculate_range(sample_data)) # 4
print(calculate_variance(sample_data)) # 0.6666666666666666
print(calculate_std(sample_data)) # 0.816496580927726

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet() # Hello, Guest!
greet("Alice") # Hello, Alice!

def show_args(**kwargs):
    print("Received:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_args(name="Alice", age=30, city="New York") # Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny") # Received: name: Bob, pet: Fluffy, the bunny

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7)) # True
print(is_prime(10)) # False

def is_unique(values):
    return len(set(values)) == len(values)

print(is_unique([1, 2, 3, 4, 5])) # True
print(is_unique([1, 2, 3, 4, 5, 1])) # False

def is_same(list):
    return type(list[0]) == type(list[1]) == type(list[2])

print(is_same([1, 2, 3])) # True
print(is_same([1, 2, "3"])) # False

def python_valid_variable(var):
    return var.isidentifier()

print(python_valid_variable("name")) # True
print(python_valid_variable("1name")) # False

from countries_data import countries_data
def most_spoken_languages():
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
    print(ten_most_spoken_languages[:10])

def most_populated_countries():
    ten_most_populated_countries = {}
    for country in countries_data:
        if country['name'] not in ten_most_populated_countries:
            ten_most_populated_countries[country['name']] = country['population']
    ten_most_populated_countries = sorted(ten_most_populated_countries.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)
    print(ten_most_populated_countries[:10])

most_spoken_languages()
most_populated_countries()





