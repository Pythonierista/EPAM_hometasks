"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if isinstance(test_string, str):
        test_string = ''.join([i for i in test_string if i.isalpha()]).upper()
        return test_string == ''.join(list(reversed(test_string)))
    else:
        raise ValueError
