import math

def fifth_alg(n):
    c = [True] * (n+1)  
    c[1] = False        
    
    i = 2
    while i <= n:
        j = 2
        while j <= int(math.sqrt(i)):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    
    primes = []
    for i in range(2, n+1):
        if c[i]:
            primes.append(i)

    return primes
