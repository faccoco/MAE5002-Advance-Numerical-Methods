import math

def diff_limit(f, x, h_init=1e-2, toler=5e-14, max_iter=50):
    eps = 1e-30
    H = []
    D = []
    # first value
    h = h_init
    H.append(h)
    D.append((f(x + h) - f(x - h)) / (2 * h))
    # second value
    h = h / 10.0
    H.append(h)
    D.append((f(x + h) - f(x - h)) / (2 * h))
    E_prev = abs(D[1] - D[0])
    R_prev = 2 * E_prev / (abs(D[1]) + abs(D[0]) + eps)
    best_D = D[1]
    best_H = H[1]
    for _ in range(2, max_iter):
        if R_prev < toler:
            break
        h = h / 10.0
        H.append(h)
        D_new = (f(x + h) - f(x - h)) / (2 * h)
        D.append(D_new)
        E_new = abs(D_new - D[-2])  # compare with previous
        R_new = 2 * E_new / (abs(D_new) + abs(D[-2]) + eps)
        # if error increased, stop
        if E_new >= E_prev:
            break
        # update best
        E_prev, R_prev = E_new, R_new
        best_D, best_H = D_new, h
    return best_D, best_H

# Function (a)
def f_a(x):
    return math.sin(math.cos(1.0 / x))

def f_a_prime_analytic(x):
    return math.cos(math.cos(1.0 / x)) * math.sin(1.0 / x) / (x ** 2)

x_a = 1.0 / math.sqrt(2.0)
d_a, h_a = diff_limit(f_a, x_a, h_init=1e-2, toler=5e-14, max_iter=50)
d_a_true = f_a_prime_analytic(x_a)
rel_err_a = abs(d_a - d_a_true) / abs(d_a_true)

# Function (b)
def f_b(x):
    return x ** x ** x  # x^(x^x)

def f_b_prime_analytic(x):
    return (x ** x) * (math.log(x) + 1.0)

x_b = 1e-4
d_b, h_b = diff_limit(f_b, x_b, h_init=1e-6, toler=5e-14, max_iter=50)
d_b_true = f_b_prime_analytic(x_b)
rel_err_b = abs(d_b - d_b_true) / abs(d_b_true)

results = [
    ["sin(cos(1/x))", x_a, d_a, d_a_true, rel_err_a, h_a],
    ["x^x^x", x_b, d_b, d_b_true, rel_err_b, h_b],
]

from tabulate import tabulate
print(tabulate(
    [[r[0], f"{r[1]:.10g}", f"{r[2]:.15g}", f"{r[3]:.15g}", f"{r[4]:.2e}", f"{r[5]:.1e}"] for r in results],
    headers=["f(x)", "x", "approx f'(x)", "analytic f'(x)", "rel. err.", "h_used"]
))