#Task 1 calculate sum

# i = 0
# sequence = ["first", "second", "third"]
# while i < 3:
# 	number = int(input(f"Enter {sequence[i]} number: "))
# 	number += number
# 	i += 1
# print("The sum is: ", number)

#Task 2 get the difference

# i = 0
# while i < 3:
# 	num1 = int(input("Enter First number: "))
# 	num2 = int(input("Enter Second number: "))

# 	abs_difference = abs(num1 - num2)

# 	if num1 > num2:
# 		double_difference = 2 * abs_difference
# 		print("The result of calucation is: ", double_difference)
# 	else:
# 		print("The result of calucation is: ", abs_difference)
# 	i += 1

#Task 3 odd or even numbers

# num = int(input("Number to check: "))
# if num % 2 == 0:
# 	print(num, "is an even number!")
# else:
# 	print(num, "is an odd number!")

#Task 4 circle area

# import math
# radius = float(input("Input the radius of the circle: "))
# area = math.pi * radius ** 2
# rounded_area = round(area, 2)
# print("The area of the circle for the ", radius, "is: ", rounded_area)

#Task 5 guess a number

# import random

# number = random.randint(1, 10)

# while True:
# 	guess = int(input("Guess a number between 1 and 10 until you get it right: "))
# 	if guess == number:
# 	    print("Well guessed!")
# 	    break
# 	elif guess < number:
# 	    print("Try highr!")
# 	else:
# 	    print("Try lower!")

#Task 6 Celsius to Fahrenheit conversion

# scale = str(input("Input F for Farenheit and C for Celcius: "))
# temp = float(input("Input temperature in whole numbers: "))

# if scale == "F":
#     converted_temp = (temp - 32) * 5/9
#     print("The temperature in Celcius is ", converted_temp)
# elif scale == "C":
#     converted_temp = (temp * 9/5) + 32
#     print("The temperature in Farenheit is ", converted_temp)
# else:
#     print("Please enter F or C")

#Task 7 pattern

# print("*\n**\n***\n****\n*****\n****\n***\n**\n*\n")

# prin = "*"
# i = 0
# while i < 9:
# 	print(prin)
# 	if i < 4:
# 		prin += "*"
# 	else:
# 		prin = prin[:-1] #this is to remove chr from a string
# 	i += 1

#Task 8 Fibonacci series

# num1 = 0
# num2 = 1

# new_num1 = 0
# new_num2 = 0

# while num1 <= 50:
# 	print(num1)
# 	print(num2)
# 	new_num1 = num1 + num2
# 	num1 = new_num1
# 	num2 = new_num1 + num2
# 	new_num2 = num2 + num1

 