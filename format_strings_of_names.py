'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names,
which should be separated by an ampersand.
'''


def nameList(names):
    for x in names:
        print(len(names)) # length of names list
        print(x.values())  # returning objects in array
        #iterate through objects


nameList([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
