#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : casa_dos_pombos.py
# Author            : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
# Date              : 27.09.2019
# Last Modified Date: 27.09.2019
# Last Modified By  : Neri Luiz von Holleben <neri_luiz@yahoo.com.br>
#===============================================================================
#
#         FILE: test.py
#
#        USAGE: python2.7 casa_dos_pombos.py  
#
#  DESCRIPTION: Generalização do problema das casas dos pombos.
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Neri Luiz von Holleben <neri_luiz@yahoo.com.br> 
# ORGANIZATION: 
#      VERSION: 1.0
#     CREATED*: 2019-09-11 Wed 16:28 PM -0400 
#     REVISION: 2019-09-27 Fri 20:33 PM -0400 
#===============================================================================
# *In VIM use ":r! date "+\%Y-\%m-\%d \%H:\%M:\%S")DD/MM/YYYY hh:mm:ss"
#   or ":r !date --rfc-3339=s" or F3(its mapped as F3 in my .vimrc)

# Se m pombos são colocados em n casas de pombos então alguma delas conterá pelo menos floor((m-1)/n) + 1 pombos.
def casas_pombos(casas,pombos):
    """Returns how much some houses(places) will be occupied
    in excess in the most distributed scenario """
    return (casas-1)//pombos + 1

print(casas_pombos(301,100))
