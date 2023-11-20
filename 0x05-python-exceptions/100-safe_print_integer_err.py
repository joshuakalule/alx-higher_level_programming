#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    out = False
    try:
        print("{:d}".format(value))
        out = True
    except Exception as e:
        error_msg = "Exception: {}\n".format(e)
        sys.stderr.write(error_msg)
    finally:
        return out
