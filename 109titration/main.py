#!/usr/bin/env python3

import sys
import math


class InvalidFile(Exception):
    def __init__(self, msg):
        print(msg, file=sys.stderr)
        Exception.__init__(self, msg)
        sys.exit(84)


def my_help():
    print("USAGE\n"
          "\t\t" + sys.argv[0] + ' file\n'
          'DESCRIPTION\n'
          '\t\tfile a csv file containing "vol;ph" lines')


def check_error():
    if "-h" in sys.argv or "--help" in sys.argv:
        my_help()
        sys.exit(0)
    if len(sys.argv) != 2:
        print("Invalid number of arguments. See man or --help", file=sys.stderr)
        sys.exit(84)


def bonjour(tab):
    pns = 0.0
    derv = []
    k = 0
    s = 1
    print("Derivative:")
    derv.append(0)
    for i in range(1, len(tab) - 1):
        derv.append((tab[i + 1][1] - tab[i - 1][1]) / (tab[i + 1][0] - tab[i - 1][0]))
        print("volume: %g ml -> %.2f" % (tab[i][0], derv[i]))
        if pns < derv[i]:
            pns = derv[i]
            s = tab[i][0]
            k = i
    derv.append(0)
    print("\n"
          "Equivalent point at %g ml\n" % s)
    print("Second derivative:")
    for i in range(1, len(derv) - 3):
        p = (derv[i + 2] - derv[i]) / (tab[i + 2][0] - tab[i][0])
        print("volume: %g ml -> %.2f" % (tab[i + 1][0], p))
    print("\nSecond derivative estimated:")

    r = s
    e = 0
    if k - 2 < 0:
        i = tab[k - 1][0]
        p = v1 = 0
    else:
        i = tab[k - 1][0]
        p = v1 = (derv[k] - derv[k - 2]) / (tab[k][0] - tab[k - 2][0])
    v2 = (derv[k + 1] - derv[k - 1]) / (tab[k + 1][0] - tab[k - 1][0])
    z = (v2 - v1) / (10 * (tab[k][0] - tab[k - 1][0]))
    while i - 0.05 < tab[k][0]:
        print("volume: %g ml -> %.2f" % (i, v1))
        if math.fabs(p) > math.fabs(v1) and k - 1 > 0:
            p = v1
            r = i
        v1 += z
        i += 0.1

    if k + 3 >= len(derv):
        z = -v2 / 10
    else:
        v1 = (derv[k + 2] - derv[k]) / (tab[k + 2][0] - tab[k][0])
        z = (v1 - v2) / (10 * (tab[k + 1][0] - tab[k][0]))
    v2 += z
    while i - 0.05 < tab[k + 1][0]:
        print("volume: %g ml -> %.2f" % (i, v2))
        v2 += z
        i += 0.1
        if math.fabs(p) > math.fabs(v2) and k + 3 < len(tab):
            p = v2
            r = i
    print("\nEquivalent point at %g ml" % r)


def parse_file(f):
    tab = f.readlines()
    try:
        for i in range(len(tab)):
            tab[i] = tab[i].strip('\n').split(';')
            tab[i][0] = float(tab[i][0])
            tab[i][1] = float(tab[i][1])
            if len(tab[i]) != 2:
                raise IndexError
    except (ValueError, IndexError):
        print("Invalid line : %s" % tab[i], file=sys.stderr)
        sys.exit(84)
    else:
        return tab


def main():
    check_error()
    try:
        with open(sys.argv[1]) as f:
            tab = parse_file(f)
        if len(tab) <= 4:
            raise InvalidFile("Not enough data in file")
    except (PermissionError, FileNotFoundError) as e:
        print(e, file=sys.stderr)
        sys.exit(84)
    else:
        bonjour(tab)

if __name__ == '__main__':
    main()
    sys.exit(0)
