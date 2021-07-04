import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, default=-1)
parser.add_argument('-w', nargs='*', type=int, default=[-1])
parser.add_argument('-n', type=int, default=-1)
args = 0
result = 0


def bounded_knapsack(args):
    global result
    for i in sorted(args.w, reverse=True):
        if result + i <= args.W:
            result += i


def main():
    global args
    args = parser.parse_args()
    if any(i < 0 for i in args.w) or args.n < 0 or args.W < 0 or args.n != len(args.w):
        raise ValueError
    else:
        bounded_knapsack(args)
        print(result)


if __name__ == '__main__':
    main()
