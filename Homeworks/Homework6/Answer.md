# Homework 6

12432670

Zitong Huang

## Problem 1 Solution

### Part (a): $f(x,y) = x^2 + y^2 + 2xy$ at $(3,4)$

**1. Exact Partial Derivatives:**
* $f_x(x,y) = \frac{\partial}{\partial x}(x^2 + y^2 + 2xy)$
* $f_y(x,y) = \frac{\partial}{\partial y}(x^2 + y^2 + 2xy)$

* Exact $f_x(x, y) = 2*x + 2*y$, $f_x(3, 4)$ = 14.
* Exact $f_y(x, y) = 2*x + 2*y$, $f_y(3, 4)$ = 14

**2. Approximations using Formula (2):**

* **For $f_x(3,4)$:**
    * $f(x,y) = (x+y)^2$. At $(3,4)$, $f_x(3,4) \approx \frac{f(3+h, 4) - f(3-h, 4)}{2h} = \frac{(7+h)^2 - (7-h)^2}{2h}$
    * $h = 0.1$: $f_x(3,4) \approx 13.999999999999986$
    * $h = 0.01$: $f_x(3,4) \approx 13.999999999999702$
    * $h = 0.0001$: $f_x(3,4) \approx 13.999999999995794$

* **For $f_y(3,4)$:**
    * At $(3,4)$, $f_y(3,4) \approx \frac{f(3, 4+h) - f(3, 4-h)}{2h} = \frac{(7+h)^2 - (7-h)^2}{2h}$
    * $h = 0.1$: $f_y(3,4) \approx 13.999999999999986$
    * $h = 0.01$: $f_y(3,4) \approx 13.999999999999702$
    * $h = 0.0001$: $f_y(3,4) \approx 14.000000000002899$

**3. Comparison:**

For $f(x,y) = x^2 + y^2 + 2xy$ at $(3,4)$:
* The exact values are $f_x(3,4) = f_y(3,4) = 14$
* For $f_x(3,4)$:
    * $h = 0.1$: error ≈ 1.4e-14
    * $h = 0.01$: error ≈ 2.98e-13
    * $h = 0.0001$: error ≈ 4.206e-12
* For $f_y(3,4)$:
    * $h = 0.1$: error ≈ 1.4e-14
    * $h = 0.01$: error ≈ 2.98e-13
    * $h = 0.0001$: error ≈ 2.899e-12

### Part (b): $f(x,y) = \frac{x^2y^2}{x+y}$ at $(2,3)$

**1. Exact Partial Derivatives:**
* $f_x(x,y) = \frac{\partial}{\partial x}\left(\frac{x^2y^2}{x+y}\right)$
* $f_y(x,y) = \frac{\partial}{\partial y}\left(\frac{x^2y^2}{x+y}\right)$

* Exact $f_x(x, y) = -x^2*y^2/(x + y)^2 + 2*x*y^2/(x + y)$, $f_x(2, 3)$ = 5.76.
* Exact $f_y(x, y) = -x^2*y^2/(x + y)^2 + 2*x*y^2/(x + y)$, $f_y(2, 3)$ = 3.36

**2. Approximations using Formula (2):**

* **For $f_x(2,3)$:**
    * $f_x(2,3) \approx \frac{f(2+h, 3) - f(2-h, 3)}{2h}$
    * $h = 0.1$: $f_x(2,3) \approx 5.7587034813925575$
    * $h = 0.01$: $f_x(2,3) \approx 5.759987039948067$
    * $h = 0.0001$: $f_x(2,3) \approx 5.759999870400101$

* **For $f_y(2,3)$:**
    * $f_y(2,3) \approx \frac{f(2, 3+h) - f(2, 3-h)}{2h}$
    * $h = 0.1$: $f_y(2,3) \approx 3.3597438975590332$
    * $h = 0.01$: $f_y(2,3) \approx 3.3599974399896926$
    * $h = 0.0001$: $f_y(2,3) \approx 3.359999974400285$

**3. Comparison:**

For $f(x,y) = \frac{x^2y^2}{x+y}$ at $(2,3)$:
* The exact values are $f_x(2,3) = 5.76$ and $f_y(2,3) = 3.36$
* For $f_x(2,3)$:
    * $h = 0.1$: error ≈ 1.296e-3
    * $h = 0.01$: error ≈ 1.296e-5
    * $h = 0.0001$: error ≈ 1.296e-7
* For $f_y(2,3)$:
    * $h = 0.1$: error ≈ 2.56e-4
    * $h = 0.01$: error ≈ 2.56e-6
    * $h = 0.0001$: error ≈ 2.56e-8

