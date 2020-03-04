#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:14:49 2020

@author: nitvishn
"""

sum_variable = 0

for j in range(1, 7):
    factorial = 1
    for i in range(1, j+1):
        factorial = factorial * i
    # s at this point is equal to j!
    sum_variable = sum_variable + factorial
    
print(sum_variable)
