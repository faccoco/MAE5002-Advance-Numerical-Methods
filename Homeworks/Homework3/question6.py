import numpy as np
import matplotlib.pyplot as plt

def jacobi_iteration(A, b, x0, max_iterations=100, tol=1e-10):
    """
    实现Jacobi迭代法解线性方程组 Ax = b
    
    参数:
    A -- 系数矩阵
    b -- 右侧向量
    x0 -- 初始猜测
    max_iterations -- 最大迭代次数
    tol -- 收敛容差
    
    返回:
    x_history -- 迭代过程中的解向量历史
    """
    n = len(b)
    x = x0.copy()
    x_history = [x0.copy()]
    
    for k in range(max_iterations):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i, j] * x[j]
            x_new[i] = (b[i] - s) / A[i, i]
        
        x_history.append(x_new.copy())
        
        # 检查收敛性
        if np.linalg.norm(x_new - x) < tol:
            break
            
        x = x_new.copy()
    
    return np.array(x_history)

def gauss_seidel_iteration(A, b, x0, max_iterations=100, tol=1e-10):
    """
    实现Gauss-Seidel迭代法解线性方程组 Ax = b
    
    参数:
    A -- 系数矩阵
    b -- 右侧向量
    x0 -- 初始猜测
    max_iterations -- 最大迭代次数
    tol -- 收敛容差
    
    返回:
    x_history -- 迭代过程中的解向量历史
    """
    n = len(b)
    x = x0.copy()
    x_history = [x0.copy()]
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            s1 = sum(A[i, j] * x[j] for j in range(i))
            s2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i, i]
        
        x_history.append(x.copy())
        
        # 检查收敛性
        if np.linalg.norm(x - x_old) < tol:
            break
    
    return np.array(x_history)

def check_convergence(A):
    """检查迭代方法是否收敛"""
    # 对角占优检查
    diag_dominant = True
    for i in range(len(A)):
        if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(len(A)) if j != i):
            diag_dominant = False
            break
    
    # 计算谱半径
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    # Jacobi迭代矩阵
    Bj = -np.linalg.inv(D) @ (L + U)
    # Gauss-Seidel迭代矩阵
    Bgs = -np.linalg.inv(D + L) @ U
    
    # 计算谱半径
    eigenvalues_j = np.linalg.eigvals(Bj)
    eigenvalues_gs = np.linalg.eigvals(Bgs)
    spectral_radius_j = max(abs(eigenvalues_j))
    spectral_radius_gs = max(abs(eigenvalues_gs))
    
    return {
        "diag_dominant": diag_dominant,
        "spectral_radius_jacobi": spectral_radius_j,
        "spectral_radius_gauss_seidel": spectral_radius_gs,
        "jacobi_converges": spectral_radius_j < 1,
        "gauss_seidel_converges": spectral_radius_gs < 1
    }

def plot_convergence(jacobi_history, gauss_seidel_history, exact_solution):
    """绘制收敛历史图"""
    # 计算每次迭代的误差
    jacobi_errors = np.linalg.norm(jacobi_history - exact_solution, axis=1)
    gs_errors = np.linalg.norm(gauss_seidel_history - exact_solution, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(jacobi_errors, 'bo-', label='Jacobi Method')
    plt.semilogy(gs_errors, 'ro-', label='Gauss-Seidel Method')
    plt.xlabel('Iteration Number')
    plt.ylabel('Error Norm (Log Scale)')
    plt.title('Convergence Comparison of Jacobi and Gauss-Seidel Methods')
    plt.legend()
    plt.grid(True)
    plt.savefig('convergence_plot.png')
    plt.close()

def main():
    # 定义问题
    A = np.array([
        [1, -5, -1],
        [4, 1, -1],
        [2, -1, -6]
    ])
    
    b = np.array([-8, 13, -2])
    x0 = np.zeros(3)  # 初始猜测 P0 = 0
    
    # 计算精确解作为参考
    exact_solution = np.linalg.solve(A, b)
    print(f"精确解: {exact_solution}")
    
    # 检查收敛性
    conv_info = check_convergence(A)
    print("\n收敛性分析:")
    print(f"矩阵是否对角占优: {conv_info['diag_dominant']}")
    print(f"Jacobi迭代谱半径: {conv_info['spectral_radius_jacobi']:.6f}")
    print(f"Gauss-Seidel迭代谱半径: {conv_info['spectral_radius_gauss_seidel']:.6f}")
    print(f"Jacobi迭代是否收敛: {conv_info['jacobi_converges']}")
    print(f"Gauss-Seidel迭代是否收敛: {conv_info['gauss_seidel_converges']}")
    
    # 执行Jacobi迭代
    jacobi_history = jacobi_iteration(A, b, x0)
    print("\nJacobi迭代:")
    for k in range(min(4, len(jacobi_history))):
        print(f"P{k} = {jacobi_history[k]}")
    
    # 执行Gauss-Seidel迭代
    gauss_seidel_history = gauss_seidel_iteration(A, b, x0)
    print("\nGauss-Seidel迭代:")
    for k in range(min(4, len(gauss_seidel_history))):
        print(f"P{k} = {gauss_seidel_history[k]}")
    
    # 绘制收敛历史
    plot_convergence(jacobi_history, gauss_seidel_history, exact_solution)
    
    print("\n结论:")
    print(f"Jacobi迭代{'收敛' if conv_info['jacobi_converges'] else '不收敛'}")
    print(f"Gauss-Seidel迭代{'收敛' if conv_info['gauss_seidel_converges'] else '不收敛'}")

if __name__ == "__main__":
    main()
