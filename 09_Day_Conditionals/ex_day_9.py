age = input("Enter your age: ")

if int(age) >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - int(age)
    print(f"You need {years_left} more years to learn to drive.")

my_age = 32
your_age = int(input("Enter your age: "))

if my_age < your_age:
    age_diff = your_age - my_age
    print(f"You are {age_diff} years older than me.")
elif my_age > your_age:
    age_diff = my_age - your_age
    print(f"I am {age_diff} years older than you.")
else:
    print("We are the same age.")

number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))

if number_one > number_two:
    print(f"{number_one} is greater than {number_two}.")
elif number_one < number_two:
    print(f"{number_one} is less than {number_two}.")
else:
    print(f"{number_one} is equal to {number_two}.")

Student_score = int(input("Enter student score (0-100): "))
if Student_score >= 90:
    grade = 'A'
elif Student_score >= 80:
    grade = 'B'
elif Student_score >= 70:
    grade = 'C'
elif Student_score >= 60:
    grade = 'D'
elif Student_score >= 0:
    grade = 'F'       

print(f"Your grade is: {grade}")

winter_months = ['December', 'January', 'February']
spring_months = ['March', 'April', 'May']
summer_months = ['June', 'July', 'August']
autumn_months = ['September', 'October', 'November']

season = input("Enter month: ")
if season in winter_months:
    print("The season is Winter.")
elif season in spring_months:
    print("The season is Spring.")
elif season in summer_months:
    print("The season is Summer.")
elif season in autumn_months:
    print("The season is Autumn.")
else:
    print("Invalid month name.")

fruit_list = ['banana', 'orange', 'mango', 'lemon']

for fruit in fruit_list:
    print(fruit)
user_fruit = input("Enter a fruit name: ")
if user_fruit in fruit_list:
    print("That fruit already exists in the list.")
else:
    fruit_list.append(user_fruit)
    print("Fruit added to the list.")
    print(fruit_list)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

#print the middle skill
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Middle skill:", person['skills'][middle_index])  # Middle skill: Node
    if 'Python' in person['skills']:
        print("You have Python skill.")
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("He is a front end developer.")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer.")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")