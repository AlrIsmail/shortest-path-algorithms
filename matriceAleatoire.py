# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:27:38 2022

@author: Ismail
"""
import numpy.random as rd
import numpy as np
import random
def matriceAleatoire (n,a,b):
    return(matriceAleatoire2(n,a,b,50))
def matriceAleatoire2 (n,a,b,p):
    M = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            M[i,j]=random.choices([rd.randint(a,b+1),np.inf],weights=(p, 100-p))[0] 
    return M
if __name__=="__main__":
    print(matriceAleatoire2(10, 1, 10, 40))
    print(matriceAleatoire(10, 1, 10))