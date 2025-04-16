import numpy as np

def gaussian_elimination_partial_pivoting(A, b):
    """
    使用部分主元高斯消元法求解线性方程组 Ax = b
    参数:
        A: 系数矩阵
        b: 常数向量
    返回:
        x: 解向量
    """
    n = len(A)
    # 将A和b组合成增广矩阵
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)
    Ab = Ab.astype(float)  # 确保数据类型为float
    
    # 前向消元
    for k in range(n-1):
        # 部分主元选择
        pivot_row = k + np.argmax(abs(Ab[k:, k]))
        if pivot_row != k:
            Ab[k], Ab[pivot_row] = Ab[pivot_row].copy(), Ab[k].copy()
            
        for i in range(k+1, n):
            factor = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= factor * Ab[k, k:]
    
    # 回代
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]
    
    return x

def gaussian_elimination_scaled_partial_pivoting(A, b):
    """
    使用标度部分主元高斯消元法求解线性方程组 Ax = b
    参数:
        A: 系数矩阵
        b: 常数向量
    返回:
        x: 解向量
    """
    n = len(A)
    # 将A和b组合成增广矩阵
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)
    Ab = Ab.astype(float)
    
    # 计算每行的最大元素（标度因子）
    s = np.max(abs(A), axis=1)
    
    # 前向消元
    for k in range(n-1):
        # 标度部分主元选择
        ratios = abs(Ab[k:, k]) / s[k:]
        pivot_row = k + np.argmax(ratios)
        if pivot_row != k:
            Ab[k], Ab[pivot_row] = Ab[pivot_row].copy(), Ab[k].copy()
            s[k], s[pivot_row] = s[pivot_row], s[k]
            
        for i in range(k+1, n):
            factor = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= factor * Ab[k, k:]
    
    # 回代
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]
    
    return x

# 定义系统a的系数矩阵和常数向量
A_a = np.array([
    [2, -4, 150],
    [1, 12, -0.01],
    [3, -150, 0.3]
])

b_a = np.array([1, 0, 0])

# 使用两种方法求解系统a
print("系统a的解（使用部分主元高斯消元法）：")
x_a1 = gaussian_elimination_partial_pivoting(A_a, b_a)
print(np.round(x_a1, 8))  # 八位小数舍入

print("\n系统a的解（使用标度部分主元高斯消元法）：")
x_a2 = gaussian_elimination_scaled_partial_pivoting(A_a, b_a)
print(np.round(x_a2, 8))  # 八位小数舍入

# 定义系统b的系数矩阵和常数向量
A_b = np.array([
    [1, 10, -1, 0.001],
    [2, -5, 35, -0.1],
    [5, 1, -120, -10],
    [2, -100, -3, 1]
])

b_b = np.array([0, 1, 0, 0])

# 使用两种方法求解系统b
print("\n系统b的解（使用部分主元高斯消元法）：")
x_b1 = gaussian_elimination_partial_pivoting(A_b, b_b)
print(np.round(x_b1, 4))  # 四位小数舍入

print("\n系统b的解（使用标度部分主元高斯消元法）：")
x_b2 = gaussian_elimination_scaled_partial_pivoting(A_b, b_b)
print(np.round(x_b2, 4))  # 四位小数舍入
