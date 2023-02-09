import time
import decimal
from prettytable import PrettyTable
import matplotlib.pyplot as plt

sequence = [5, 7, 10, 15, 20, 25, 30, 35, 40]
sequence2 = [1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943]

# Fibonacci - recursive algorithm
def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return(recursive_fib(n-1) + recursive_fib(n-2))

rec = []

start = time.time()
for i in sequence:
    recursive_fib(i)
    end = time.time()
    rec.append(round(end-start, 8))

rec_tbl = PrettyTable(sequence)
rec_tbl.add_row(rec)
rec_tbl.add_autoindex('Nr.')
print('Recursive table')
print(rec_tbl)

plt.figure(1)
plt.plot(sequence, rec, color = 'blue')
plt.scatter(sequence, rec, color='blue')
plt.title('Recursive fibonacci algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()
    
    
# Fibonacci - dynamic programming algorithm
def dynamic_fib(n):
    d = [0, 1]
    for i in range(2, n + 1):
        d.append(d[i - 1] + d[i - 2])
    return d[n]

dyn = []

start = time.time()
for i in sequence2:
    dynamic_fib(i)
    end = time.time()
    dyn.append(round(end-start, 8))

dyn_tbl = PrettyTable(sequence2)
dyn_tbl.add_row(dyn)
dyn_tbl.add_autoindex('Nr.')
print('Dynamic table')
print(dyn_tbl)

plt.figure(2)
plt.plot(sequence2, dyn, color = 'black')
plt.scatter(sequence2, dyn, color = 'black')
plt.title('Dynamic fibonacci algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()


# Fibonacci - optimized dynamic programming algorithm
def ODP_fib(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
    
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

opd = []

start = time.time()
for i in sequence2:
    ODP_fib(i)
    end = time.time()
    opd.append(round(end - start, 8))

OPD_tbl = PrettyTable(sequence2)
OPD_tbl.add_row(opd)
OPD_tbl.add_autoindex('Nr.')
print('OPD table')
print(OPD_tbl)

plt.figure(3)
plt.plot(sequence2, opd, color = 'green')
plt.scatter(sequence2, opd, color = 'green')
plt.title('Optimised dynamic algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()


# Fibonacci - matrix power algorithm
def matrix_fib(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)

    return F[0][0] 

def power(F, n):

    M = [[1, 1],
         [1, 0]]

    for l in range(2, n + 1):
        multiply(F, M)

def multiply(F, M):

    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

matrix = []

start = time.time()
for i in sequence2:
    matrix_fib(i)
    end = time.time()
    matrix.append(round(end - start, 8))
    
matrix_tbl = PrettyTable(sequence2)
matrix_tbl.add_row(matrix)
matrix_tbl.add_autoindex('Nr.')
print('Matrix table')
print(matrix_tbl)

plt.figure(4)
plt.plot(sequence2, opd, color = 'red')
plt.scatter(sequence2, opd, color = 'red')
plt.title('Matrix algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()

# Fibonacci - binet formula method
def binet_fib(n):
    decimal.getcontext().prec = 100
    phi = (decimal.Decimal(1) + decimal.Decimal(5).sqrt()) / decimal.Decimal(2)
    phi2 = (decimal.Decimal(1) - decimal.Decimal(5).sqrt()) / decimal.Decimal(2)
    return int((phi**n - phi2**n) / decimal.Decimal(5).sqrt())

binets = []

start = time.time()
for i in sequence2:
    binet_fib(i)
    end = time.time()
    binets.append(round(end - start, 8))

binet_tbl = PrettyTable(sequence2)
binet_tbl.add_row(binets)
binet_tbl.add_autoindex('Nr.')
print('Binet table')
print(binet_tbl)

plt.figure(5)
plt.plot(sequence2, opd, color = 'purple')
plt.scatter(sequence2, opd, color = 'purple')
plt.title('Binet algorithm')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()

# Fibonacci - exp fib method
def exponentiation_fib(n):
    if n < 2:
        return n
    i = n - 1
    a, b = 1, 0
    c, d = 0, 1
    while i > 0:
        if i % 2 == 1:
            a, b = d * b + c * a, d * (b + a) + c * b
        c, d = c ** 2 + d ** 2, d * (2 * c + d)
        i = i >> 1
    return a + b

exp = []

start = time.time()
for i in sequence2:
    exponentiation_fib(i)
    end = time.time()
    exp.append(round(end - start, 8))
    
ologn_tbl = PrettyTable(sequence2)
ologn_tbl.add_row(exp)
ologn_tbl.add_autoindex('Nr.')
print('Exponentiation table')
print(ologn_tbl)

plt.figure(6)
plt.plot(sequence2, exp, color = 'pink')
plt.scatter(sequence2, exp, color = 'pink')
plt.title('Exponentiation method')
plt.xlabel('n-th fibonacci number')
plt.ylabel('Execution time in s')
plt.show()

