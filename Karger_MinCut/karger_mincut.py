import random
from mincut_external_data import read_data_graph

best_min_cut = 1000

def pick_edge(G):
    # method to select an edge at random
    edge = [0,0]
    edge[0] = random.choice(list(G))
    edge[1] = random.choice(list(G[edge[0]]))

    while edge[0] == edge[1]:
        edge[1] = random.choice(list(G[edge[0]]))

    print("edge chosen at random is...", edge)
    return edge


def contract_nodes(G, edge):
    # method to contract / merge two nodes of a graph, around a selected edge

    node_1 = edge[0]
    node_2 = edge[1]

    # combine lists of values for the two nodes
    both_edges = G.get(node_1) + G.get(node_2)
    G[node_1] = both_edges

    # removes 2nd node from keys
    G.pop(node_2)

    # removes 2nd node from other keys' values & replaces it with 1st node
    for key in G.keys():
        edges = G[key]
        for i in range(0, len(edges)):
            if edges[i] == node_2:
                edges[i] = node_1

    return G


def check_self_loops(G, edge):
    # method to check for self loops and remove them

    edges = G.get(edge[0])
    edges[:] = (x for x in edges if x != edge[0])

    return G

def min_cut(G):
    # algorithm which contracts nodes around randomly-selected edges, until only two nodes remain.

    num_nodes = (len(G))

    edge = pick_edge(G) # pick an edge in G, at random
    G = contract_nodes(G, edge) # contract / merge nodes either side of the selected edge
    G = check_self_loops(G, edge) # remove any edges that connect nodes to themselves
    num_nodes = (len(G)) # update count of number of nodes in graph, G

    minimum_cut = len(G[edge[0]])

    if num_nodes == 2: # if not base case, recurse
        return minimum_cut

    else:
        minimum_cut = min_cut(G)
        return minimum_cut

def run_min_cut():
    # method to run Karger's Min Cut algorithm N times and remembers the best min-cut result
    minimum_cut = 0

    for i in range(1, 50):
        G = read_data_graph()
        print("Graph is", G)
        minimum_cut = min_cut(G)

        global best_min_cut
        if minimum_cut < best_min_cut:
            best_min_cut = minimum_cut
            print("Best score so far...",best_min_cut)
        i += 1

    return best_min_cut




best_score = run_min_cut()
print("Best overall score is",best_score)