Observations:
1. For the first function (simple polynomial), the numerical method achieves very high accuracy with errors in the range of 10^-12 to 10^-14.
2. For the second function (rational function), the errors are relatively larger, ranging from 10^-3 to 10^-8.
3. In both cases, accuracy generally improves as h decreases, but for the first function, there is a slight loss of precision when h becomes too small, likely due to rounding errors.
4. The second function shows significant improvement in accuracy as h decreases, indicating that choosing smaller step sizes is beneficial for such complex functions.

## Problem 2
Let $\epsilon = 5 \cdot 10^{-4}$ be the round-off error in $y_k$.
Given $|f^{(3)}(c)| \le M_3 = 1.5$ and $|f^{(5)}(c)| \le M_5 = 1.5$.
The best step size $h$ minimizes total error $E(h) \approx E_t(h) + E_r(h)$.

**(a) Formula: $f'(x_0) \approx \frac{y_1 - y_{-1}}{2h}$**

1.  **Truncation Error ($E_t$):**
    $E_t(h) \approx \frac{h^2}{6}M_3 = \frac{1.5}{6}h^2 = 0.25h^2$.

2.  **Round-off Error ($E_r$):**
    The error in $y_1 - y_{-1}$ is bounded by $2\epsilon$.
    $E_r(h) \approx \frac{2\epsilon}{2h} = \frac{\epsilon}{h} = \frac{5 \cdot 10^{-4}}{h}$.

3.  **Total Error & Minimization:**
    $E(h) = 0.25h^2 + \frac{5 \cdot 10^{-4}}{h}$.
    $\frac{dE}{dh} = 0.5h - \frac{5 \cdot 10^{-4}}{h^2} = 0$.
    $0.5h^3 = 5 \cdot 10^{-4} \Rightarrow h^3 = 10^{-3}$.
    $h = (10^{-3})^{1/3} = 0.1$.

**Best step size for (a): $h = 0.1$.**

**(b) Formula: $f'(x_0) \approx \frac{-y_2 + 8y_1 - 8y_{-1} + y_{-2}}{12h}$**

1.  **Truncation Error ($E_t$):**
    $E_t(h) \approx \frac{h^4}{30}M_5 = \frac{1.5}{30}h^4 = 0.05h^4$.

2.  **Round-off Error ($E_r$):**
    The error in the numerator $(-y_2 + 8y_1 - 8y_{-1} + y_{-2})$ is bounded by $(1+8+8+1)\epsilon = 18\epsilon$.
    $E_r(h) \approx \frac{18\epsilon}{12h} = \frac{3\epsilon}{2h} = \frac{3 \cdot (5 \cdot 10^{-4})}{2h} = \frac{7.5 \cdot 10^{-4}}{h}$.

3.  **Total Error & Minimization:**
    $E(h) = 0.05h^4 + \frac{7.5 \cdot 10^{-4}}{h}$.
    $\frac{dE}{dh} = 0.2h^3 - \frac{7.5 \cdot 10^{-4}}{h^2} = 0$.
    $0.2h^5 = 7.5 \cdot 10^{-4} \Rightarrow h^5 = \frac{7.5 \cdot 10^{-4}}{0.2} = 37.5 \cdot 10^{-4} = 3.75 \cdot 10^{-3}$.
    $h = (3.75 \cdot 10^{-3})^{1/5}$.

**Best step size for (b): $h = (0.00375)^{1/5} \approx 0.3268$.**

## Problem 3
Let $f(x) = \cos(x)$ and $x_0 = 1.2$. The approximation formula is $f'(x_0) \approx \frac{-y_2 + 8y_1 - 8y_{-1} + y_{-2}}{12h}$.
The inherent round-off error for $y_k = f(x_0+kh)$ is $|e_k| \le 5 \cdot 10^{-6}$.

**Part (a)**

1.  **Case 1: $h = 0.1$**
    * $y_2 = f(1.4) = 0.16997$
    * $y_1 = f(1.3) = 0.26750$
    * $y_{-1} = f(1.1) = 0.45360$
    * $y_{-2} = f(1.0) = 0.54030$
    * $f'(1.2) \approx \frac{-0.16997 + 8(0.26750) - 8(0.45360) + 0.54030}{12(0.1)}$
    * $f'(1.2) \approx \frac{-0.16997 + 2.14000 - 3.62880 + 0.54030}{1.2} = \frac{-1.11847}{1.2} \approx -0.932058$

2.  **Case 2: $h = 0.001$**
    * $y_2 = f(1.202) = 0.36049$
    * $y_1 = f(1.201) = 0.36143$
    * $y_{-1} = f(1.199) = 0.36329$
    * $y_{-2} = f(1.198) = 0.36422$
    * $f'(1.2) \approx \frac{-0.36049 + 8(0.36143) - 8(0.36329) + 0.36422}{12(0.001)}$
    * $f'(1.2) \approx \frac{-0.36049 + 2.89144 - 2.90632 + 0.36422}{0.012} = \frac{-0.01115}{0.012} \approx -0.929167$

