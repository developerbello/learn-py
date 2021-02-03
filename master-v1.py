# # master-v1 
# # The script includes every code that I will write while, mastering python 

# #1 ***************************************************************
# print("*"*19)
# print("*"*19)
# print("*"*19)
# print("*"*19)
# # ***************************************************************

# #2 ***************************************************************
# print("*"*19)
# print("*                 *")
# print("*                 *")
# print("*"*19)
# #****************************************************************

# #3 ***************************************************************
# print("*")
# print("**")
# print("***")
# print("*****")
# # ***************************************************************


# #4 ***************************************************************
# # Write a program that computes and prints the result of 512 − 282/47 · 48 + 5 It is roughly .1017.
# compute_1 = (512 - 282)/(47.48 + 5)
# print("compute 1, result: ", compute_1)
# # ***************************************************************

# #5 ***************************************************************
# # Ask the user to enter a number. Print out the square of the number, but use the sep optional
# # argument to print it out in a full sentence that ends in a period.

# user_1 = eval(input("Enter a number: "))
# print("Square root:",user_1**2, sep=" ", end=".\n")
# # ***************************************************************

# #6 ***************************************************************
# # Ask the user to enter a number x . Use the sep optional argument to print out x , 2x , 3x , 4x ,
# # and 5x , each separated by three dashes, like below. Enter a number: 7. 7---14---21---28---35
# user_2 = eval(input("Enter a number, x: "))
# print(user_2, (2*user_2), (3*user_2), (4*user_2), (5*user_2), sep="---")
# # ***************************************************************

# #7 ***************************************************************
# # Write a program that asks the user for a weight in kilograms and converts it to pounds. There
# # are 2.2 pounds in a kilogram.

# # COME BACK HERE
# # ***************************************************************

# #8 ***************************************************************
# # Write a program that asks the user to enter three numbers (use three separate input state-
# # ments). Create variables called total and average that hold the sum and average of the
# # three numbers and print out the values of total and average .

# user_3_1 = eval(input("Enter a number(FIRST): "))
# user_3_2 = eval(input("Enter a number(SECOND): "))
# user_3_3 = eval(input("Enter a number(THIRD): "))

# total = user_3_1 + user_3_2 + user_3_3
# average = total // 3
# print("Total:", total, "\nAverage:", average)

# #9 ***************************************************************
# # A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# # the percent tip they want to leave. Then print both the tip amount and the total bill with the
# #tip included.

# user_4 = eval(input("What amount of meal will you buy: "))
# print("Your meal and a water(@N50)")
# water = 50
# total = user_4 + water
# print("*********Meal receipt**********")
# print("Meal amount ", user_4, "\nWater*: ", water, "\nTotal Amount:", total)
# print("************PAID***************") 
# # *****************************************************************

# #10 ****************************************************************
# your_name = input("What is your name: ")
# for i in range(100):
#   print(your_name, "\n")
# print("************** GOOD CODE ***********************************")
# # *****************************************************************

# #11 ****************************************************************
# # Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
# # option end= '' into the print function to fill the screen horizontally.]

# print(your_name, end='\n')
# for name in your_name:
#   print(name)

# # *****************************************************************

# #12 ****************************************************************
# # Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it.

# for i in range(100):
#   print(i+1, your_name, end='\n')

# # *****************************************************************

# #13 ****************************************************************
# # Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89

# for i in range(8, 92, 3):
#   print(i, sep=",")

# # *****************************************************************

# #14 ****************************************************************
# # Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.

# for i in range(100, 2, -2):
#   print(i, sep=",")

# # *****************************************************************

# #15 ****************************************************************
# # Write a program that prints out a list of the integers from 1 to 20 and their squares

# for i in range(20):
#   print(i+1, (i+1)**2, sep=" --- ")

# # *****************************************************************

# #16 ****************************************************************
# # Write a program that asks the user for their name and how many times to print it. The pro-
# # gram should print out the user’s name the specified number of times

# user_5 = input("What is your name: ")
# times = eval(input("How many time should I call your name: "))

# for i in range(times):
#   print(user_5, sep="\n")

# # *****************************************************************

# #17 ****************************************************************
# # Write a program that generates and prints 50 random integers, each between 3 and 6.
# from random import randint

# number_gen_1 = randint(3, 6)
# print("Number available beween 3 and 6 = ", number_gen_1)
# # *****************************************************************

# #18 ****************************************************************
# # Write a program that generates a random number, x , between 1 and 50, a random number y
# #between 2 and 5, and computes x y

# x = randint(1,50)
# y = randint(2, 5)

# compute_2 = x * y
# print(compute_2)

# # *****************************************************************

# #19 ****************************************************************
# # Write a program that generates a random number between 1 and 10 and prints your name that many times.

# number_gen_2 = randint(1, 10)

# for i in range(number_gen_2):
#   print("=>", i + 1, your_name, sep=" ")

# # *****************************************************************

# #20 ****************************************************************
# # Write a program that asks the user to enter two numbers, x and y , and computes|x− y|x+ y .

# x_1 = eval(input("Enter a number for x: "))
# y_2 = eval(input("Enter a number for y: "))

# compute_3 = (x_1 - y_2) / x_1 + y_2
# print(compute_3)
# # *****************************************************************

# #21 ****************************************************************
# # Write a program that asks the user to enter an angle between −180 ◦ and 180 ◦ . Using an
# # expression with the modulo operator, convert the angle to its equivalent between 0 ◦ and 360 ◦

# # COME BACK HERE

# # *****************************************************************

# #22 ****************************************************************
# # Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# #length, the program should tell the user that the entry is invalid. Otherwise, the program
# #should convert the length to inches and print out the result. There are 2.54 centimeters in an inch.

# #COME BACK HERE
# # *****************************************************************

# #23 *****************************************************************

# # Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
# # ature is in. Your program should convert the temperature to the other unit. The conversions
# # are F = 95 C + 32 and C = 9 5 (F − 32) .

# # COME BACK HERE

# #25 ****************************************************************
# # Write a program that asks the user how many credits they have taken. If they have taken 23
# # or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# # they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

# user_6 = eval(input("How many credits have you taken: "))

# if user_6 >= 84:
#   print("You're a senior")
# elif user_6 >= 54 and user_6 <= 83:
#   print("You're junior")
# elif user_6 >= 24 and user_6 <= 53:
#   print("You're a sophomore")
# else:
#   if user_6 <= 23:
#     print("You're a freshman")
# *****************************************************************

#26 ****************************************************************

# *****************************************************************
# Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.

# count = 0
# for square in range(100, 0, -1):
#   count = count + 1
#   print(count, square**2, sep=' --- ')

#27 ****************************************************************
# Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 4 and how many end in a 9.

# count_4 = 0
# count_9

# for square in range(1, 100):
#   s = (square**2)
#   print(s)
   
# *****************************************************************

#28 ****************************************************************
# Write a program that asks the user to enter a value n , and then computes (1 + 12 + 13 + · · · + 1 n ) −
# ln(n) . The ln function is log in the math module.
# ******************************************************************

#15 ****************************************************************

# ******************************************************************

#15 ****************************************************************

# ******************************************************************

#15 ****************************************************************

# ******************************************************************

#15 ****************************************************************

# ******************************************************************

#15 ****************************************************************

# ******************************************************************

#14 ****************************************************************
print("****************Nice Code************************************")
print("****************Happy Coding*********************************")

# *****************************************************************