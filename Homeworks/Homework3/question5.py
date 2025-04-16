import numpy as np

def lu_decomposition(A):
    """
    计算矩阵A的LU分解，返回下三角矩阵L和上三角矩阵U
    使得A = LU
    
    参数:
        A: 输入矩阵，numpy数组
        
    返回:
        L: 下三角矩阵
        U: 上三角矩阵
        steps: 记录每一步计算过程的列表
    """
    n = A.shape[0]  # 矩阵A的维度
    
    # 初始化L和U矩阵
    U = np.copy(A).astype(float)
    L = np.eye(n)  # L初始化为单位矩阵
    
    # 用于记录计算过程的列表
    steps = []
    steps.append({"step": "初始化", "L": np.copy(L), "U": np.copy(U)})
    
    # 执行高斯消元
    for k in range(n-1):
        for i in range(k+1, n):
            # 计算L中的元素
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            
            # 记录当前操作
            step_desc = f"计算L[{i+1},{k+1}] = U[{i+1},{k+1}]/U[{k+1},{k+1}] = {U[i, k]}/{U[k, k]} = {factor}"
            
            # 更新U中的行
            U[i, k:] = U[i, k:] - factor * U[k, k:]
            
            # 更新步骤说明
            step_desc += f", 消去U的第{i+1}行"
            steps.append({
                "step": step_desc,
                "L": np.copy(L),
                "U": np.copy(U)
            })
    
    return L, U, steps

def print_matrix(matrix, name, precision=4):
    """美观打印矩阵"""
    print(f"\n矩阵{name}:")
    rows, cols = matrix.shape
    for i in range(rows):
        print("[", end=" ")
        for j in range(cols):
            print(f"{matrix[i, j]:{precision+6}.{precision}f}", end=" ")
        print("]")

def main():
    # 题目中给定的矩阵
    A = np.array([
        [1, 1, 0, 3],
        [2, -1, 5, -2],
        [3, -3, 6, -17],
        [-3, 0, -19, -24]
    ])
    
    print("问题5：计算矩阵A的三角分解 A = LU")
    print("\n输入矩阵A:")
    print(A)
    
    # 计算LU分解
    L, U, steps = lu_decomposition(A)
    
    # 打印详细的计算过程
    print("\n============ 详细计算过程 ============")
    for idx, step in enumerate(steps):
        print(f"\n步骤 {idx}：{step['step']}")
        print_matrix(step['L'], "L", 4)
        print_matrix(step['U'], "U", 4)
        print("-" * 50)
    
    # 打印最终结果
    print("\n============ 最终结果 ============")
    print("\n下三角矩阵L:")
    print(np.round(L, 6))
    
    print("\n上三角矩阵U:")
    print(np.round(U, 6))
    
    # 验证A = LU
    print("\n验证A = L×U:")
    LU = np.dot(L, U)
    print(np.round(LU, 6))
    
    # 检查原始矩阵A与LU的差异
    error = np.max(np.abs(A - LU))
    print(f"\n验证误差（最大绝对值差）: {error}")
    
    if error < 1e-10:
        print("\n结论：成功验证 A = LU")

if __name__ == "__main__":
    main() 