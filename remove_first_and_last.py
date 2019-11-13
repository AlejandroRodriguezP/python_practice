'''
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
'''


def remove_char(s):
    size = len(s)
    if size <= 2:
        print(str(size) + " " + s)
        return " "
    elif size > 2:
        f_last = s[1:-1]
        print(f_last)
        return f_last


remove_char("hail satan")

