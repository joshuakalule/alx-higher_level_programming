#!/usr/bin/python3
"""
14. Log parsing
Reads stdin line by line and computes metrics;
    Prints the file total size
    Count of the status codes read
"""
import sys
import re

CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total_size, codes):
    """ printing occurs in this method """
    uniq_codes = {x: codes.count(x) for x in sorted(set(codes)) if x in CODES}
    print("File size: {:d}".format(total_size))
    for code, n in uniq_codes.items():
        print("{:s}: {:d}".format(code, n))


count = 0
code_list = list()
total_size = 0
exp = r'[\S]*[\s]*-[\s]*\[.*\][\s]*"GET.*HTTP/1.1"\s([\S]+)\s([0-9]+)'

try:
    for line in sys.stdin:
        count += 1
        if (m := re.search(exp, line, re.A)):
            status_code = m.group(1)
            size = m.group(2)
        else:
            continue
        code_list.append(status_code)
        total_size += int(size)
        if count % 10 == 0:
            print_stats(total_size, code_list)
except KeyboardInterrupt:
    print_stats(total_size, code_list)
    raise
print_stats(total_size, code_list)
