import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=float)
parser.add_argument("operator", type=str)
parser.add_argument("num2", type=float)


def calculate(args):
    num1 = args.num1
    num2 = args.num2
    operator = args.operator

    math_operations = {
        '+': lambda op1, op2: op1 + op2,
        '-': lambda op1, op2: op1 - op2,
        '/': lambda op1, op2: op1 / op2,
        '*': lambda op1, op2: op1 * op2
    }

    if operation := math_operations.get(operator):
        return operation(num1, num2)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
