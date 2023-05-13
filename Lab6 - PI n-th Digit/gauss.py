from decimal import *

def gauss_algorithm(n):
    # Returns the nth decimal digit of Pi using the Gauss-Legendre algorithm.
    if n < 0:
        raise ValueError("Invalid value of n.")

    getcontext().prec = n + 1  # Set the precision to n+1 decimal places

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(n):
        atmp = (a + b) / Decimal(2)
        b = (a * b).sqrt()
        t -= p * (a - atmp) ** Decimal(2)
        a = atmp
        p *= Decimal(2)

    pi = (a + b) ** Decimal(2) / (Decimal(4) * t)

    return int(str(pi)[n])

