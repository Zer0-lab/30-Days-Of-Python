#Lvl 1/2

#1.Check the python version
import sys
print(sys.version);

#2. Print the following statement:
print(5 + 6)   # addition(+)
print(10 - 4)   # subtraction(-)
print(8 % 3)   # modulus(%)
print(4 / 2)   # division(/)
print(3 ** 3)  # exponential(**)
print(7 // 2)  # Floor division operator(//)
print(4 - 4j)  # Complex number

#3. Write strings on the Python shell
print("Hello World!")
print("I strarted learning Python programming today.")
print("My name is Kevin.")
print("D")
print("I'm living in BE")
print("I am enjoying 30 days of python programming")

#4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Kevin"))
print(type(('Kevin', 'Python', 'BE')))


#lvl 3
#1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

print(type(20))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type("Kevin"))             # String
print(type(True))                # Boolean
print(type([1, 2, 3]))           # List
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type({9.8, 3.14, 2.7}))    # Set
print(type({'name': 'Kevin', 'age': 25}))  # Dictionary

#2. Find an Euclidean distance between (2, 3) and (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print("Euclidean distance between points", point1, "and", point2, "is:", distance)

