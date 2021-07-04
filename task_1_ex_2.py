import operator
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operation")
parser.add_argument("num", nargs='*')
args = 0


def calculate(args):
    a = ''
    for i in args.num:
        a = a + i + ', '
    a = a[:-2]
    if args.operation in dir(math):
        return eval(f'math.{args.operation}({a})')
    elif args.operation in dir(operator):
        return eval(f'operator.{args.operation}({a})')
    else:
        raise NotImplementedError


def main():
    global args
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
