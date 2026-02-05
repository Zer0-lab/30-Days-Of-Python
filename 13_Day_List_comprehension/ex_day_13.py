# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([num for num in numbers if num <= 0])
print(list(filter(lambda num: num <= 0, numbers)))

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
from functools import reduce
print(reduce(lambda acc, sub: acc + sub, list_of_lists, []))

print([item for list in list_of_lists for item in list])


tuples = list(map(lambda n: (n, 1, n, n**2, n**3, n**4, n**5), range(11)))
print("[{}]".format(",\n".join(map(str, tuples))))


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = list(map(lambda item: [item[0].upper(), item[0][:3].upper(), item[1].upper()],
                  [pair for sublist in countries for pair in sublist]))
print(output)

country_city = list(map(lambda item: {"country": item[0].upper(), "city": item[1].upper()},
                        [pair for sublist in countries for pair in sublist]))
print(country_city)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = list(map(lambda item: f"{item[0]} {item[1]}",
                      [pair for sublist in names for pair in sublist]))
print(full_names)

linear_function = lambda m, b: lambda x: m * x + b
print(linear_function(2, 3)(4))