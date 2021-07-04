"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n')
args = 0


def from_roman_numerals(args):
    d = {'IV': '4 ', 'IX': '9 ', 'XL': '40 ', 'XC': '90 '}
    d2 = {'I': '1 ', 'V': '5 ', 'X': '10 ', 'L': '50 ', 'C': '100 '}
    for i in args:
        if i not in d2:
            raise ValueError
    for i in d.keys():
        if i in args:
            args = args.replace(i, d[i])
    for i in d2.keys():
        if i in args:
            args = args.replace(i, d2[i])
    result = sum(map(int, args.split()))
    return result if result <= 100 else ValueError


def main():
    global args
    args = parser.parse_args()
    print(from_roman_numerals(args.n))


if __name__ == "__main__":
    main()
