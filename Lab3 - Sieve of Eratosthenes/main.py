import time
import matplotlib.pyplot as plt

from algorithms.firstAlgorithm import first_alg
from algorithms.secondAlgorithm import second_alg
from algorithms.thirdAlgorithm import third_alg
from algorithms.fourthAlgorithm import fourth_alg
from algorithms.fifthAlgorithm import fifth_alg
from prettytable import PrettyTable


sizes = [10, 50, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000]

firstA_time = []
secondA_time = []
thirdA_time = []
fourthA_time = []
fifthA_time = []
    
for i in sizes:
        
    start_time = time.perf_counter()
    first_alg(i)
    end_time = time.perf_counter()
    result1 = end_time - start_time
    firstA_time.append(round(result1, 5))
        
    start_time = time.perf_counter()
    second_alg(i)
    end_time = time.perf_counter()
    result2 = end_time - start_time
    secondA_time.append(round(result2, 5))
    
    start_time = time.perf_counter()
    third_alg(i)
    end_time = time.perf_counter()
    result3 = end_time - start_time
    thirdA_time.append(round(result3, 5))
    
    start_time = time.perf_counter()
    fourth_alg(i)
    end_time = time.perf_counter()
    result4 = end_time - start_time
    fourthA_time.append(round(result4, 5))
    
    start_time = time.perf_counter()
    fifth_alg(i)
    end_time = time.perf_counter()
    result5 = end_time - start_time
    fifthA_time.append(round(result5, 5))
    
myTable = PrettyTable(["Algorithm Nr. ", "10", "50", "100", "500", "1 000", "5 000", "10 000", "25 000", "50 000", "100 000"])
myTable.add_row(["First", firstA_time[0], firstA_time[1], firstA_time[2], firstA_time[3], firstA_time[4], firstA_time[5], firstA_time[6],
                 firstA_time[7], firstA_time[8], firstA_time[9]])
myTable.add_row(["Second", secondA_time[0], secondA_time[1], secondA_time[2], secondA_time[3], secondA_time[4], secondA_time[5],
                 secondA_time[6], secondA_time[7], secondA_time[8], secondA_time[9]])
myTable.add_row(["Third", thirdA_time[0], thirdA_time[1], thirdA_time[2], thirdA_time[3], thirdA_time[4], thirdA_time[5], thirdA_time[6],
                 thirdA_time[7], thirdA_time[8], thirdA_time[9]])
myTable.add_row(["Fourth", fourthA_time[0], fourthA_time[1], fourthA_time[2], fourthA_time[3], fourthA_time[4], fourthA_time[5], fourthA_time[6],
                 fourthA_time[7], fourthA_time[8], fourthA_time[9]])
myTable.add_row(["Fifth", fifthA_time[0], fifthA_time[1], fifthA_time[2], fifthA_time[3], fifthA_time[4], fifthA_time[5], fifthA_time[6],
                fifthA_time[7], fifthA_time[8], fifthA_time[9]])
print(myTable)
        
plt.plot(sizes, firstA_time, label = "Algorithm 1", color = "red")
plt.plot(sizes, secondA_time, label = "Algorithm 2", color = "blue")
plt.plot(sizes, thirdA_time, label = "Algorithm 3", color = "green")
plt.plot(sizes, fourthA_time, label = "Algorithm 4", color = "pink")
plt.plot(sizes, fifthA_time, label = "Algorithm 5", color = "black")
plt.xlabel("Number of the list")
plt.ylabel("Time (s)")
plt.title("Sieve of Eratosthenes Algorithms")
plt.legend()
plt.grid()
plt.show()


        
        
                
                

        