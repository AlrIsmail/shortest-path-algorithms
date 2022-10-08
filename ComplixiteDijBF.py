# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:58:12 2022

@author: Ismail
"""
import time
from matriceAleatoire import matriceAleatoire as ma
from dijkstra import algoDijkstra
from BellmanFord import algoBellmanFordv2
import matplotlib.pyplot as plt
import numpy as np
from math import log
def Dij(n):
    M = ma(n,1,5)
    start=time.perf_counter()
    algoDijkstra(M,0)
    stop=time.perf_counter()
    return(stop-start)
def BF(n):
    M = ma(n,1,5)
    start=time.perf_counter()
    algoBellmanFordv2(M,0)
    stop=time.perf_counter()
    return(stop-start)

X=np.arange(2,100,1)
Y=[Dij(x) for x in X]
Z=[BF(x) for x in X]
plt.figure(1)            
plt.plot(X,Y, 's', label="Dij")       
plt.plot(X,Z, 's', label="BF")
plt.legend()
plt.figure(2) 
plt.semilogy(X,Y, 's', label="Dij")
plt.semilogy(X,Z, 's', label="BF")
plt.legend()

""" On constate que la représentation graphique en semi-log est approximativement linéaire entre 40 et 100. Donc 
la fonction était approximativement polynomiale : ct**a. L'exposant a est la pente de la représentation semi-log, donc:"""

aBF=(log(BF(100))-log(BF(40)))/((100)-(40))
#print(aBF)

aDij=(log(Dij(100))-log(Dij(40)))/((100)-(40))
#print(aDij)

# Les résultats sont très variables. On moyennise sur 50 calculs successifs:
AD=[]
AB=[]
for i in range(50):
    aBF=(log(BF(100))-log(BF(40)))/((100)-(40))
    AB.append(aBF)
    aDij=(log(Dij(100))-log(Dij(40)))/((100)-(40))
    AD.append(aDij)

print("pente BellmenFord : ",np.mean(AB))
print("pente Dijkstra : ",np.mean(AD))
