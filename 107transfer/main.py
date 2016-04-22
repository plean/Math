#!/usr/bin/env python3.4

import sys
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)


class InvalidArgument(Exception):
    def __init__(self, msg):
        print(msg)
        sys.exit(84)


def bonjour(tab):
    try:
        for i in range(1001):
            c = 1
            for t in range(0, len(tab), 2):
                a = 0
                b = 0
                if tab[t] != tab[t + 1]:
                    for j in range(len(tab[t])):
                        a += tab[t][j] * ((i / 1000) ** j)
                    for k in range(len(tab[t + 1])):
                        b += tab[t + 1][k] * ((i / 1000) ** k)
                    c *= (a / b)
            print("%.3g -> %.5f" % (i / 1000, c))
    except ZeroDivisionError:
        print("Denominator cannot be 0 (division by zero)", file=sys.stderr)
        sys.exit(84)


def to_int(tab):
    try:
        for k in range(len(tab)):
            for i in range(len(tab[k])):
                tab[k][i] = int(tab[k][i])
    except ValueError:
        my_help(84)


def function():
    tab = []
    for i in range(len(sys.argv[1:])):
        tab.append(sys.argv[i + 1].split("*"))
    to_int(tab)
    bonjour(tab)


def my_help(k):
    print("USAGE\n"
    "\t   ./107transfer [num den]*\n"
    "\n"
    "DESCRIPTION\n"
    "\t   num\tpolynomial numerator defined by its coeficients\n"
    "\t   den\tpolynomial denominator defined by its coeficients")
    sys.exit(k)


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        my_help(0)
    if not len(sys.argv) % 2 or len(sys.argv) <= 2:
        my_help(84)
    function()


if __name__ == '__main__':
    main()
    sys.exit(0)
