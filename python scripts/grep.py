#grep command is used to find the string in the file

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(type=str, nargs=1, dest='input')

parser.add_argument(type=str, nargs='*', dest='file')

args = parser.parse_args()

inp=args.input[0]

for s in args.file:
    with open(s, 'r') as w:
        for l in w.readlines():
            if inp in l:
                print(l)
    
