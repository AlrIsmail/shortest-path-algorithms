# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:52:04 2022

@author: Ismail
"""

import networkx as nx
import matplotlib.pyplot as plt
import pylab
from matriceAleatoire import matriceAleatoire as ma
from math import inf
import random
from BellmanFord import algoBellmanFordv2
import numpy as np

def visualiserGraph(m):
    G = nx.DiGraph()
    n = len(m)
    for i in range(n):
        for j in range(n):
            if (m[i,j] != inf):
                G.add_edges_from([(i, j)], weight=int(m[i,j]))
    
    val_map = {}
    for i in range(n):
        val_map[i] = random.random()
    
    values = [val_map.get(node, 0.45) for node in G.nodes()]
    edge_labels=dict([((u,v,),d['weight'])
                     for u,v,d in G.edges(data=True)])
    
    pos=nx.spring_layout(G)
    node_labels = {node:node for node in G.nodes()}
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw(G,pos, node_color = values, node_size=1500,edge_cmap=plt.cm.Reds)
    pylab.show()


def visualiserPlusCourtChemin(m):
    G = nx.DiGraph()
    n = len(m)
    for i in range(n):
        for j in range(n):
            if (m[i,j] != inf):
                G.add_edges_from([(i, j)], weight=int(m[i,j]))
    
    val_map = {}
    for i in range(n):
        val_map[i] = random.random()
    
    values = [val_map.get(node, 0.45) for node in G.nodes()]
    edge_labels=dict([((u,v,),d['weight'])
                     for u,v,d in G.edges(data=True)])
    fleches = []
    for i in algoBellmanFordv2(m, 0)[0]:
        if len(i) == 2:
            if i[1] is not str:
                fleches.append(i[1])
    f = set()
    for i in fleches:
        l = len(i)
        if  l > 1:
            for j in range(l-1):
                f.add((i[j+1],i[j]))
    red_edges = list(f)
    edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
    
    pos=nx.spring_layout(G)
    node_labels = {node:node for node in G.nodes()}
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw(G,pos, node_color = values, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
    pylab.show()
    
if __name__=="__main__":
    mat = ma(5,1,5)
    visualiserGraph(mat)
    # le plus il y des sommets a visualisser plus c'est diffficle de lire le graph
    mat = np.array([[inf, 4, 6, inf, 8, inf, inf, inf],
                    [inf,inf,1,inf,2,inf,inf,inf],
                    [inf,inf,inf,4,inf,4,6,inf],
                    [inf,inf,inf,inf,inf,inf,3,inf],
                    [inf,inf,inf,inf,inf,1,inf,inf],
                    [inf,2,inf,4,1,inf,2,inf],
                    [inf,inf,inf,inf,inf,inf,inf,inf],
                    [inf,inf,inf,3,inf,inf,2,inf]])
    visualiserPlusCourtChemin(mat)
    # exemple plus simple
    mat = np.array([[inf, 4, 6, inf],
                    [inf,inf,1,inf],
                    [inf,inf,inf,4],
                    [3,inf,inf,inf]])
    visualiserPlusCourtChemin(mat)