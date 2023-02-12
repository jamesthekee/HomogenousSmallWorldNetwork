import networkx as nx
import random
import matplotlib.pyplot as plt


# @py_random_state(3)
def homogeneous_small_word_graph(n, k, p, seed=None):
    """Returns a homogenous small-world graph.

    Parameters
    ----------
    n : int
        The number of nodes
    k : int
        Each node is joined with its `k` nearest neighbors in a ring
        topology. k is asssumed even
    p : float
        The probability of rewiring each edge
    seed : UNUSED
    """

    if k > n:
        raise nx.NetworkXError("k>n, choose smaller k or larger n")

    if k % 2 != 0:
        raise ValueError("Odd values for K not accepted")

    # If k == n, the graph is complete not Watts-Strogatz
    if k == n:
        return nx.complete_graph(n)

    G = nx.Graph()
    nodes = list(range(n))  # nodes are labeled 0 to n-1
    # connect each node to k/2 neighbors
    for j in range(1, k // 2 + 1):
        targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
        G.add_edges_from(zip(nodes, targets))

    # rewire edges from each node
    # loop over all nodes in order (label) and neighbors in order (distance)
    # no self loops or multiple edges allowed
    total_edges = (n*k) // 2
    steps = int(total_edges*p)

    i = 0
    while i < steps:
        ab = random.choice(list(G.edges))
        cd = random.choice(list(G.edges))

        while cd == ab:
            cd = random.choice(list(G.edges))

        a, b = ab
        c, d = cd

        # Ensure a,b,c,d are all distinct
        if a == c or a == d or b == c or b == d:
            continue

        # Prevent double edges
        if G.has_edge(a, d) or G.has_edge(b, c):
            continue

        # Rewire edges to AD, BC
        G.add_edge(a, d)
        G.add_edge(b, c)
        G.remove_edge(a, b)
        G.remove_edge(c, d)

        i += 1
    return G


if __name__ == "__main__":
    g1 = nx.generators.watts_strogatz_graph(50, 2, 0)
    print(len(g1.edges))


    g2 = homogeneous_small_word_graph(50, 4, 0.1)
    nx.draw_networkx(g2)
    plt.show()


    print(set(list(zip(*g2.degree))[1]))




