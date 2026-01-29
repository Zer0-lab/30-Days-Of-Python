#lvl 1
#Day 2: 30 Days of Python Programming

first_name = 'Kevin'
last_name = 'D'
full_name = first_name + ' ' + last_name
country = 'BE'
city = 'Brussels'
age = 32
year = 2026
is_married = False
is_true = True
is_light_on = True
multiple_var1, multiple_var2, multiple_var3 = 'Kevin', 'D', 32

#lvl 2

print(type(first_name))      # str
print(type(last_name))       # str
print(type(full_name))       # str
print(type(country))         # str
print(type(city))            # str
print(type(age))             # int
print(type(year))            # int
print(type(is_married))      # bool
print(type(is_true))         # bool
print(type(is_light_on))     # bool
print(type(multiple_var1))   # str
print(type(multiple_var2))   # str
print(type(multiple_var3))   # int

len(first_name)

compare_len = len(first_name) > len(last_name)
print(compare_len)

num_one, num_two = 5, 4
print("Nombre 1:", num_one, " et nombre 2:", num_two)

total = num_one + num_two
print("Total:", total)

diff = num_two - num_one
print("Diff:", diff)

product = num_two * num_one
print("Product:", product)

division = num_one / num_two
print("Division:", division)

remainder = num_two % num_one
print("Remainder:", remainder)

variable_exp = num_one ** num_two
print("Variable exp:", variable_exp)

floor_division = num_two // num_one
print("Floor division:", floor_division)

area_of_circle = 3.14 * 30**2
print("Area of circle:", area_of_circle)

circum_of_cicle = 2 * 3.14 * 30
print("Circumference of circle:", circum_of_cicle)

radius = input("Enter radius: ")
area_of_circle_input = 3.14 * float(radius)**2
print("Area of circle with radius", radius, "is:", area_of_circle_input)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print("Your name is", first_name, last_name, "and you are", age, "years old. You live in", country)

help('keywords')