'''

Implement a function that computes the intersection of two lists, i.e. a
function that returns a list of elements that are members of both input-lists.
(2 Points)

>>> intersection([1, 2, 3, 4], [2, 4, 6])
[2, 4]

Hints and comments:

x = [] creates an empty list

x.append(y) adds y to list x

>>> x = []
>>> x.append(1)
>>> x
[1]
>>> x.append(2)
>>> x
[1, 2]


For the sake of the exercise, don‘t use Python’s in operator.
'''


# ... your code ...
def intersection(list1, list2):
    shared = []
    for i in list1:
        for j in list2:
            if (i == j):
                shared.append(i)
    return shared

if __name__ == '__main__':
    print('intersection')
    print('Test1', sorted(intersection([1, 2, 3], [3, 2, 1])) == [1,2,3])
    print('Test2', sorted(intersection([1, 2, 3], [2, 3])) == [2,3])
    print('Test3', sorted(intersection([1, 2, 3], [4])) == [])
    print('Test4', sorted(intersection([], [4])) == [])
