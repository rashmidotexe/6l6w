#checks the existence of a directory of the given name at the given location

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument(type=str, nargs=1, dest='location')
parser.add_argument('--name', type=str)

args = parser.parse_args()

i=0
for name in os.listdir(args.location[0]):
        if name==args.name:
            print("found")
            i+=1
            break
if i==0:
    print("doesn't exist")

