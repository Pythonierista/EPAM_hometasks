"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string


def chars_in_all(*s):
    if all(isinstance(x, str) for x in s):
        r = set(s[0])
        for i in s[1:]:
            r &= set(i)
        return r
    raise TypeError


def chars_in_one(*s):
    if all(isinstance(x, str) for x in s):
        r = set(s[0])
        for i in s[1:]:
            r |= set(i)
        return r
    raise TypeError


def chars_in_two(*s):
    if all(isinstance(x, str) for x in s):
        if len(s) > 1:
            result = set()
            index = 1
            while index < len(s):
                for i in s[index:]:
                    r = set(s[index - 1])
                    r &= set(i)
                    result |= r
                index += 1
            return result
        raise ValueError
    raise TypeError


def not_used_chars(*s):
    if all(isinstance(x, str) for x in s):
        result = set(string.ascii_lowercase)
        for i in s:
            result -= set(i)
        return result
    raise TypeError
