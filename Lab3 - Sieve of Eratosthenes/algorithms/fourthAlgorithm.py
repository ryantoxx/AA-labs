def fourth_alg(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
                break
            j += 1
        i += 1
    primes = [i for i in range(len(c)) if c[i]]
    return primes


