#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  factorial.py
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
#  04.12.2014


def factorial(x):
	if x == 0:
		return 1
	elif type(x) == int and x>0:
		i=1
		y=x
		if i <= x:
			y = y*(y-1)
			i += 1
		return y
	else:
		return 'Sorry. The number must be integer positive'
#Debugging
print factorial(4)
print factorial(5)
print factorial(-4)
print factorial(4.5)
print factorial(0)

