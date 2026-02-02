dog_dictionary = {}
print(type(dog_dictionary))  # <class 'dict'>

dog_dictionary = {'name': 'Roger', 'color': 'white', 'breed': 'husky', 'legs': 4, 'age': 5}
print(dog_dictionary)  # {'name': 'Roger', 'color': 'white', 'breed': 'husky', 'legs': 4, 'age': 5}

student_dictionary = {
    'first_name': 'Kevin',
    'last_name': 'D',
    'gender': 'Male',
    'age': 32,
    'marital_status': 'Single',
    'skills': ['Python', 'Django', 'JavaScript'],
    'country': 'BE',
    'city': 'Brussels',
    'address': 'Some Address'
}
print(student_dictionary)  # {'first_name': 'Kevin', 'last_name': 'D', 'gender': 'Male', 'age': 32, 'marital_status': 'Single', 'skills': ['Python', 'Django', 'JavaScript'], 'country': 'BE', 'city': 'Brussels', 'address': 'Some Address'}

print(len(student_dictionary))  # 9

print(student_dictionary['skills']) # ['Python', 'Django', 'JavaScript']

student_dictionary['skills'].append('React')
print(student_dictionary['skills'])  # ['Python', 'Django', 'JavaScript', 'React']

print(list(student_dictionary.keys()))
# ['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city', 'address']

print(list(student_dictionary.values()))

print((tuple(student_dictionary.items())))

student_dictionary.pop('address')
print(student_dictionary)

del dog_dictionary
