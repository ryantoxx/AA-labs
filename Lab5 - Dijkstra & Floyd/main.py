import time
from floyd import floyd_warshall
from dijkstra import dijkstra
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from graphs import generate_graph, generate_complete_graph


def exec_alg(graph):
    
    start_time = time.perf_counter()
    floyd_warshall(graph)
    floyd_time.append(round(time.perf_counter() - start_time, 5))

    start_time = time.perf_counter()
    for node in graph.nodes():
        dijkstra(graph, node)
    dijkstra_time.append(round(time.perf_counter() - start_time, 5))


def exec_info(case):

    if case == 0: 
        print('\n100-node Graph')
        table = PrettyTable(['Name/Edges', '4950', '3712', '2475', '1237', '618', '290'])
    elif case == 1: 
        print('\n200-node Graph')
        table = PrettyTable(['Name/Edges', '19900', '15654', '10787', '5676', '2265', '1876'])
    table.add_row(['Floyd', floyd_time[0], floyd_time[1], floyd_time[2], floyd_time[3], floyd_time[4], floyd_time[5]])
    table.add_row(['Dijkstra', dijkstra_time[0], dijkstra_time[1], dijkstra_time[2], dijkstra_time[3], dijkstra_time[4], dijkstra_time[5]])
    print(table)

    plt.plot(edges_count, floyd_time, label='Floyd', color = 'red')
    plt.plot(edges_count, dijkstra_time, label='Dijkstra', color = 'black')
    plt.xlabel('n Edges')
    plt.ylabel('Time (s)')
    if case == 0: plt.title('100-node Graph')
    elif case == 1: plt.title('200-node Graph')
    plt.legend()
    plt.show()


floyd_time = []
dijkstra_time = []

g_max = generate_complete_graph(100)
g_1 = generate_graph(100, 3712)
g_2 = generate_graph(100, 2475)
g_3 = generate_graph(100, 1237)
g_4 = generate_graph(100, 618)
g_5 = generate_graph(100, 290)

edges_count = [4950, 3712, 2475, 1237, 618, 290]

exec_alg(g_max)
exec_alg(g_1)
exec_alg(g_2)
exec_alg(g_3)
exec_alg(g_4)
exec_alg(g_5)
exec_info(0)

floyd_time.clear()
dijkstra_time.clear()

g_max = generate_complete_graph(200)
g_1 = generate_graph(200, 15654)
g_2 = generate_graph(200, 10787)
g_3 = generate_graph(200, 5674)
g_4 = generate_graph(200, 2265)
g_5 = generate_graph(200, 1876)

edges_count = [19900, 15654, 10787, 5674, 2265, 1876]

exec_alg(g_max)
exec_alg(g_1)
exec_alg(g_2)
exec_alg(g_3)
exec_alg(g_4)
exec_alg(g_5)
exec_info(1)