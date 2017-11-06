"""
Write a Python program that outputs all prime numbers < 100. (2 Points)

A number is called a prime number if it is greater than 1 and has exactly
two divisors, 1 and the number itself.

For instance, the first ten prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

"""
# Range from 1-100, inclusive
for x in range(1, 101):
    isPrime = True
    for y in range(2, x - 1):
        if (isPrime):
            if (x % y == 0):
                isPrime = False
    if (isPrime):
        if (x != 1):
            print(x)