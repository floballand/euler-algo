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

    MaxNumber = 100
    vecteur = [0, 0, 0]
    limitMaxNumber = len(vecteur)

    while (sum(vecteur) <= (limitMaxNumber * MaxNumber)):
        i = 0
        vecteur[0]=0
        while(i <MaxNumber):
            i+=1
            vecteur[0]=i
            if (sum(vecteur) == MaxNumber):
                print("okkkk")
                print(vecteur)


        if(vecteur[0]==MaxNumber):
            for j in range (1,limitMaxNumber):
                if((vecteur[j-1]==MaxNumber)):
                    vecteur[j-1] =0
                    vecteur[j]=vecteur[j]+1


    exit(0)
    
if __name__ == '__main__':
    main()
