#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
#  
#  Copyright 2014 Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def digit_sum(n):
    if n > 0 and type(n) == int:
        n_str = str(n)
        soma = 0
        for i in range(0,len(n_str)):
            soma = soma+int(n_str[i])
	return soma
    else:
		print 'Esta função não aceita numeros que não seja positivos inteiros'

print digit_sum(123)
print digit_sum(123.0)
print digit_sum(-321)
print digit_sum(123.03)
