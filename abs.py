#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : abs.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 27.09.2019
# Last Modified Date: 27.09.2019
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
def distance_from_zero(dist):
    if type(dist) == int or type(dist) == float:
        return abs(dist)
	print abs(dist)
    else:
        return "Nao"
	print "Nao"
#print distance_from_zero(-9.5)
#print distance_from_zero(False)
distance_from_zero(-9.5)
distance_from_zero(False)