**Part (b)**

The total error bound is $B(h) \approx |E_{round}(f,h)|_{max} + |E_{trunc}(f,h)|_{max}$.

1.  **$|E_{round}(f,h)|_{max}$:**
    The formula for the round-off error contribution is $E_{round}(f,h) = \frac{-e_2 + 8e_1 - 8e_{-1} + e_{-2}}{12h}$.
    $|E_{round}(f,h)|_{max} \le \frac{|e_2| + 8|e_1| + 8|e_{-1}| + |e_{-2}|}{12h} \le \frac{(1+8+8+1) \cdot 5 \cdot 10^{-6}}{12h} = \frac{18 \cdot 5 \cdot 10^{-6}}{12h} = \frac{7.5 \cdot 10^{-6}}{h}$.

2.  **$|E_{trunc}(f,h)|_{max}$:**
    The formula for the truncation error is $E_{trunc}(f,h) = \frac{h^4 f^{(5)}(c)}{30}$.
    $f(x) = \cos(x)$, so $f^{(5)}(x) = -\sin(x)$. Thus, $|f^{(5)}(c)| = |-\sin(c)| \le 1$.
    $|E_{trunc}(f,h)|_{max} \le \frac{h^4 \cdot 1}{30} = \frac{h^4}{30}$.

3.  **Total Error Bound Calculation:**

    * **For $h=0.1$:**
        * $|E_{round}(f,0.1)|_{max} \le \frac{7.5 \cdot 10^{-6}}{0.1} = 7.5 \cdot 10^{-5}$
        * $|E_{trunc}(f,0.1)|_{max} \le \frac{(0.1)^4}{30} = \frac{10^{-4}}{30} \approx 0.03333 \cdot 10^{-4} = 3.333 \cdot 10^{-6}$
        * Total Error Bound $B(0.1) \le 7.5 \cdot 10^{-5} + 3.333 \cdot 10^{-6} = 75 \cdot 10^{-6} + 3.333 \cdot 10^{-6} = 78.333 \cdot 10^{-6} \approx 7.83 \cdot 10^{-5}$

    * **For $h=0.001$:**
        * $|E_{round}(f,0.001)|_{max} \le \frac{7.5 \cdot 10^{-6}}{0.001} = 7.5 \cdot 10^{-3}$
        * $|E_{trunc}(f,0.001)|_{max} \le \frac{(0.001)^4}{30} = \frac{10^{-12}}{30} \approx 3.333 \cdot 10^{-14}$
        * Total Error Bound $B(0.001) \le 7.5 \cdot 10^{-3} + 3.333 \cdot 10^{-14} \approx 7.5 \cdot 10^{-3}$

Thus:
* For $h=0.1$: $f'(1.2) \approx -0.932058$; Total Error Bound $\approx 7.83 \cdot 10^{-5}$.
* For $h=0.001$: $f'(1.2) \approx -0.929167$; Total Error Bound $\approx 7.5 \cdot 10^{-3}$.

## Problem 4

**True Value:**
For $f(x) = \ln(x)$:
$f'(x) = \frac{1}{x}$
$f''(x) = -\frac{1}{x^2}$
So, $f''(5) = -\frac{1}{5^2} = -\frac{1}{25} = -0.04$.

**Given data values from the table for $x_0 = 5$:**
$f(4.90) = 1.5892$
$f(4.95) = 1.5994$
$f(5.00) = 1.6094$ (this is $f_0$ or $f(x_0)$)
$f(5.05) = 1.6194$
$f(5.10) = 1.6292$

**(a) Using formula (3) with $h = 0.05$:**
Formula (3): $$f''(x_0) \approx \frac{f(x_0+h) - 2f(x_0) + f(x_0-h)}{h^2}$$
Here, $x_0=5$ and $h=0.05$.
$f(x_0+h) = f(5.05) = 1.6194$
$f(x_0) = f(5.00) = 1.6094$
$f(x_0-h) = f(4.95) = 1.5994$
$h^2 = (0.05)^2 = 0.0025$
$$f''(5) \approx \frac{1.6194 - 2(1.6094) + 1.5994}{0.0025} = \frac{1.6194 - 3.2188 + 1.5994}{0.0025} = \frac{0.0000}{0.0025} = 0.0000$$

**(b) Using formula (3) with $h = 0.1$:**
Here, $x_0=5$ and $h=0.1$.
$f(x_0+h) = f(5.10) = 1.6292$
$f(x_0) = f(5.00) = 1.6094$
$f(x_0-h) = f(4.90) = 1.5892$
$h^2 = (0.1)^2 = 0.01$
$$f''(5) \approx \frac{1.6292 - 2(1.6094) + 1.5892}{0.01} = \frac{1.6292 - 3.2188 + 1.5892}{0.01} = \frac{-0.0004}{0.01} = -0.0400$$

