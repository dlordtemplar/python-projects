
'''
Implement an iterative version (using a loop instead of recursion) of fib 
and compare runtimes. (2 Points).

Note that in each step of the computation, you need only the values of 
the last two fibonacci numbers in the sequence to compute the next value.
'''

def fib(n):
    '''Returns the nth Fibonacci number'''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# The iterative version is significantly faster than the recursive version.
def fibit(n):
    total = 0
    previous = 0
    previous2 = 0
    for i in range(n):
        previous2 = previous
        previous = total

        if i == 0:
            total = 1
        else:
            total = previous + previous2
    return total

if __name__ == '__main__':
    for i in range(33):
        print(i, fib(i))
    for i in range(33):
        print(i, fibit(i))

