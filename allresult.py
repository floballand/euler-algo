#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name :
 @brief : find all result to obtain 100.
 --------
 @author : INOPE <fballand.inope@gmail.com>
 @license : GPL3
"""

# --------
# Imports
# --------
import string
import sys, io, random
import locale
import math


# --------
# definition
# --------
def main():
    """ Main function
    """

    MaxNumber = 100 """GOAL VALUE, AND MAXIMUM RATE"""
    vecteur = [0, 0, 0 ,0 ,0]  """INPUT VECTEUR : YOU CAN CHANGE THIS SIZE"""
    limitMaxNumber = len(vecteur)

    while (sum(vecteur) <= (limitMaxNumber * MaxNumber)):
        vecteur[0]=-1
        while(vecteur[0] <MaxNumber):
            vecteur[0]+=1
            if (sum(vecteur) == MaxNumber):
                print(vecteur)

        if(vecteur[0]==MaxNumber):
            for j in range (1,limitMaxNumber):
                if((vecteur[j-1]==MaxNumber)):
                    vecteur[j-1] =0
                    vecteur[j]=vecteur[j]+1

    exit(0)


if __name__ == '__main__':
    main()
