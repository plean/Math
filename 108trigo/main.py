#!/usr/bin/env python3

import sys
from functions import *


def tab_fcts():
    fct_tab = [my_exp, my_cos, my_cosh, my_sinh]


def my_help():
    print("USAGE\n"
          "\t\t./108trigo fun a0 a1 a2....\n"
          "\n"
          "DESCRIPTION\n"
          "\t\tfun\tfunction to be applied,"
          ' among at least "EXP", "COS", "SIN", "COSH" and "SINH"\n'
          '\t\tai\tcoeficients of the matrix')
    sys.exit(0)


def check_parameters():
    if "--help" in sys.argv or "-h" in sys.argv:
        my_help()
    if len(sys.argv) <= 2 \
            or sys.argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        print("Bad format, see --help, -h, or man entry for more info",
              file=sys.stderr)
        sys.exit(84)
    try:
        for i in range(2, len(sys.argv)):
            sys.argv[i] = float(sys.argv[i])
    except ValueError:
        print("Argument %d (%s) must be a number"
              % (i, sys.argv[i]), file=sys.stderr)


def error_mngmt():
    i = len(sys.argv) - 2
    sqi = trunc(sqrt(i))
    if trunc(sqrt(i)) ** 2 != i:
        print("Not enough parameters to create a matrix",
              file=sys.stderr)
        sys.exit(84)
    return sqi


def print_matrix(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%.2f%c" % (tab[i][j],
                              '\t' if (j != len(tab[i]) - 1) else '\n'),
                  end="")


def launch_func(tab):
    args = ["EXP", "COS", "SIN", "COSH", "SINH"]
    fct_tab = [my_exp, my_cos, my_sin, my_cosh, my_sinh]
    for i in range(len(fct_tab)):
        if sys.argv[1] == args[i]:
            tab = fct_tab[i](tab)
    return tab


def main():
    tab = []
    check_parameters()
    sqi = error_mngmt()
    for i in range(int(sqi)):
        tab.append([])
        for j in range(int(sqi)):
            tab[i].append(sys.argv[i * int(sqi) + j + 2])
    tab = launch_func(tab)
    print_matrix(tab)


if __name__ == '__main__':
    main()
    sys.exit(0)
