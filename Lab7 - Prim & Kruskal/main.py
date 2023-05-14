import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from prim import prim_algorithm
from kruskal import kruskal_algorithm
from graph import generate_graph

sizes = [10, 100, 150, 200, 250, 300, 400, 500]
prim_time = []
kruskal_time = []

for size in sizes:
    graph = generate_graph(size)

    # Time Prim's algorithm
    start_time = time.perf_counter()
    prim_algorithm(graph)
    result = time.perf_counter() - start_time
    prim_time.append(round(result, 5))

    # Time Kruskal's algorithm
    start_time = time.perf_counter()
    kruskal_algorithm(graph)
    result = time.perf_counter() - start_time
    kruskal_time.append(round(result, 5))

def plot_results():
    table = PrettyTable(['Name/Nodes', '10', '100', '150', '200', '250', '300', '400', '500'])
    table.add_row(['Prim', prim_time[0], prim_time[1], prim_time[2], prim_time[3], prim_time[4], prim_time[5], prim_time[6], prim_time[7]])
    table.add_row(['Kruskal', kruskal_time[0], kruskal_time[1], kruskal_time[2], kruskal_time[3], kruskal_time[4], kruskal_time[5], kruskal_time[6], kruskal_time[7]])
    print(table)

    plt.plot(sizes, prim_time, label='Prim', color = 'red')
    plt.plot(sizes, kruskal_time, label='Kruskal', color = 'black')
    plt.xlabel('n Nodes')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid()
    plt.show()
    
plot_results()