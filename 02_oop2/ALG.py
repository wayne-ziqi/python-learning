#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 22/2/19 11:32
# @Author   : Wayne Qi
# @FileName : ALG.py
# @Software : PyCharm
# @Email    : wayne-ziqi@gmail.com

def preLargest(A):
    n = len(A)
    P = [0 for _ in range(n)]
    for i in range(1, n):
        j = i - 1
        while j >= 0:
            if A[j] > A[i]:
                P[i] = j + 1
                break
            elif P[j] != 0:
                j = P[j] - 1
            else:
                break;
    return P


A = [7, 3, 9, 10, 8, 3, 4, 2, 1, 5]
print(preLargest(A))

import types
types.BuiltinFunctionType== type(A)

isinstance([1,2,3], (list, tuple))