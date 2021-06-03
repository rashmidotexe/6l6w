#sorts the lines of a text file

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(type=str, nargs=1, dest='file')
parser.add_argument('-r', action='store_true')

args = parser.parse_args()

with open(args.file[0], 'r') as w:
    lst=w.readlines()
    if args.r:
        lst.sort(reverse=True)
    else:
        lst.sort()
    for l in lst:
        print(l)
