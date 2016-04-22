from math import *


def identity_mat(n):
    tmp = []
    for i in range(n):
        caca = []
        for j in range(n):
            caca.append(1 if j == i else 0)
        tmp.append(caca)
    return tmp


def init_mat(n, k):
    tmp = []
    for i in range(n):
        caca = []
        for j in range(n):
            caca.append(k)
        tmp.append(caca)
    return tmp


def mat_mult(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        moustique = []
        for j in range(len(mat2[0])):
            a = 0
            for k in range(len(mat1[0])):
                a += mat1[i][k] * mat2[k][j]
            moustique.append(a)
        tmp.append(moustique)
    return tmp


def pow_mat(mat, n):
    tmp = mat
    for i in range(n - 1):
        tmp = mat_mult(tmp, mat)
    return tmp


def div_mat(mat, k):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] /= k
    return mat


def add_mat(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] + mat2[i][j])
        tmp.append(c)
    return tmp


def sub_mat(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] - mat2[i][j])
        tmp.append(c)
    return tmp
