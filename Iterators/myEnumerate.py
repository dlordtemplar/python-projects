######################################
# Introduction to Python Programming #
# WS 2013/2014                       #
# Iterators                          #
######################################

'''
EXERCISES 1

Reimplement the builtin "enumerate." Each call of the "next" method should
return a pair (tuple) containing the count (starting from 0) and the value
obtained from iterating over the sequence the function is applied to. Make sure
that your also works with unordered collection types such as sets or
dictionaries. (3 Points)

Note: If you have troubles in making myEnumerate work for unordered types,
implement it for ordered types such as lists or strings. (-1 Point)
'''


class myEnumerate:
    def __init__(self, iterable):
        self.is_set = isinstance(iterable, set)
        self.is_dict = isinstance(iterable, dict)
        if self.is_set or self.is_dict:
            self.iterable = iterable.copy()
        else:
            self.iterable = iterable
        self.index = 0

    def __iter__(self):
        """
            usually returns the iterator itself
        :return:
        """
        return self

    def __next__(self):
        """
            returns the next element or raises StopIteration
        :return:
        """
        try:
            if self.is_set:
                result = (self.index, self.iterable.pop())
            elif self.is_dict:
                result = (self.index, self.iterable.popitem())
            elif self.index < len(self.iterable):
                result = (self.index, self.iterable[self.index])
            else:
                raise StopIteration
            self.index += 1

            return result
        except:
            raise StopIteration

if __name__ == '__main__':
    for (i, ch) in myEnumerate("Python"):
        print(i, ch)

    # Output:
    # 0 P
    # 1 y
    # 2 t
    # 3 h
    # 4 o
    # 5 n
    
    for (i, ch) in myEnumerate({"a", "b", "c"}):
        print(i, ch)
    
    # Output: (order might differ)
    # (0, "a")
    # (1, "b")
    # (2, "c")

    for (i, ch) in myEnumerate({"d": 12, "b": 124, "c": 351}):
        print(i, ch)

    for (i, ch) in myEnumerate((12, 124, 351)):
        print(i, ch)
