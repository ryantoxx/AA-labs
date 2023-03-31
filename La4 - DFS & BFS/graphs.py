from graphviz import Digraph

def balanced_tree():
    tree = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [8, 9],
        5: [10, 11],
        6: [12, 13],
        7: [14, 15],
        8: [16, 17],
        9: [18, 19],
        10: [20, 21],
        11: [22, 23],
        12: [24, 25],
        13: [],
        14: [],
        15: [],
        16: [],
        17: [],
        18: [],
        19: [],
        20: [],
        21: [],
        22: [],
        23: [],
        24: [],
        25: []
    }
    return tree


def unbalanced_tree():
    tree = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [8, 9],
        7: [10, 11],
        8: [12, 13],
        9: [14, 15],
        10: [],
        11: [16],
        12: [17, 18],
        13: [19],
        14: [],
        15: [],
        16: [20],
        17: [21],
        18: [],
        19: [22, 23],
        20: [24],
        21: [25],
        22: [],
        23: [],
        24: [],
        25: []
    }
    return tree

def visualize_tree(tree, filename):
    g = Digraph()
    
    for node_id in tree:
        g.node(str(node_id))
        for child_id in tree[node_id]:
            if child_id:
                g.edge(str(node_id), str(child_id))
    g.render(filename, format='png', view=True)


visualize_tree(balanced_tree(),'balanced_tree')
visualize_tree(unbalanced_tree(), 'unbalanced_tree')