def first_alg(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i] == True:
            j = 2*i
            while j <= n:
                c[j] = False
                j += i
        i += 1

    primes = [i for i in range(2, n+1) if c[i]]
    return primes




