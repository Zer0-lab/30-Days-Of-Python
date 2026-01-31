concat_string = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(concat_string)  # 'Thirty Days Of Python'

concat_string_2 = 'Coding' + ' ' + 'for' + ' ' + 'all'
print(concat_string_2)  # 'Coding for all'

company = 'Coding For All'

print(company)  # 'Coding For All'

print(len(company))  # 16

print(company.upper())  # 'CODING FOR ALL'

print(company.lower())  # 'coding for all'

print (company.capitalize())  # 'Coding for all'
print(company.title())  # 'Coding For All'
print(company.swapcase())  # 'cODING fOR aLL'

print(company[0:6])  # 'Coding'

print(company.find('Coding'))  # 0
print(company.count('coding'))  # 1

print(company.replace('Coding', 'Python'))  # 'Python For All'

print('Python for Everyone'.replace('Everyone', 'All'))  # 'Python for All'

print(company.split())  # ['Coding', 'For', 'All']

print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))  # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(company[0])  # 'C'

print(company[-1])  # 'l'

print(company[10])  # ' '

acronym = company[0] + company[7] + company[11]
print(acronym)  # 'CFA'
abbreviation = ''.join([word[0] for word in company.split()])
print(abbreviation)  # 'CFA'

print(company.index('C'))  # 0

print(company.index('F'))  # 7

company2 = 'Coding For All People'
print(company2. rfind('l'))  # 18

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))  # 47

print(" ".join(word for word in sentence.split() if word == "because"))

print(sentence.find('because'))  # 31

print(company.startswith('Coding'))  # True

print(company.endswith('Coding'))  # False

print('   Coding For All      '.strip())  # 'Coding For All'

print('30DaysOfPython'.isidentifier())  # False
print('thirty_days_of_python'.isidentifier())  # True

python_libraries = ['Django', 'Flask', 'Bootle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))  # 'Django# Flask# Bootle# Pyramid# Falcon'

#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

#Name	Age	Country	City
#Asabeneh	250	Finland	Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# radius = 10
# pi = 3.14
# area = radius ** 2 * pi
radius = 10
area = int(3.14 * radius ** 2)

print(
    "radius = {}\n"
    "area = 3.14 * radius ** 2\n"
    "The area of a circle with radius {} is {} meters square."
    .format(radius, radius, area)
)

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
