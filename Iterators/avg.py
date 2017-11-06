######################################
# Introduction to Python Programming #
# WS 2013/2014                       #
# Iterators                          #
######################################

'''
EXERCISE 2:

As we have seen in the lecture, len() cannot be applied to iterators, as
they return one value at a time, not knowing how many will follow. This is
actually an advantage when working with large data files, as it saves
memory (the file can be loaded in to memory just line by line, not all
at once).

However, we cannot ask Python for the length of an iterator (try out the
following counter-example using the shell):

    myIter = iter([1, 2, 3]) # creating an iterator for the sequence (list)

    len(myIter) # will give you an error

The following function computes the average of a sequence of numbers:

    def avg(sequence):
        return sum(sequence) / len(sequence)

It doesn't work for iterators.

A straightforward way to make avg work also with iterators would be:

    def avg(iterable):
        sequence = list(iterable)
        return sum(sequence) / len(sequence)

However, this implemenation would be quite inefficent if list(iterable) results
in a very long list.

Reimplement the avg function so that it can be applied to iterators, in a way
that uses iterators directly (without computing a list)

(2 points)

'''


def avg(iterable):
    sum = 0
    count = 0
    for item in iterable:
        sum += item
        count += 1
    return sum / count


if __name__ == '__main__':
    # Testing

    myIter = iter([32, 5, 2, 75])
    print(avg(myIter))
