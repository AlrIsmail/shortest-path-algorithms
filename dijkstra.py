# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:29:08 2022

@author: Ísmail
"""
#importion des bibliotheque utile
from math import inf
import numpy as np

def algoDijkstra(M, si): #defintion des valeure en entrer des algorithme
    n = len(M)# definition de n la longuere de M
    dist, pred, pris = [], [], []#definition des tableau distance, predeceseur, pris
    for s in range(n):#premier boucle pour s dans dans n
        pris.append(0) #on ajoute 0 a pris
        if (s == si):#si s est égale a si alors
            dist.append(0) #on ajoute 0 a dist
            pris[s] = 1
            pred.append(None) #pred devient null
        elif (M[si,s] == inf):#sinon si M de si et s est egale a inf 
            dist.append(inf) #on ajoute inf a dist
            pred.append(None)#et pred devient null
        else:   #sinon
            dist.append(M[si,s])#ajoute si de s de M a dist
            pred.append(si)#ajouter si a pred
    A = [si]
    cmpt =0
    fin = 0
    while(cmpt != n and not fin):#deuxieme boucl while tant que cmpr est different de n
        cmpt += 1 
        distMin = inf
        sMin = -1
        for s in range(n): # tant que s est dans n faire
            if ( not pris[s] and dist[s] < distMin):#si not s de pris et s de dist sont inferieur a distmin faire
                distMin = dist[s] #distMin devient s de dist
                sMin = s
        if sMin != -1:# si smin est different de 1 faire
            A.append(sMin) #ajouter sMin a A
            pris[sMin] = 1
        else:#sinon faire
            fin = 1 #fin devient 1
        for s in range(n):#tant que s est dans n faire 
            if (not pris[s] and dist[sMin] + M[sMin,s] < dist[s]):#si not s de pris et smin de dist plus sMin de s de M est inferieure a s de dist faire
                    dist[s] = dist[sMin] + M[sMin,s]# s de dist est egale smin de dist plus sMin de s de M
                    pred[s] = sMin# et s de pred est égale a sMin
    res = []#création du tableau res
    for s in range(n):#pour s dans n faire 
        liste = [s]
        p = pred[s]
        if p is None and s is not si:#si p est null et s est  pas si alors faire
            res.append([str(s) + " sommet non joignable à s0 par un chemin dans le graphe G"])#ajouter str de s avec la phrase dans res
        else:#sinon
            while (p is not None):#tant que p n'est pas null alors faire
                liste.append(p)#ajouter p a list
                p = pred[p]
            res.append([int(dist[s]),liste])#ajouter l'integer s de dist avec liste a res
    return res#renvoie res

########################################################################
if __name__=="__main__":                
    mat = np.array([[inf, 4, 6, inf, 8, inf, inf, inf],
                    [inf,inf,1,inf,2,inf,inf,inf],
                    [inf,inf,inf,4,inf,4,6,inf],
                    [inf,inf,inf,inf,inf,inf,3,inf],
                    [inf,inf,inf,inf,inf,1,inf,inf],
                    [inf,2,inf,4,1,inf,2,inf],
                    [inf,inf,inf,inf,inf,inf,inf,inf],
                    [inf,inf,inf,3,inf,inf,2,inf]])
    
    print(algoDijkstra(mat, 0))





