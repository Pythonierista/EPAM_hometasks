"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(s):
    i = 0
    result = list(s)
    for a in s:
        if a == '"':
            result[i] = "'"
        elif a == "'":
            result[i] = '"'
        i += 1
    return ''.join(result)
