import random
import time
import matplotlib.pyplot as plt

from quickSort import quick_sort
from mergeSort import merge_sort
from heapSort  import heap_sort
from combSort import comb_sort
from prettytable import PrettyTable

random.seed(10)

start = - 500000
end = 500000

def plot_sorting_performance():
    sizes = [10, 100, 1000, 10000, 50000, 100000, 250000, 500000, 750000]
    quicksort_times = []
    mergesort_times = []
    heapsort_times = []
    combsort_times = []
    for size in sizes:
        arr = [random.randint(start, end) for _ in range(size)]
        start_time = time.time()
        quick_sort(arr)
        end_time = time.time()
        quicksort_times.append(round(end_time - start_time, 5))
        
        arr = [random.randint(start, end) for _ in range(size)]
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        mergesort_times.append(round(end_time - start_time, 5))
        
        arr = [random.randint(start, end) for _ in range(size)]
        start_time = time.time()
        heap_sort(arr)
        end_time = time.time()
        heapsort_times.append(round(end_time - start_time, 5))
        
        arr = [random.randint(start, end) for _ in range(size)]
        start_time = time.time()
        comb_sort(arr)
        end_time = time.time()
        combsort_times.append(round(end_time - start_time, 5))
    
    plt.plot(sizes, quicksort_times,label="quickSort", color = 'red')
    plt.plot(sizes, mergesort_times, label="mergeSort",color = 'blue')
    plt.plot(sizes, heapsort_times, label="heapSort",color = 'green')
    plt.plot(sizes, combsort_times, label="combSort",color = 'pink')
    plt.ylabel('Time (s)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.show()
    
    myTable = PrettyTable(["Name", '10', '100', '1000', '10 000', '50 000', '100 000', '250 000', '500 000', '750 000'])
    myTable.add_row(["quick Sort", quicksort_times[0],quicksort_times[1],quicksort_times[2], quicksort_times[3], quicksort_times[4],
                    quicksort_times[5], quicksort_times[6], quicksort_times[7], quicksort_times[8]])
    myTable.add_row(["merge Sort", mergesort_times[0], mergesort_times[1], mergesort_times[2], mergesort_times[3], mergesort_times[4],
                     mergesort_times[5], mergesort_times[6], mergesort_times[7], mergesort_times[8]])
    myTable.add_row(["heap Sort", heapsort_times[0], heapsort_times[1], heapsort_times[2], heapsort_times[3], heapsort_times[4],
                     heapsort_times[5], heapsort_times[6], heapsort_times[7], heapsort_times[8]])
    myTable.add_row(["comb Sort", combsort_times[0], combsort_times[1], combsort_times[2], combsort_times[3], combsort_times[4],
                     combsort_times[5], combsort_times[6], combsort_times[7], combsort_times[8]])
    print(myTable)
    
plot_sorting_performance()


