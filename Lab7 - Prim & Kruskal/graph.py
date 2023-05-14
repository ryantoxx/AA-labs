import random
import networkx as nx

random.seed(23)

def generate_graph(nodes):
    Graph = nx.complete_graph(nodes)
    Graph = nx.convert_node_labels_to_integers(Graph)

    for (u, v) in Graph.edges():
        Graph[u][v]['weight'] = random.randint(1, 10)

    return Graph
