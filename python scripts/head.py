#output is frst n lines of a given file

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(type=str, nargs=1, dest='file')
parser.add_argument('-n', type=int, nargs=1, action='store', default=10)

args = parser.parse_args()

with open(args.file[0], 'r') as w:
    lst=w.readlines()
    n=args.n
    for i in range (n):
        print(lst[i])
