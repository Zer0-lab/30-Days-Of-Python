age = 32
height = 1.75
roger = 6 * 3j
print(age)
print(height)
print(roger)

input_based = input("Enter base: ")
input_height = input("Enter height: ")
area_of_triangle = 0.5 * float(input_based) * float(input_height)
print("Area of triangle is:", area_of_triangle)

input_side_a = input("Enter side a: ")
input_side_b = input("Enter side b: ")
input_side_c = input("Enter side c: ")
perimeter_of_triangle = float(input_side_a) + float(input_side_b) + float(input_side_c)
print("Perimeter of triangle is:", perimeter_of_triangle)

input_length = input("Enter length: ")
input_width = input("Enter width: ")
area_of_rectangle = float(input_length) * float(input_width)
perimeter_of_rectangle = 2 * (float(input_length) + float(input_width))
print("Area of rectangle is:", area_of_rectangle)
print("Perimeter of rectangle is:", perimeter_of_rectangle)

input_pi = input("Enter pi value: ")
input_radius = input("Enter radius: ")
area_circle = float(input_pi) * float(input_radius)**2
circumference_circle = 2 * float(input_pi) * float(input_radius)
print("Area of circle is:", area_circle)
print("Circumference of circle is:", circumference_circle)

m = 2
b = -2

y_intercept = (0, b)
x_intercept = (1, 0)

print("Slope:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

y1 = 2
x1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("Slope is:", slope)

compare_slope = slope == m
print("Is the slope from two points equal to the given slope?", compare_slope)  # False

for x in range(-6, 1):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")

print(len("Python"))        # 6
print(len("Dragon"))        # 6
compare_strings = len("Python") != len("Dragon")
print("Are the lengths of 'Python' and 'Dragon' equal?", compare_strings)   # False

print("on" in "Python" and "on" in "Dragon")  # True

print("jargon" in "I hope this course is not full of jargon")  # True

print("on" not in "Python" and "on" not in "Dragon")  # False

lenght_str = len("Python")
float_lenght_str = float(lenght_str)
str_lenght_str = str(float_lenght_str)
print("Length of 'Python' as float string:", str_lenght_str)  # '6.0'

print(str_lenght_str % 2 == 0)  # False

div = 7 // 3
is_equal = div == int(2.7)
print("Is floor division of 7 by 3 equal to int(2.7)?", is_equal)  # True

print(type('10') == type(10))  # False

print(int('9.8') == 10)  # True

hours = int(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hour
print("Your weekly earnings are:", weekly_earnings)  # 1120

life_years = int(input("Enter number of years you have lived: "))
seconds_lived = life_years * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")  # e.g., 1000000000 seconds

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)
    


