"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(s, spl=' '):
    if isinstance(s, str) and isinstance(spl, str):
        result = []
        while s.find(spl) != -1:
            result.append(s[0:s.find(spl)])
            s = s[s.find(spl) + 1:]
        result.append(s)
        return result
    else:
        raise ValueError
