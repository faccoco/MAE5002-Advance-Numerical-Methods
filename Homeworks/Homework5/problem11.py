import numpy as np

def spline_cubic(x, y, mode='natural'):
    n = len(x) - 1
    h = np.diff(x)
    d = np.diff(y) / h

    A = h[1:]
    B = 2 * (h[:-1] + h[1:])
    C = h[:-1]
    U = 6 * (d[1:] - d[:-1])

    if mode == 'natural':
        B = np.concatenate(([1], B, [1]))
        U = np.concatenate(([0], U, [0]))
        A = np.concatenate(([0], A))
        C = np.concatenate((C, [0]))
    elif mode == 'extrapolated':
        dx0 = (y[1] - y[0]) / (x[1] - x[0])
        dxn = (y[-1] - y[-2]) / (x[-1] - x[-2])
        B = np.concatenate(([2 * h[0]], B, [2 * h[-1]]))
        U0 = 6 * (d[0] - dx0)
        UN = 6 * (dxn - d[-1])
        U = np.concatenate(([U0], U, [UN]))
        A = np.concatenate(([0], A))
        C = np.concatenate((C, [0]))
    elif mode == 'parabolic':
        B = np.concatenate(([1], B, [1]))
        U = np.concatenate(([U[0]], U, [U[-1]]))
        A = np.concatenate(([0], A))
        C = np.concatenate((C, [0]))
    elif mode == 'curvature':
        B = np.concatenate(([2], B, [2]))
        U0 = 6 * (d[1] - d[0])
        UN = 6 * (d[-1] - d[-2])
        U = np.concatenate(([U0], U, [UN]))
        A = np.concatenate(([0], A))
        C = np.concatenate((C, [0]))
    else:
        raise ValueError("Unsupported mode!")

    for k in range(1, n + 1):
        factor = A[k] / B[k - 1]
        B[k] = B[k] - factor * C[k - 1]
        U[k] = U[k] - factor * U[k - 1]

    M = np.zeros(n + 1)
    M[n] = U[n] / B[n]
    for k in range(n - 1, -1, -1):
        M[k] = (U[k] - C[k] * M[k + 1]) / B[k]

    # 计算每段的多项式系数
    coeffs = np.zeros((n, 4))
    for k in range(n):
        a = (M[k + 1] - M[k]) / (6 * h[k])
        b = M[k] / 2
        c = d[k] - h[k] * (2 * M[k] + M[k + 1]) / 6
        d_ = y[k]
        coeffs[k] = [a, b, c, d_]

    return coeffs

x = [0, 1, 2, 3, 4]
y = [0, 1, 0, 1, 0]

# 选择模式之一：'natural', 'extrapolated', 'parabolic', 'curvature'
S = spline_cubic(x, y, mode='natural')

print(S)