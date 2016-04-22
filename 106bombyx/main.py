#!/usr/bin/env python3.4

import sys


class InvalidArgument(Exception):
    def __init__(self, msg):
        print(msg)
        exit(84)


def my_help():
    print("USAGE\n"
          "\t   ./106bombyx n [k | i0 i1]\n\n"
          "DESCRIPTION\n"
          "\t   n\tnumber of first generation individuals\n"
          "\t   k\tgrowth rate from 1 to 4\n"
          "\t   i0\tinitial generation (included)\n"
          "\t   i1\tfinal generation (included)")


def error_mngmt_1():
    try:
        i = 1
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError
        i = 2
        if n < 0:
            raise InvalidArgument("n must be greater than or equal to 0")
        if float(sys.argv[2]) > 4 or float(sys.argv[2]) < 1:
            raise InvalidArgument("k (%s) must be contained between "
                                  "1.0 included and 4.0 included" % sys.argv[2])
    except ValueError:
        print("%s (%s) must be a positive integer." %
              (("n" if i == 1 else "k"), sys.argv[i]), file=sys.stderr)
        exit(84)
    else:
        return n


def error_mngmt_2():
    try:
        for i in range(1, len(sys.argv)):
            sys.argv[i] = int(sys.argv[i])
            if sys.argv[i] < 0:
                raise ValueError
        if sys.argv[1] < 0:
            raise InvalidArgument("n must be greater than or equal to 0")
        if sys.argv[3] < sys.argv[2]:
            raise InvalidArgument("Argument 3 (%d) must be greater"
                                  " than argument 2 (%d)" % (sys.argv[3], sys.argv[2]))
    except ValueError:
        print("argument {} : {}"
              " must be a positive integer".format(i, sys.argv[i]),
              file=sys.stderr)
        exit(84)


def suite(k, xi):
    p = k * xi * (1000 - xi) / 1000
    if p < 0:
        p = 0
    return p


def args_3(n):
    for i in range(1, 101):
        print("%d %.2f" % (i, n))
        n = suite(float(sys.argv[2]), n)


def args_4():
    for k in range(100, 401):
        n = int(sys.argv[1])
        for i in range(1, int(sys.argv[2])):
            n = suite(k / 100, n)
        for i in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
            print("%.2f %.2f" % (k / 100, n))
            n = suite(k / 100, n)


if __name__ == "__main__":
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        my_help()
        exit(0)
    if len(sys.argv) not in [3, 4]:
        print("Invalid expression, see {} --help or -h".format(sys.argv[0]),
              file=sys.stderr)
        exit(84)
    if len(sys.argv) == 3:
        error_mngmt_1()
        args_3(int(sys.argv[1]))
    else:
        error_mngmt_2()
        args_4()
