def prim_algorithm(graph):
    start_node = list(graph.nodes())[0]
    selected_nodes = {start_node}
    selected_edges = []
    while len(selected_nodes) < len(graph.nodes()):
        min_weight = float('inf')
        min_edge = None

        for node in selected_nodes:
            for neighbor in graph.neighbors(node):
                if neighbor not in selected_nodes:
                    weight = graph[node][neighbor]['weight']
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (node, neighbor)

        selected_edges.append(min_edge)

        selected_nodes.add(min_edge[1])
    return selected_edges

