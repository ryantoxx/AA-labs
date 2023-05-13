import random
import time
import matplotlib.pyplot as plt

from bbp import bbp_algorithm
from spigot import spigot_pi
from gauss import gauss_algorithm
from prettytable import PrettyTable

random.seed(10)

def plot_algorithms_performance():
    sizes = [10, 100, 1000, 1500, 2000, 2500, 3000]
    bbp_times = []
    gauss_times = []
    spigot_times = []
    for i in sizes:
        start_time = time.perf_counter()
        bbp_algorithm(i)
        end_time = time.perf_counter()
        bbp_times.append(round(end_time - start_time, 5))
        
        start_time = time.perf_counter()
        gauss_algorithm(i)
        end_time = time.perf_counter()
        gauss_times.append(round(end_time - start_time, 5))
        
        start_time = time.perf_counter()
        spigot_pi(i)
        end_time = time.perf_counter()
        spigot_times.append(round(end_time - start_time, 5))
    
    plt.plot(sizes, bbp_times,label="bbp Alg", color = 'red')
    plt.plot(sizes, gauss_times, label="gauss Alg", color = 'blue')
    plt.plot(sizes, spigot_times, label="spigot Alg", color = 'green')
    plt.xlabel('Size of n-th digits')
    plt.ylabel('Time (s)')
    plt.title('Algorithm Performance')
    plt.legend()
    plt.grid()
    plt.show()
    
    myTable = PrettyTable(["Name", '10', '100', '1000', '1500', '2000', '2500', '3000'])
    myTable.add_row(["bbp Alg", bbp_times[0],bbp_times[1],bbp_times[2], bbp_times[3], bbp_times[4],
                    bbp_times[5], bbp_times[6]])
    myTable.add_row(["gauss Alg", gauss_times[0], gauss_times[1], gauss_times[2], gauss_times[3], gauss_times[4],
                     gauss_times[5], gauss_times[6]])
    myTable.add_row(["spigot Alg", spigot_times[0], spigot_times[1], spigot_times[2], spigot_times[3], spigot_times[4],
                     spigot_times[5], spigot_times[6]])
    print(myTable)
    
plot_algorithms_performance()


