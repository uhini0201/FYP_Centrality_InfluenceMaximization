''' File for testing different files
'''
__author__ = 'Uhini'

import networkx as nx

from icCode import runIC
from degreeDiscount import degreeDiscountIC

import matplotlib.pylab as plt
import os

if __name__ == '__main__':
    import time
    start = time.time()

    # read in graph
    G = nx.Graph()
    with open('../graphdata/hep.txt') as f:
        n, m = f.readline().split()
        for line in f:
            a,b=map(str,line.split())
            u, v = map(int, line.split())
            try:
                G[u][v]['weight'] += 1
            except:
                G.add_edge(u,v, weight=1)
            # G.add_edge(u, v, weight=1)
            #print(nx.shortest_path(str(u),str(v),weight=1))
    print('Built graph G')
    print(time.time() - start)

    #calculate initial set
    seed_size = 10
    S = degreeDiscountIC(G, seed_size)
    print('Initial set of', seed_size, 'nodes chosen')
    print(time.time() - start)

    # write results S to file
    with open('visualisation.txt', 'w') as f:
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 200 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(G, S)
        avg += float(len(T))/iterations
        print(i, 'iteration of IC')
    print('Avg. Targeted', int(round(avg)), 'nodes out of', len(G))
    print(time.time() - start)

    with open('lemma1.txt', 'w') as f:
        f.write(str(len(S)) + os.linesep)
        for node in T:
            f.write(str(node) + os.linesep)

    console = []