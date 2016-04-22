#!/usr/bin/env python3

import sys
from math import *


a = 0
b = 5000
n = 10000
h = (b - a) / n
diff = pi / 2


def function(x, fun):
    if x == 0:
        return 1
    p = 1
    for i in range(fun + 1):
        p *= sin(x / (2 * i + 1)) / (x / (2 * i + 1))
    return p


def rect(fun):
    res = 0
    for i in range(n):
        res += function(a + i * h, fun)
    res *= h
    print("I%d = %.10f" %(fun, res))
    if res - diff > -0.0000000001 and res - diff < 0:
        print("diff = 0.0000000000\n")
    else:
        print("diff = %.10f\n" %(res - diff))


def trapez(fun):
    res = 0
    for i in range(1, n):
        res += function(a + i * h, fun)
    res *= 2
    res += function(a, fun) + function(b, fun)
    res *= (h / 2)
    print("I%d = %.10f" %(fun, res))
    if res - diff > -0.0000000001 and res - diff < 0:
        print("diff = 0.0000000000\n")
    else:
        print("diff = %.10f\n" %(res - diff))


def simpson(fun):
    res1 = 0
    res2 = 0
    for i in range(0, n):
        res1 += function(a + i * h + h / 2, fun)
    res1 *= 4
    for i in range(1, n):
        res2 += function(a + i * h, fun)
    res2 *= 2
    res = res1 + res2
    res += function(a, fun) + function(b, fun)
    res *= (h / 6)
    print("I%d = %.10f" %(fun, res))
    if res - diff > -0.0000000001 and res - diff < 0:
        print("diff = 0.0000000000")
    else:
        print("diff = %.10f" %(res - diff))


def usage():
    print("USAGE:\n"
          "\t\t{} n\n"
          "DESCRIPTION\n"
          "\t\tn\tconstant defining the integral to be computed".format(sys.argv[0]))


def init_n():
    try:
        n = int(sys.argv[1])
    except ValueError:
        usage()
        exit(84)
    if n < 0:
        usage()
        exit(84)
    return n


def check_args():
    if "-h" in sys.argv or "--help" in sys.argv:
        usage()
        sys.exit(0)
    if len(sys.argv) != 2:
        usage()
        sys.exit(84)


def main():
    check_args()
    n = init_n()
    func = 1
    print("Rectangles:")
    rect(n)
    print("Trapezoids:")
    trapez(n)
    print("Simpson:")
    simpson(n)


if __name__ == '__main__':
    main()