**(c) Using formula (4) with $h = 0.05$:**
Formula (4): $$f''(x_0) \approx \frac{-f(x_0+2h) + 16f(x_0+h) - 30f(x_0) + 16f(x_0-h) - f(x_0-2h)}{12h^2}$$
Here, $x_0=5$ and $h=0.05$.
$f(x_0+2h) = f(5.10) = 1.6292$
$f(x_0+h) = f(5.05) = 1.6194$
$f(x_0) = f(5.00) = 1.6094$
$f(x_0-h) = f(4.95) = 1.5994$
$f(x_0-2h) = f(4.90) = 1.5892$
$12h^2 = 12(0.05)^2 = 12(0.0025) = 0.03$
Numerator:
$-1.6292 + 16(1.6194) - 30(1.6094) + 16(1.5994) - 1.5892$
$= -1.6292 + 25.9104 - 48.2820 + 25.5904 - 1.5892$
$= (25.9104 + 25.5904) - (1.6292 + 48.2820 + 1.5892)$
$= 51.5008 - 51.5004 = 0.0004$
$$f''(5) \approx \frac{0.0004}{0.03} = \frac{4}{300} = \frac{1}{75} \approx 0.0133$$

**(d) Comparation**
True value $f''(5) = -0.04$.
Comparing the approximations:
(a) Approximation = $0.0000$. Absolute error = $|0.0000 - (-0.04)| = 0.0400$.
(b) Approximation = $-0.0400$. Absolute error = $|-0.0400 - (-0.04)| = 0.0000$.
(c) Approximation $\approx 0.0133$. Absolute error = $|0.013333... - (-0.04)| = |0.053333...| \approx 0.0533$.

The approximation from **(b) is the most accurate**, as its absolute error is the smallest (in this case, $0$ due to the rounding of the provided table values).

## Problem 5

**(a) Central-difference formula for $f''(x) + f'(x)$ of order $O(h^2)$:**

Let $f'_c(x) = \frac{f(x+h) - f(x-h)}{2h}$ (which is $O(h^2)$) and $f''_c(x) = \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$ (which is $O(h^2)$).

Then, $f''(x) + f'(x) \approx f''_c(x) + f'_c(x) = \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} + \frac{f(x+h) - f(x-h)}{2h}$.
This simplifies to:
$f''(x) + f'(x) \approx \frac{2(f(x+h) - 2f(x) + f(x-h)) + h(f(x+h) - f(x-h))}{2h^2}$
$f''(x) + f'(x) \approx \frac{(2+h)f(x+h) - 4f(x) + (2-h)f(x-h)}{2h^2}$.
The order of this combined formula is $O(h^2)$.

**(b) Backward-difference formula for $f''(x) + f'(x)$ of order $O(h^2)$:**

Let $f'_b(x) = \frac{3f(x) - 4f(x-h) + f(x-2h)}{2h}$ (which is $O(h^2)$) and $f''_b(x) = \frac{2f(x) - 5f(x-h) + 4f(x-2h) - f(x-3h)}{h^2}$ (which is $O(h^2)$).

Then, $f''(x) + f'(x) \approx f''_b(x) + f'_b(x) = \frac{2f(x) - 5f(x-h) + 4f(x-2h) - f(x-3h)}{h^2} + \frac{3f(x) - 4f(x-h) + f(x-2h)}{2h}$.
This simplifies to:
$f''(x) + f'(x) \approx \frac{2(2f(x) - 5f(x-h) + 4f(x-2h) - f(x-3h)) + h(3f(x) - 4f(x-h) + f(x-2h))}{2h^2}$
$f''(x) + f'(x) \approx \frac{(4+3h)f(x) - (10+4h)f(x-h) + (8+h)f(x-2h) - 2f(x-3h)}{2h^2}$.
The order of this combined formula is $O(h^2)$.

**(c) What would happen if a formula for $f'(x)$ of order $O(h^4)$ were added to a formula for $f''(x)$ of order $O(h^2)$?**

If a formula for $f'(x)$ with error $E_1 = C_1h^4 + \dots$ (order $O(h^4)$) is added to a formula for $f''(x)$ with error $E_2 = C_2h^2 + \dots$ (order $O(h^2)$), the total error is $E_{total} = E_1 + E_2 = C_2h^2 + C_1h^4 + \dots$.
The dominant term in the error for small $h$ is $C_2h^2$.
Therefore, the resulting formula would have an order of accuracy of $O(h^2)$.

## Problem 6

![image-20250511235405445](/home/huangzitong/.config/Typora/typora-user-images/image-20250511235405445.png)

## Problem 7

![image-20250511235834140](/home/huangzitong/.config/Typora/typora-user-images/image-20250511235834140.png)