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
    MaxNumber=100
    currentDigit=0
    limitMaxNumber=2
    positionNumber=0
    vecteur=[0,0]
    
    incrementNumber=0

    while (sum(vecteur)<=(limitMaxNumber*MaxNumber)):
        i=0
        
        while (i!=MaxNumber):
            i+=1
            vecteur[currentDigit]=i
            
            if sum(vecteur)==sumMax:
                print(vecteur)
                vecteur[currentDigit]=0
                i=0
                break
        currentDigit+=1               
    exit(0)
    
if __name__ == '__main__':
    main()
