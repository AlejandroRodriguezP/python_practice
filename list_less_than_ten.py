# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 10, 22]
# and write a program that prints out all the elements of the list that are less than 5.

# Variables
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 10, 22]
new_list = []
user_input = int(input('please enter any number '))

# Logic (with extra credit)
for x in list:
    if(x <= user_input):
        new_list.append(x)
        print(new_list)





# Extras:
# Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.