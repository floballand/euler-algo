#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : 
 @brief : 
 --------
 @author : INOPE <fballand.inope@gmail.com>
 @license : GPL3
"""

# --------
# Imports
# --------
import string
import sys,io,random
import locale
import math

"""
all result to 100 without size fixed
"""
# --------
# definition
# --------
def main():
    """ Main function
    """

    sumMax=100
    variationMaxNumber=100
    limitMinNumber=0
    limitMaxNumber=2
    positionNumber=0
    vecteur=[0,0]
    
    incrementNumber=0

    while (limitMinNumber!=limitMaxNumber):
        incrementNumber=0
        print(limitMinNumber)
        while (incrementNumber!=variationMaxNumber):
            incrementNumber+=1
            vecteur[limitMinNumber]=incrementNumber
            if sum(vecteur)==sumMax:
                print(vecteur)
                vecteur[limitMinNumber]=0
                break
        limitMinNumber+=1               
    exit(0)
    
if __name__ == '__main__':
    main()
