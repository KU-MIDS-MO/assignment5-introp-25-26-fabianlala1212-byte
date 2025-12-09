def approx_real_root(coeffs, interval):
    a = interval[0]
    b = interval[1]

    c0 = coeffs[0]
    c1 = coeffs[1]
    c2 = coeffs[2]
    c3 = coeffs[3]

    eps = 1e-9

    while (b - a) > eps:
        m = (a + b) / 2

        fa = c0 + c1*a + c2*a*a + c3*a*a*a
        fm = c0 + c1*m + c2*m*m + c3*m*m*m

        if fa * fm <= 0:
            b = m
        else:
            a = m

    return (a + b) / 2

coeffs = [1, -3, 0, 1]
interval = (0, 2)

print(approx_real_root(coeffs, interval))
