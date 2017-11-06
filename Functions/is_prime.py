'''
Implement a function is_prime(x) that returns True if x is prime, False 
otherwise. (1 Point)

>>> is_prime(7)
True
>>> is_prime(15)
False
'''


# ... your code ...
def is_prime(num):
    if (num == 1):
        return False
    isPrime = True
    for y in range(2, num - 1):
        if (isPrime):
            if (num % y == 0):
                isPrime = False
    return isPrime

if __name__ == '__main__':
    print('is_prime')
    print('Test1', is_prime(1) == False)
    print('Test2', is_prime(2) == True)
    print('Test3', is_prime(3) == True)
    print('Test4', is_prime(4) == False)
    print('Test5', is_prime(5) == True)
