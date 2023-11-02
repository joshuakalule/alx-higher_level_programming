#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
_s_ = "s" if argc != 1 else ""
_p_ = ":" if argc >= 1 else "."

if __name__ == "__main__":
    print("{} argument{}{}".format(argc, _s_, _p_))
    if argc > 0:
        for n in range(1, argc + 1, 1):
            print("{}: {}".format(n, sys.argv[n]))
