'''
The Python programming language has many built-in functions, such as sorted()
or len(). Sometimes, you won't know by heart which functions are available,
what they expect as their parameter values, and what kind of values they
return. No-one expects you to know all of this by heart, being a good
programmer doesn't require to know everything about Python, but to be able to
look it up quickly.

You will usually find some good answers just using your favorite search engine.
A forum that contains good answers to most questions is

    http://stackoverflow.com

Make sure to search the forum before asking a question!

In this exercise, however, we will practice to use the official Python
documentation, which you can find at:

    http://docs.python.org/3/library/index.html

You can use the search field on the right-hand side, or navigate using the
index. Once you opened a page of the documentation, it is often useful to use
the search function of your browser (Ctrl & F) to find the paragraphs answering
your question. When looking for a method of particular data type (e.g., you
want to get some information about the append() method of lists), it is often
quicker to search for the library reference entry of the data type. There, you
will find a list of methods that the data type provides.

The task is to implement a very simple (and very inefficient) sorting algorithm:

1. start with a new empty list to store the result.

2. as long as the input list is not empty:

2a. find the smallest value in the list to be sorted

2b. remove this value from the input list and append it to the new list

3. return the new list.

Use the Python documentation to find out how to find the smallest number in a 
list and how to remove this value from the list. 

Obviously, you should not use the builtin functions sorted() or list.sort() to 
solve the task.
'''

def my_sort(l):
    '''Returns a new sorted list'''
    result = []
    # ... your code ...

    # As long as the input list is not empty
    while len(l) > 0:
        # Find the smallest value in the list to be sorted
        minValue = min(l)

        # Remove this value from the input list and append it to the new list
        l.remove(minValue)
        result.append(minValue)

    # Return the new list
    return result

if __name__ == '__main__':
    # some tests
    print('Test1', my_sort([3,1,2]) == [1,2,3])
    print('Test2', my_sort([1,2,3]) == [1,2,3])
    print('Test3', my_sort([]) == [])
