def third_alg(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i] == True:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    primes = [i for i in range(2, n+1) if c[i]]
    return primes
