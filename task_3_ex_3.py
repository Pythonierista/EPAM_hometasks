import argparse
import os
import fnmatch
import stat

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('-p')
args = 0


def finder(path, pattern):
    return [path + "/" + file for file in os.listdir(path) if fnmatch.fnmatch(file, pattern)]


def display_results(file_path):
    for file in file_path:
        print(file, stat.filemode(os.stat(file).st_mode))
    print('Found {count1} file(s).'.format(count1=len(file_path)))


def main():
    global args
    args = parser.parse_args()
    display_results(finder(args.path, args.p))


if __name__ == '__main__':
    main()
