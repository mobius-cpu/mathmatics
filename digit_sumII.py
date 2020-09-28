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
n_str = raw_input("Escreva um numero inteiro positivo ",)
n = float(n_str)
while n<0 or n-int(n)>0:
	n_str = raw_input("Escreva um numero inteiro positivo ",)
	n = float(n_str)
i = 1
while n//10**i > 10:
	i += 1
print 'The number have '+ str(i+1) + ' elements'

soma = n%10
soma += n//10**i
m = n-(n//10**i)*10**i
soma += m//10**i

print 'A soma dos algarismos é '+ str(soma)

