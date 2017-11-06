"""
Introduction to Python Programming
COLLECTIONS

Exercise 1: Lists (4 points)

a) Write a function countElements(myList) that takes a list
   as its parameter and that counts for each element of the
   list how often it occurs in the list. The return value of
   the function is supposed to be a dictionary whose keys are
   the elements of the list and whose values are integers
   indicating how often each element occurs in the list. 
"""


def countElements(myList):
    """
    Remove the 'pass' statement (which stands for 'do nothing')
    and write your own code.

    Example code:
    >>> countElements([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
    {1: 2, 2: 3, 3: 4, 4: 1}
    """
    mode = {}
    for item in myList:
        if item in mode:
            mode[item] += 1
        else:
            mode[item] = 1
    return mode

"""
b) Implement the above function such that it returns a list of tuples
   (key, value). The returned list of tuples is supposed to be sorted
   by the second element of the tuples (= by how often the values
   occur in the dictionary, with the element that occurs most often
   first).
   
   You can use the builtin functions sorted() or list.sort() to sort
   a list of tuples. Note, however, that these function sort by the first
   element of a tuple by default.
"""


def countElements2(myList):
    """
    Remove the 'pass' statement and write your own code.

    >>> countElements2([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
    [(3, 4), (2, 3), (1, 2), (4, 1)]
    """
    mode = {}
    for item in myList:
        if item in mode:
            mode[item] += 1
        else:
            mode[item] = 1
    tuples = mode.items()
    return sorted(tuples, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    # This executes the functions
    # Comment out one of the functions when testing!
    countElements([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
    countElements2([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])

