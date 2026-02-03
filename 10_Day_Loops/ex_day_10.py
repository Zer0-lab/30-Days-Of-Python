for i in range(11):
    print("For loop:", i)

while_loop_counter = 0
while while_loop_counter < 11:
    print("While loop:", while_loop_counter)
    while_loop_counter += 1

while_str = "#"
while len(while_str) <= 7:
    print(while_str)
    while_str += "#"

for i in range(8):
    print("# " * 7)

for i in range(1, 11):
    print(f"{i} x {i} = {i * i}")

list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in list:
    print(language)

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i) 

sum_total = 0
for i in range(101):
    if i % 2 != 0:
        sum_total += i
print("Sum of all numbers from 0 to 100 odd numbers is:", sum_total) # 2500

from countries import countries
for country in countries:
    if 'lands' in country:
        print(country)

print(len(countries)) # 195

# import the countries_data.py file. et calculer le nombre de langues au total sans doublon

from countries_data import countries_data

langues = []
for country in countries_data:
    for langue in country['languages']:
        if langue not in langues:
            langues.append(langue)
print(langues)
print(len(langues))

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

ten_most_populated_countries = {}
for country in countries_data:
    if country['name'] not in ten_most_populated_countries:
        ten_most_populated_countries[country['name']] = country['population']
ten_most_populated_countries = sorted(ten_most_populated_countries.items(), 
                                   key=lambda x: x[1], 
                                   reverse=True)
print(ten_most_populated_countries[:10])