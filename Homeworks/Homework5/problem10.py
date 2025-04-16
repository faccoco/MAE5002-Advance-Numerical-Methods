import numpy as np

t = np.array([0, 2, 4, 6, 8], dtype=float)
d = np.array([0, 40, 160, 300, 480], dtype=float)
n = len(t) - 1

h = np.diff(t) 

A = np.zeros((n+1, n+1))
alpha = np.zeros(n+1)

A[0, 0] = 2 * h[0]
A[0, 1] = h[0]
alpha[0] = 3 * ((d[1] - d[0]) / h[0] - 0)  # f'(0) = 0

A[n, n-1] = h[-1]
A[n, n] = 2 * h[-1]
alpha[n] = 3 * (98 - (d[n] - d[n-1]) / h[-1])  # f'(8) = 98

for i in range(1, n):
    A[i, i-1] = h[i-1]
    A[i, i]   = 2 * (h[i-1] + h[i])
    A[i, i+1] = h[i]
    alpha[i] = 3 * ((d[i+1] - d[i]) / h[i] - (d[i] - d[i-1]) / h[i-1])

# np.linalg.solve is for solving linear systems, presumably permitted？
c = np.linalg.solve(A, alpha)

a = d[:-1]
b = np.zeros(n)
d_coef = np.zeros(n)

for i in range(n):
    b[i] = (d[i+1] - d[i])/h[i] - h[i]*(2*c[i] + c[i+1])/3
    d_coef[i] = (c[i+1] - c[i]) / (3*h[i])

splines = []
for i in range(n):
    coeffs = (a[i], b[i], c[i], d_coef[i])
    splines.append(coeffs)

for i, (a_, b_, c_, d_) in enumerate(splines):
    print(f"S_{i}(t) = {a_:.2f} + {b_:.2f}(t-{t[i]}) + {c_:.2f}(t-{t[i]})^2 + {d_:.2f}(t-{t[i]})^3")