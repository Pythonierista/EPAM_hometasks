import argparse

parser = 0
arg = 0


def check_formula(user_input):
    numbers = arg.user_input.replace('+', ' ').replace('-', ' ')
    if len(numbers.split(' ')) == len(numbers.split()) and numbers.replace(' ', '').isnumeric():
        return (True, eval(arg.user_input))
    else:
        return (False, None)


def main():
    global parser
    global arg
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input")
    arg = parser.parse_args()
    print(check_formula(arg.user_input))


if __name__ == '__main__':
    main()
