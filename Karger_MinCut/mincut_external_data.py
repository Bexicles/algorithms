import random

def read_data_graph():
    G ={} # blank dictionary

    with open('./karger_mincut_data.txt') as f:
        for line in f:
            if line.strip():
                node, edges = line.split(None, 1)
                G[node] = edges.split()

    return G