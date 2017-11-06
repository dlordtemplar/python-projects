'''
Implement a function that recognizes palindromes (2 Points).

>>> is_palindrome("level")
True
>>> is_palindrome("levels")
False

Hints:

string[i] gives you the ith character from left (starting from 0)

string[-i] gives you ith character from right (starting from 1)

# >>> s = "abcd"
# >>> s[0]
a
# >>> s[-1]
d

Integer division:

>>> 5 // 2
2

'''



# ... your code ...
def is_palindrome(str):
    for i in range(len(str) // 2):
        if (str[i] != str[-i - 1]):
            return False
    return True

if __name__ == '__main__':
    print('is_palindrome')
    print('Test1', is_palindrome("level") == True)
    print('Test1', is_palindrome("levels") == False)
    print('Test1', is_palindrome("abba") == True)
    print('Test1', is_palindrome("aba") == True)
    print('Test1', is_palindrome("abab") == False)
    print('Test1', is_palindrome("") == True)
