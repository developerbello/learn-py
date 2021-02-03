# # The file Exercise-v1 include solution to all exercises from the book Python for Everybody
# # Author: Charles R. Severance
# # The exercise covers the following topics
# # - Variables, expressions, and statements
# # - Conditional execution
# # - Functions
# # - Iteration
# # - Strings
# # - Files

#-----------------------------------------------------------------------------------
# # 1. Write a program that uses input to prompt a user for their name and then welcomes them.
# user_name = input('What is your name: ')
# print("Welcome to the journey of becomming a pythonista ", user_name)
# #-----------------------------------------------------------------------------------

# #-----------------------------------------------------------------------------------
# #2. Write a program to prompt the user for hours and rate per hour to compute gross pay.
# hours = eval(input("Hours "))
# rate = eval(input("Rate "))
# pay = hours * rate

# print("Pay: ", pay)
# #-----------------------------------------------------------------------------------
# #3. Assume that we execute the following assignment statements:
# width = 17
# height = 12.0

# wtoi      = width//2
# wtod      = width/2.0
# heigh     = height/3
# compute_1 = 1 + 2 * 5
# print("WTOI=", wtoi, " - ", "WTOD=", wtod, " - ", "HEIGHT=" , heigh, " - ", "COMPUTE=", compute_1 )
# #-----------------------------------------------------------------------------------
# #4 Write a program which prompts the user for a Celsius temperature, convert the temperature to 
# # Fahrenheit, and print out the converted temperature.


# #-----------------------------------------------------------------------------------

# #5. Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# hours_2 = eval(input("Hour_2: "))
# rate_2 = eval(input("Rate_2: "))
# if hours_2 >= 40:
#   pay = hours_2 *rate_2 * (1.5)
#   print(pay)
# else:
#   pay = hours_2 * rate_2
#   print(pay)
# #-----------------------------------------------------------------------------------

#5. Rewrite your pay program using try and except so that your program handles non-numeric 
# input gracefully by printing a message and exiting the program.
# hours_3 = input("Hour_3: ")
# try:
#   hrs = eval(hours_3) 
#   if type(hrs) == int:
#     rate_3 = eval(input("Rate_3: "))
#     pay = hrs * rate_3
#     print("Pay", pay, sep=" = ")
# except:
#   print("Error, please enter numeric input")
#-----------------------------------------------------------------------------------

#6. Write a program to prompt for a score between 0.0 and1.0. If the score is out of range, print an error message. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
# user_score = float(input("Enter your score: "))
# if type(user_score) != float:
#   print("Bad score => Please enter a numeric value")
# else:
#   if user_score >= 0.9 and user_score < 1.0:
#     print("A")
#   elif user_score >= 0.8 and user_score < 0.9:
#     print("B")
#   elif user_score >= 0.7 and user_score < 0.8:
#     print("C")
#   elif user_score >= 0.6 and user_score < 0.7:
#     print("D")
#   else:
#     if user_score < 0.6:
#       print("F")
#-----------------------------------------------------------------------------------

#7. Rewrite your pay computation with time-and-a-half for over-time and create a function 
# called computepay which takes two parameters(hours and rate)
# def computepay(hours, rate):
#   hours = eval(hours)
#   if type(hours) != int:
#     return "Error, Enter a numerical value"
#   else:
#     pay = hours * rate
#     return pay
  
# hours = input("Enter Hours")
# rate = eval(input("Enter Rate"))
# result = computepay(hours, rate)
# print(result)
#-----------------------------------------------------------------------------------

#8. Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its 
# parameter and returns a grade as a string.
# def computegrade(score):

#   if type(score) != float:
#     return "Bad score => Please enter a numeric value"
#   else:
#     if score >= 0.9 and score < 1.0:
#       return "A"
#     elif score >= 0.8 and score < 0.9:
#       return "B"
#     elif score >= 0.7 and score < 0.8:
#       return "C"
#     elif score >= 0.6 and score < 0.7:
#       return "D"
#     else:
#       if score < 0.6:
#         return "F"

# user_score = float(input("Enter your score: "))
# compute_result = computegrade(user_score)
# print(compute_result)
#-----------------------------------------------------------------------------------

