""" 
Implement the Euclidean algorithm for computing the greatest common divisor of
to given numbers m and n, i.e., the largest integer by which both m and n are
divisible without remainder. (2 Points)

Algorithm:

(a) Compute the remainder of m divided by n.

(b) In each step: divide divisor of previous step by remainder.

(c) If remainder is 0, the last divisor is the gcd.

Example:

       1071 // 1029 = 1,  remainder: 42
       1029 // 42   = 24, remainder: 21
         42 // 21   = 2,  remainder: 0

Note: // is integer division:

    12 // 4 = 3
    12 // 5 = 2
"""

m = int(input("First number: "))
n = int(input("Second number: "))

# YOUR CODE

if (m > n):
    greaterNum = m
    lesserNum = n
else:
    greaterNum = n
    lesserNum = m

remainder = lesserNum
result = -1
while (remainder != 0):
    result = remainder
    remainder = greaterNum % remainder

print("The result is:", result)