# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:22:24 2022

@author: ismail
"""
from math import inf #importation de la bibliothèque inf
import numpy as np #importation de la bibliothèque numpy
import random #importation de la bibliothèque 
import matplotlib.pyplot as plt #importation de la bibliothèque pyplot
from matriceAleatoire import matriceAleatoire2 #importation de la bibliothèque matriceAleatoire

def algoBellmanFord(M, si, fleches, n): #defintion de  l'algorithme de BellmanFord avec en entrer M, si, fleches, n
    dist, pred = [], [] # definition de des tableau distance et du predecesseur 
    for i in range(n): #bloucle for tant que i est dans n 
        pred.append(None)# ajouter None au predecesseur
        if (i == si): #condition si i est egale a si
            dist.append(0) #jouter 0 a distance
        else: #sinon 
            dist.append(inf) #ajouter inf a distance 
    change, cmp = True, 1 #definition du boolean change et compteur
    while(change and cmp < n ): #boucle tant que change et commpteur son infrieure a n
        change = False #change égale faux 
        cmp += 1 #compteur gange 1
        for f in fleches: #pour f dans fleches faire
            if (dist[f[0]] + M[f[0],f[1]] < dist[f[1]]): #si distance de f de 0 + M de f de 0 et de 1 infrieur a distance de f de 1 faire
                change = True 
                dist[f[1]] = dist[f[0]] + M[f[0],f[1]]# distance de f de 1 egale a distance de f de 0 + m de f de 0, f de A 
                pred[f[1]] = f[0] #pred de f de 1 égale a f de 0
    if change == True: #si change est vrai alors 
        return("pas de plus court chemin : présence d’un cycle de poids négatif") #retourner le texte*
    res = []# defintion du tableau res
    for s in range(n): #pour s dans n faire
        liste = [s] 
        p = pred[s]
        if p is None and s is not si: #si p est None et s n'est pas si :
            res.append([str(s) + " sommet non joignable à s0 par un chemin dans le graphe G"])
        else: # sinon 
            while (p is not None): #tant que p est pas Null
                liste.append(p) #ajouter p a la liste 
                p = pred[p]
            res.append([int(dist[s]),liste])# ajouter distance de s et la liste a res
    return res, cmp #retourner le resultat et le compteur
    # resultat est de fromat [[sommet 0], [sommet 1], [sommet 2]] ou chaque sommet a longeur et iteneraire
    # cheque sommet est de format [longeur plus court chemin , iteneraire]
def algoBellmanFordv1(M,si): #defintion avec M et si en entrer
    temp, fleches = [], [] #création des tableau temp et fleche 
    n = len(M) #creation n la taille de M
    for i in range(n): #pour i dans la r faire
        for j in range(n): #pour i dans la r faire
            if (M[i,j] != inf):#si M de i,j est deferent de inf
                temp.append([i,j])#ajouter [i,j] a temp
    l = len(temp) #definition de len
    while (l != len(fleches)):#tant que l est diffrent de la longueur de fleches
        x = random.randrange(0,l)#defintion de x chiffre aleatoire entre 0 et l
        if temp[x] not in fleches:#si temp de x n'est pas dans fleche alors faire
            fleches.append(temp[x])#ajouter x de temp a fleche 
    return(algoBellmanFord(M, si, fleches, n))#retourn apres avoir appliquer bellmanford
    
def algoBellmanFordv2(M,si): # largeur
    n=len(M)
    couleur={}     # On colorie tous les sommets en blanc et s en vert
    for i  in range(n):
        couleur[i]='blanc'
    couleur[si]='vert'
    file=[si]
    Liste_rouge=[]
    while file !=[]:
        i=file[0]           # on prend le premier terme de la file
        for j in range(n):  # On enfile les successeurs de i encore blancs:
            if (M[file[0]][j]!= inf and couleur[j]=='blanc'):
                file.append(j)
                couleur[j]='vert' # On les colorie en vert
        couleur[i]='rouge'     # on colorie i en rouge
        Liste_rouge.append(i)  # on met i en liste rouge
        file.pop(0) # on défile i
    fleches = []
    for i in Liste_rouge:
        for j in range(n):
            if (M[i,j] != inf):
                fleches.append([i,j])
    return(algoBellmanFord(M, si, fleches, n))
def algoBellmanFordv3(M,si): # profondeur
    n=len(M)       # taille du tableau = nombre de sommets
    couleur={}     # On colorie tous les sommets en blanc et s en vert
    for i  in range(n):
        couleur[i]='blanc'
    couleur[si]='vert'
    pile=[si]       # on initialise la pile à s
    Resultat=[si] # on initialise la liste des résultats à s
    
    while pile !=[]: # tant que la pile n'est pas vide,
        i=pile[-1]          # on prend le dernier sommet i de la pile
        Succ_blanc=[]       # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if (M[i,j]!= inf and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc!=[]:  # s'il y en a,
            v= Succ_blanc[0]    # on prend le premier (si on veut l'ordre alphabétique)
            couleur[v]='vert'   # on le colorie en vert, 
            pile.append(v)      # on l'empile
            Resultat.append(v)  # on le met en liste rsultat
        else:               # sinon:
            pile.pop()          # on sort i de la pile
    fleches = []
    for i in Resultat:
        for j in range(n):
            if (M[i,j] != inf):
                fleches.append([i,j])            
    return(algoBellmanFord(M, si, fleches, n))  
      
##################################################test
if __name__=="__main__":

    mat = np.array([[inf, 3, inf, inf, inf, inf],
                    [inf,inf,4,inf,2,1],
                    [inf,-1,inf,inf,inf,inf],
                    [2,inf,inf,inf,8,inf],
                    [inf,inf,inf,inf,inf,9],
                    [inf,inf,inf,inf,-3,inf]])
    print("exemple 1 v1: ", algoBellmanFordv1(mat, 3))
    print("exemple 1 v2: ", algoBellmanFordv2(mat, 3))
    print("exemple 1 v3: ", algoBellmanFordv3(mat, 3))
    mat = np.array([[inf, 1, inf, inf],
                    [inf, inf, -1, inf],
                    [inf, inf, inf, -1],
                    [-1, inf, inf, inf]])
    print("exemple 2: ",algoBellmanFordv1(mat, 3))
    X=np.arange(1,50,1)
    m = [matriceAleatoire2(50,1,2, 20) for x in X]
    Y=[algoBellmanFordv1(m[x], 0)[1] for x in range(len(m))]
    Z=[algoBellmanFordv2(m[x], 0)[1] for x in range(len(m))]
    a=[algoBellmanFordv3(m[x], 0)[1] for x in range(len(m))]
    plt.figure(1)            
    plt.plot(X,Y, label="v1")       
    plt.plot(X,Z, label="v2")
    plt.plot(X,a, label="v3")
    plt.legend()
 

        