#3. Write a program which repeatedly reads numbers until theuser enters “done”. Once “done” is entered, 
# print out the total, count, and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error message and skip to the next number.

# count = 0 # set counter
# total = 0 # start total value

# while True: # infinite loop

#   theuser = input("Enter a number: ") # take the user inputs and store it in the memory 
#   count = count + 1 # add 1 to the counter and update it value
#   if  theuser.startswith(('1', '2' ,'3' ,'4', '5' ,'6' ,'7', '8', '9')): # check weather user input starts with values btw 1-10
#     convuser = eval(theuser) # take the value and convert it to a real number value(integer)
#     total = total + convuser # add the real number value to total value and udate the total 

#   if theuser == 'done': # check if the user input is equal to the string value 'done'
#     average = total/count # divide the total value to the count value, set it as the average
#     print('Count:', count, 'Total:', total, 'Average', average, sep=' ') # display the counter total and average
#     break # stop the loop

#-----------------------------------------------------------------------------------

#3. Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

# numbers = [] # An empty list to store the numbers

# while True: # An infinite Loop, which will continue to run until the is termined
#   num_gen = input('Enter a number> ') # generate a number
#   if num_gen.startswith(('1','2','3','4','5','6','7','8','9')): # if the generated start with digits btw 1 - 9
#     num_conv = eval(num_gen) # the number will be converted to an integer
#     numbers.append(num_conv) # the also would then be added to list 
#   if num_gen.startswith('done'): # if the generated numbers is equal-to the string 'done' the program, will be terminated...
#     break

# lowest = 0 # declare variable to store he lowest number on the list
# highest = 0 # declare variable to store he highest number on the list

# for number in numbers: # iterate through each of the number on list 
#   lowest = number 
#   if lowest >= highest:
#     highest = lowest
#   else:
#     if lowest < highest:
#       lowest = lowest
  
# print("Highest Value: ", highest)
# print("Lowest Value: ", lowest)

#-----------------------------------------------------------------------------------

#3. Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

# words = 'X-DSPAM-Confidence:0.8475' # declare a string of alpha-numeric values, and them in words
# searchword = words.find(':') # search the substring colon to get the require values
# foundword = words[searchword + 1:] # sllce the string from value after colon to end
# decnum = float(foundword) # convert the string to a floating point value.

# print(decnum)

#-----------------------------------------------------------------------------------

#3. Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

#-----------------------------------------------------------------------------------

#3. Write a program to read through a file and print the contents of the file (line by line) all in upper case.

# fname = input("Enter the file name: ")
# try:
#   ofile = open(fname)
# except:
#   print("The file name does not exit")
#   exit()

# for line in ofile:
#   toupper = line.upper()
#   print(toupper)


#-----------------------------------------------------------------------------------

#3. Write a program to prompt for a file name, and then read through the file and look for lines of the form
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”pull apart the line to 
# extract the floating-point number on the line.Count these lines and then compute the total of the 
# spam confidence values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# flname = input("Enter file name: ")
# try:
#   opfile = open(flname)
# except: 
#   print("The file does not exit")
#   exit()

# count = 0
# total = 0
# for line in opfile:
#   if line.startswith('X-DSPAM-Confidence'):
#     exline = line
#     count = count + 1
#     col = exline.find(':')
#     number = eval(exline[col + 2:])
#     total = total + number
    
# avg = total/count
# print('Counter:', count, 'Total:', total, 'Average:', avg, sep=' ')

#-----------------------------------------------------------------------------------

#3. 
# fn = input("Enter file-name: ")
# try:
#   ofl = open(fn) # open the file handle
# except:
#   print("The file does not exit")

# for line in ofl:
#   word = line.split()
#   if len(word) == 0 or line[0:5] != 'From ' : continue
#   print(word)
#-----------------------------------------------------------------------------------

#3. Write a function called chop that takes a list and modifies it, removing the first and last elements, 
# and returns None. Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

# def chop(t):
#   rfirst = t.pop(0)
#   rlast = t.pop()

#   return None

# def middle(t):
#   newt = []
#   first = t.pop(0)
#   second = t.pop()

#   newt.append(first)
#   newt.append(second)
#   return newt 

