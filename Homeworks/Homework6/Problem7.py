import math

def f(x):
    # Function: x^(x^x)
    return x ** (x ** x)

def f_1(x):
    return math.sin(math.cos(1.0 / x))

def diff4(f, x, h0=1.0, max_iter=15, tol=5e-14):
    """Fourth‑order central difference with adaptive step."""
    h = h0
    D_prev = (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)
    H = [h]
    D = [D_prev]
    E = [float('inf')]  # first error undefined
    for _ in range(max_iter):
        h /= 10
        D_new = (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)
        err = abs(D_new - D_prev)
        H.append(h)
        D.append(D_new)
        E.append(err)
        # stop if improvement stalls or reached desired tol
        if err > E[-2] or err < tol:
            break
        D_prev = D_new
    # best index = error minimum (skip first inf)
    best_idx = E[1:].index(min(E[1:])) + 1
    return H, D, E, best_idx

# Compute derivative at x = 1
x0 = 1.0
H, D, E, n_best = diff4(f, x0)

best_derivative = D[n_best]
best_h = H[n_best]

print(best_derivative, best_h)

# Compute derivative at x = 1
x0 = 1.0
H, D, E, n_best = diff4(f_1, x0)

