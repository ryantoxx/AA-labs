def spigot_pi(n):
    pi = []
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3

    while n > 0:
        if 4*q+r-t < m*t:
            pi.append(m)
            n -= 1
            q, r, t, k, m, x = (
                10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t-10*m, x)
        else:
            q, r, t, k, m, x = (
                q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)

    return ''.join(map(str, pi))
