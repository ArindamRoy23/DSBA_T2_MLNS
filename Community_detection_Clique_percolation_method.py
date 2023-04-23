import matplotlib.pyplot as plt
from multiprocessing import Pool
import itertools
import networkx as nx
import numpy as np
import itertools


def get_cliques(graph, size):
    """
    Returns a list of cliques of size 'size' in the graph.
    """
    cliques = []
    nodes = set(graph.keys())
    for node in nodes:
        neighbors = set(graph[node])
        for clique_nodes in itertools.combinations(neighbors, size - 1):
            clique = set(clique_nodes)
            clique.add(node)
            if all(n in graph[other_node] for n in clique for other_node in clique - {n}):
                cliques.append(clique)
    return cliques

def get_overlap(clique1, clique2):
    """
    Returns the size of the overlap between two cliques.
    """
    return len(clique1.intersection(clique2))

def get_percolated_cliques(cliques, k):
    """
    Returns a list of percolated cliques with size 'k' in the graph.
    """
    percolated_cliques = []
    for clique1, clique2 in itertools.combinations(cliques, 2):
        overlap = get_overlap(clique1, clique2)
        if overlap >= k - 1:
            percolated_cliques.append(clique1.union(clique2))
    return percolated_cliques

def clique_percolation(graph, k):
    """
    Returns a list of percolated cliques with size 'k' in the graph.
    """
    cliques = get_cliques(graph, k)
    percolated_cliques = get_percolated_cliques(cliques, k)
    return percolated_cliques

# Load the dataset
circles_file = r'facebook_combined.txt/facebook_combined.txt'
G = nx.read_edgelist(circles_file)

graph_dict = {str(node): [str(neighbor) for neighbor in G.neighbors(str(node))] for node in G.nodes()}

k = 10
percolated_cliques = clique_percolation(graph_dict, k)
print(percolated_cliques)