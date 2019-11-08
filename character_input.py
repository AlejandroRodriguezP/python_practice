#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

# imports
import datetime

# variables
name = input("please enter first and last name ")
age = input("please enter your age ")
current_year = datetime.datetime.now()

#logic
hundreth_birthday = 100 - int(age)
message = f'Hi {name} you will turn 100 in {hundreth_birthday + int(current_year.year)}'
print(message)