# t = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Z']
# print(chop(t))
# print(middle(t))

#-----------------------------------------------------------------------------------

#3. Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file 
# romeo.txt and read it line by line. For each line, split the line into a list 
# of words using the split function.For each word, check to see if the word is already in a list. If the word
# is not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.
# filename = open('romeo.txt')
# nlt = []
# for line in filename:
#   tline = line.split()
#   for word in tline:
#     nlt.append(word)

# arrange = sorted(nlt)
# print(arrange)


#-----------------------------------------------------------------------------------

#3. Write a program to read through the mail box data and when you find line that starts with “From”, 
# you will split the line into words using the split function. We are interested in who sent the
# message, which is the second word on the From line.
# You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:)
# lines and print out a count at the end

# useri = input("Enter file-name: ")
# try:
#   oufn = open(useri)
# except:
#   print("File does not exist.")

# count = 0
# for line in oufn:
#   if line[:5] != 'From ': continue
#   count = count + 1
#   sline = line.split()
#   second = sline[1]
#   print(second)

# print("There were %d lines in the file with From as the first word" % count)
#-----------------------------------------------------------------------------------

#3. Rewrite the program that prompts the user for a list of numbers and prints out the maximum 
# and minimum of the numbers at the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to compute the maximum and 
# minimum numbers after the loop completes.

# t = []

# while True:
#   userv = input('Enter a number: ')
#   try:
#     if userv.startswith(('1', '2' ,'3' ,'4', '5' ,'6' ,'7', '8', '9')):
#       convu = eval(userv)
#       t.append(convu)
#     if userv == 'done':
#       lowest = min(t)
#       highest = max(t)
      
#       print("Minimum value in the list is: ", lowest)
#       print("Minimum value in the list is: ", highest)
#       break
#   except:
#     print("Wront input, please a number")

#3-----------------------------------------------------------------------------------
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether
# a string is in thedictionary

# stored = dict()
# wfn = open('words.txt')

# for line in wfn:
#   removemws = line.rstrip()
#   spltline = removemws.split()

#   for word in spltline:
#     stored[word] = None

# print(stored)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
store = dict()
dictfn = open('words.txt')

# for line in dictfn:
#   rmwspace = line.strip()
#   for c in rmwspace:
#     if c not in store:
#       store[c] = 1
#     else:
#       store[c] = store[c] + 1

# print(store)

# Alternate:
# for line in dictfn:
#   for c in line:
#     store[c] = store.get(c, 0) + 1

# print(store)

#-----------------------------------------------------------------------------------
# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# wstore = dict()

# userip = input("Enter a filename: ")
# try:
#   ofn = open(userip)
# except:
#   print("File does not exit")
#   exit()

# for line in ofn:
#   rmline = line.rstrip()
#   if not line.startswith('From'): continue
  
#   sline = rmline.split()

#   if len(sline) > 2:

#     pickword = sline[2]

#     wstore[pickword] = wstore.get(pickword,0) + 1

# print(wstore)

#-----------------------------------------------------------------------------------

# Write a program to read through a mail log, build a his-togram using a dictionary to count how many 
# messages have come from each email address, and print the dictionary.


# histostore = dict()

# hfname = input("Enter a file name: ")

# try:
#   ofname = open(hfname)
# except:
#   print("File does'nt in the directory")
#   exit()

# for line in ofname:
#   rmwline = line.rstrip()

#   if rmwline[:4] == 'From': 
#     sline = rmwline.split()
#     pickword = sline[1]

#     if not pickword in histostore:
#       histostore[pickword] = 1
#     else:
#       histostore[pickword]  = histostore[pickword] + 1

# print(histostore)


#-------------------------------------------------------------------------
# Add code to the above program to figure out who has the most messages in the file. After all the data has 
# been read and the dic-tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

# bigvalue = 0
# largehisto = None
# for email in histostore:
#   emailvalue = histostore[email]
#   if emailvalue >= bigvalue:
#     bigvalue = emailvalue
#     largehisto = email


# print(largehisto, bigvalue)


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
print("---------------------Script written by Ibrahim Bello-------------------------")
#-----------------------------------------------------------------------------------