'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
# Functions
def is_palindrome(s):
 if s == reversed_string:
    return True
    return False

# Variables
string = input("please enter a word ")
s = string
reversed_string = ''.join(reversed(s))
check = is_palindrome(s)

# Logic
if check:
    print("This is a PALINDROME")
else: print("This is NOT a PALINDROME")












