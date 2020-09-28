#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : combinatory.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 27.09.2019
# Last Modified Date: 02.05.2020
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>

str1 = 'AB'
str2 = '34'

comb = [ x + y for y in str2 for x in str1]
print(comb)

# ['A3', 'B3', 'A4', 'B4']

comb_iter = ( x + y for y in str2 for x in str1)
print(next(comb_iter))
print(next(comb_iter))
print(*comb_iter)

