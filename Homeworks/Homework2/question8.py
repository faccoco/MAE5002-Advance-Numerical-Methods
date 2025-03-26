import numpy as np
import matplotlib.pyplot as plt

def y_position(t):
    return 9500 * (1 - np.exp(-t/14)) - 470 * t

def x_position(t):
    return 2500 * (1 - np.exp(-t/14))

def bisection_method(f, a, b, tol=1e-15, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("区间端点的函数值必须异号")
    
    iterations = 0
    while (b - a) > tol and iterations < max_iter:
        c = (a + b) / 2
        
        if f(c) == 0:
            return c, iterations
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        iterations += 1
    
    return (a + b) / 2, iterations

a = 10
b = 100

while y_position(a) * y_position(b) >= 0:
    if y_position(a) > 0 and y_position(b) > 0:
        b *= 2
    elif y_position(a) < 0 and y_position(b) < 0:
        a /= 2
    else:
        if y_position(a) == 0:
            impact_time = a
            break
        if y_position(b) == 0:
            impact_time = b
            break

impact_time, iterations = bisection_method(y_position, a, b)
print(f"(a) 撞击时间 = {impact_time:.10f} 秒 (经过 {iterations} 次迭代)")

range_value = x_position(impact_time)
print(f"(b) 射程 = {range_value:.10f} 米")

t_values = np.linspace(0, impact_time, 1000)
x_values = [x_position(t) for t in t_values]
y_values = [y_position(t) for t in t_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values)
plt.grid(True)
plt.xlabel('x 位置 (米)')
plt.ylabel('y 位置 (米)')
plt.title('抛射体轨迹')
plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='r', linestyle='-', alpha=0.3)
plt.scatter([range_value], [0], color='red', s=100, label=f'撞击点 ({range_value:.2f}, 0)')
plt.legend()
plt.savefig('projectile_trajectory.png')
plt.show()
