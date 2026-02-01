empty_tuple = ()
print(empty_tuple)  # ()

family_members = ('Kevin', 'Roger', 'Diana', 'Sophia', 'Isabella')
print(family_members)  # ('Kevin', 'Roger', 'Diana', 'Sophia', 'Isabella')

siblings = ('Anna', 'Tom')
print(siblings)  # ('Anna', 'Tom')

family_members += siblings
print(family_members)  # ('Kevin', 'Roger', 'Diana', 'Sophia', 'Isabella', 'Anna', 'Tom')

#5 add or modify tuple items
# Tuples are immutable, so we cannot add or modify items directly.
# However, we can convert the tuple to a list, make changes, and convert it back
family_list = list(family_members)
family_list.append('Michael')  # Adding a new family member
family_members = tuple(family_list)
print(family_members)  # ('Kevin', 'Roger', 'Diana', 'Sophia', 'Isabella', 'Anna', 'Tom', 'Michael')

family_list.remove('Tom')
family_list.remove('Anna')
family_members = tuple(family_list)
print(family_members)  # ('Kevin', 'Roger', 'Diana', 'Sophia', 'Isabella', 'Michael')

fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
vegetables = ('asparagus', 'broccoli', 'carrot', 'daikon', 'endive')
animalproducts = ('milk', 'cheese', 'yogurt', 'butter', 'cream')
food_stuff_tp = fruits + vegetables + animalproducts
print(food_stuff_tp)
# ('apple', 'banana', 'cherry', 'date', 'elderberry', 'asparagus', 'broccoli', 'carrot', 'daikon', 'endive', 'milk', 'cheese', 'yogurt', 'butter', 'cream')

food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)
# ['apple', 'banana', 'cherry', 'date', 'elderberry', 'asparagus', 'broccoli', 'carrot', 'daikon', 'endive', 'milk', 'cheese', 'yogurt', 'butter', 'cream']

middle_index = len(food_stuff_tp) // 2
print("Middle item(s):", food_stuff_tp[middle_index-1:middle_index+2])  # Middle item(s): ('broccoli', 'carrot', 'daikon')

print("First three items:", food_stuff_list[:3])  # First three items: ['apple', 'banana', 'cherry']
print("Last three items:", food_stuff_list[-3:])  # Last three items: ['butter', 'cream']

#delete the food_stuff_tp tuple completely
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)  # ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True