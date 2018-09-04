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

    MaxNumber=100
    currentDigit=0
    vecteur=[0,0,0]
    vecteurMem=list(vecteur)
    limitMaxNumber=len(vecteur)
    
    print(limitMaxNumber)

    while (sum(vecteur)<=(limitMaxNumber*MaxNumber)):
        i=0
        while (i<MaxNumber):
            i+=1
            vecteur[currentDigit]=i
            if(sum(vecteur)==100):
                print(vecteur)

        if(currentDigit==limitMaxNumber-1):
            f=0
            while(f<=currentDigit):
                vecteurMem[f]=vecteurMem[f]+1
                
                f+=1
            currentDigit=0
        else:
            currentDigit+=1
        vecteur = list(vecteurMem)
    exit(0)
    
if __name__ == '__main__':
    main()
