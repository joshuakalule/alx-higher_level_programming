#!/usr/bin/python3
import sys
sum = 0
if __name__ == "__main__":
    for n in range(1, len(sys.argv)):
        sum += int(sys.argv[n])
    print("{}".format(sum))
