'''
Implement a function gcd(x, y) that computes the greatest common divisor 
of x and y. (1 Point)

>>> gcd(8, 12)
4

'''


# ... your code ...
def gcd(num1, num2):
    if (num1 > num2):
        greaterNum = num1
        lesserNum = num2
    else:
        greaterNum = num2
        lesserNum = num1

    remainder = lesserNum
    result = -1
    while (remainder != 0):
        result = remainder
        remainder = greaterNum % remainder
    return result

if __name__ == '__main__':
    print('gcd')
    print('Test1', gcd(8, 12) == 4)
    print('Test2', gcd(42, 56) == 14)
    print('Test3', gcd(1071, 1029) == 21)

