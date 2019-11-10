'''
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:
find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
'''
def find_needle(haystack):
 if isinstance(haystack, list):
    needle = haystack.index("needle")
    print("found the needle at position " + str(needle))
 else:
    print("This is not a list, please enter a list")


find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])