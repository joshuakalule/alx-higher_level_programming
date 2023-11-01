#!/usr/bin/python3
for char in range(97, 123):
    if (char == 113 or char == 101):
        continue
    print("{}".format(chr(char)), end='')
