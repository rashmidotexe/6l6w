#cat utility reads files in sequence and prints their contents in the same sequence.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(nargs='+', dest='files')

args = parser.parse_args() 

for s in args.files:
    with open(s, 'r') as w:
        for line in w.readlines():
            print(line, end='')
        print()
