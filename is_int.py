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

# Verifica se a parte decimal é zero ou não. Se é zero o número é inteiro.
def is_int(x):
    if x-int(x) == 0:
        return True
    else:
        return False
print is_int(-12)
print is_int(7.00)
print is_int(7.0008)
print is_int(-1.00000)
print is_int(-77.000000000009)

