from matrix import *


def my_exp(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 18):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, i), factorial(i)))
    return tmp


def my_cos(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 17):
        if i % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i), factorial(2 * i)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * i), factorial(2 * i)))
    return tmp


def my_sin(tab):
    tmp = tab
    for i in range(1, 17):
        if i % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), factorial(2 * i + 1)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), factorial(2 * i + 1)))
    return tmp


def my_cosh(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 17):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i), factorial(2 * i)))
    return tmp


def my_sinh(tab):
    tmp = tab
    for i in range(1, 17):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), factorial(2 * i + 1)))
    return tmp
