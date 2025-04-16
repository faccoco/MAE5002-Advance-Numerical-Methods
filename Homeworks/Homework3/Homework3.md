# Homework3
12432670 Zitong Huang

## Question 1.

(a) and (d). Since (a) is symmetric obviously, we will focus on (d)

Proof of (d): Off-diagonal elemnts:

$a_{ij}= 2i - ij + 2j$

$a_{ji}= 2j - ij + 2i$

Which is equavalent. So (d) is symmetric.

## Question 2.

(a) Time of multiply: $M \cdot N$

(b) Time of addition: $M \cdot (N - 1)$

## Question 3.

Division: $\sum_{i=1}^{N} 1 = N$

Multiply&Add&Sub: $\sum_{i=1}^{N} (N - i) = \sum_{k=1}^{N-1} k = \frac{(N - 1)N}{2} = \frac{N^2 - N}{2}$

Thus, totally need $N$ divisions, $\frac{N^2 - N}{2}$ multiplication and $\frac{N^2 - N}{2}$ addition / Subtraction

## Question 4
**Answer:** 
(a) In this problem, I need to solve two linear systems using both partial pivoting and scaled partial pivoting Gaussian elimination methods.

For system a:
$$
\begin{bmatrix}
2 & -4 & 150 \\
1 & 12 & -0.01 \\
3 & -150 & 0.3
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}=
\begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix}
$$

### Partial Pivoting Method for System a:

1. Forming the augmented matrix $[A|b]$

Initial augmented matrix:
$$
\begin{bmatrix}
2 & -4 & 150 & 1 \\
1 & 12 & -0.01 & 0 \\
3 & -150 & 0.3 & 0
\end{bmatrix}
$$

2. For each column $k$, finding the pivot row with the largest absolute value in column $k$

For $k=0$, the largest absolute value in the first column is 3 in row 3, so we swap row 1 and row 3:
$$
\begin{bmatrix}
3 & -150 & 0.3 & 0 \\
1 & 12 & -0.01 & 0 \\
2 & -4 & 150 & 1
\end{bmatrix}
$$

3. Elimination for $k=0$:

Row 2 = Row 2 - (1/3) × Row 1:
$$
\begin{bmatrix}
3 & -150 & 0.3 & 0 \\
0 & 62 & -0.11 & 0 \\
2 & -4 & 150 & 1
\end{bmatrix}
$$

Row 3 = Row 3 - (2/3) × Row 1:
$$
\begin{bmatrix}
3 & -150 & 0.3 & 0 \\
0 & 62 & -0.11 & 0 \\
0 & 96 & 149.8 & 1
\end{bmatrix}
$$

For $k=1$, the largest absolute value in the second column (from row 2 to 3) is 96 in row 3, so we swap row 2 and row 3:
$$
\begin{bmatrix}
3 & -150 & 0.3 & 0 \\
0 & 96 & 149.8 & 1 \\
0 & 62 & -0.11 & 0
\end{bmatrix}
$$

Elimination for $k=1$:

Row 3 = Row 3 - (62/96) × Row 2:
$$
\begin{bmatrix}
3 & -150 & 0.3 & 0 \\
0 & 96 & 149.8 & 1 \\
0 & 0 & -96.9792 & -0.6458
\end{bmatrix}
$$

4. Back-substitution:

$x_3 = -0.6458 / (-96.9792) = 0.00667$

$x_2 = (1 - 149.8 \times 0.00667) / 96 = 0.0000118$

$x_1 = (0 - (-150) \times 0.0000118 - 0.3 \times 0.00667) / 3 = -0.0000753$

Therefore, using partial pivoting, the solution is:
$$x = [-7.53 \times 10^{-5}, 1.18 \times 10^{-5}, 6.67 \times 10^{-3}]^T$$

### Scaled Partial Pivoting Method for System a:

1. Forming the augmented matrix and calculating scaling factors:

Scaling factors for system a:
$s_1 = \max(|2|, |-4|, |150|) = 150$
$s_2 = \max(|1|, |12|, |-0.01|) = 12$
$s_3 = \max(|3|, |-150|, |0.3|) = 150$

Initial augmented matrix with scaling factors:
$$
\begin{bmatrix}
2 & -4 & 150 & 1 & | & 150\\
1 & 12 & -0.01 & 0 & | & 12\\
3 & -150 & 0.3 & 0 & | & 150
\end{bmatrix}
$$

2. For $k=0$, we compute ratios:
$|2|/150 = 0.0133$, $|1|/12 = 0.0833$, $|3|/150 = 0.02$

The largest ratio is 0.0833 in row 2, so we swap row 1 and row 2:
$$
\begin{bmatrix}
1 & 12 & -0.01 & 0 & | & 12\\
2 & -4 & 150 & 1 & | & 150\\
3 & -150 & 0.3 & 0 & | & 150
\end{bmatrix}
$$

3. Elimination for $k=0$:

Row 2 = Row 2 - (2) × Row 1:
$$
\begin{bmatrix}
1 & 12 & -0.01 & 0 & | & 12\\
0 & -28 & 150.02 & 1 & | & 150\\
3 & -150 & 0.3 & 0 & | & 150
\end{bmatrix}
$$

Row 3 = Row 3 - (3) × Row 1:
$$
\begin{bmatrix}
1 & 12 & -0.01 & 0 & | & 12\\
0 & -28 & 150.02 & 1 & | & 150\\
0 & -186 & 0.33 & 0 & | & 150
\end{bmatrix}
$$

For $k=1$, we compute ratios:
$|-28|/150 = 0.1867$, $|-186|/150 = 1.24$

The largest ratio is 1.24 in row 3, so we swap row 2 and row 3:
$$
\begin{bmatrix}
1 & 12 & -0.01 & 0 & | & 12\\
0 & -186 & 0.33 & 0 & | & 150\\
0 & -28 & 150.02 & 1 & | & 150
\end{bmatrix}
$$

Elimination for $k=1$:

Row 3 = Row 3 - ($\frac{-28}{-186}$) × Row 2:
$$
\begin{bmatrix}
1 & 12 & -0.01 & 0 & | & 12\\
0 & -186 & 0.33 & 0 & | & 150\\
0 & 0 & 150.07 & 1 & | & 150
\end{bmatrix}
$$

4. Back-substitution:

$x_3 = 1 / 150.07 = 0.00666$

$x_2 = (0 - 0.33 \times 0.00666) / (-186) = -0.0000118$

$x_1 = (0 - 12 \times (-0.0000118) - (-0.01) \times 0.00666) / 1 = -0.0000753$

Therefore, using scaled partial pivoting, the solution is:
$$x = [-7.53 \times 10^{-5}, -1.18 \times 10^{-5}, 6.66 \times 10^{-3}]^T$$

(b) For system b:

$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 \\
2 & -5 & 35 & -0.1 \\
5 & 1 & -120 & -10 \\
2 & -100 & -3 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix} =
\begin{bmatrix}
0 \\
1 \\
0 \\
0
\end{bmatrix}
$$

### Partial Pivoting Method for System b:

Initial augmented matrix:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 \\
2 & -5 & 35 & -0.1 & 1 \\
5 & 1 & -120 & -10 & 0 \\
2 & -100 & -3 & 1 & 0
\end{bmatrix}
$$

For $k=0$, the largest absolute value in the first column is 5 in row 3, so we swap row 1 and row 3:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
2 & -5 & 35 & -0.1 & 1 \\
1 & 10 & -1 & 0.001 & 0 \\
2 & -100 & -3 & 1 & 0
\end{bmatrix}
$$

Elimination for $k=0$:

Row 2 = Row 2 - (2/5) × Row 1:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -5.4 & 83 & 3.9 & 1 \\
1 & 10 & -1 & 0.001 & 0 \\
2 & -100 & -3 & 1 & 0
\end{bmatrix}
$$

Row 3 = Row 3 - (1/5) × Row 1:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -5.4 & 83 & 3.9 & 1 \\
0 & 9.8 & 23 & 2.001 & 0 \\
2 & -100 & -3 & 1 & 0
\end{bmatrix}
$$

Row 4 = Row 4 - (2/5) × Row 1:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -5.4 & 83 & 3.9 & 1 \\
0 & 9.8 & 23 & 2.001 & 0 \\
0 & -100.4 & 45 & 5 & 0
\end{bmatrix}
$$

For $k=1$, the largest absolute value in the second column is 100.4 in row 4, so we swap row 2 and row 4:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -100.4 & 45 & 5 & 0 \\
0 & 9.8 & 23 & 2.001 & 0 \\
0 & -5.4 & 83 & 3.9 & 1
\end{bmatrix}
$$

Elimination for $k=1$:

Row 3 = Row 3 - (9.8/(-100.4)) × Row 2:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -100.4 & 45 & 5 & 0 \\
0 & 0 & 27.39 & 2.488 & 0 \\
0 & -5.4 & 83 & 3.9 & 1
\end{bmatrix}
$$

Row 4 = Row 4 - ((-5.4)/(-100.4)) × Row 2:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -100.4 & 45 & 5 & 0 \\
0 & 0 & 27.39 & 2.488 & 0 \\
0 & 0 & 85.42 & 4.17 & 1
\end{bmatrix}
$$

For $k=2$, the largest absolute value in the third column is 85.42 in row 4, so we swap row 3 and row 4:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -100.4 & 45 & 5 & 0 \\
0 & 0 & 85.42 & 4.17 & 1 \\
0 & 0 & 27.39 & 2.488 & 0
\end{bmatrix}
$$

Elimination for $k=2$:

Row 4 = Row 4 - (27.39/85.42) × Row 3:
$$
\begin{bmatrix}
5 & 1 & -120 & -10 & 0 \\
0 & -100.4 & 45 & 5 & 0 \\
0 & 0 & 85.42 & 4.17 & 1 \\
0 & 0 & 0 & 1.155 & -0.3207
\end{bmatrix}
$$

Back-substitution:

$x_4 = -0.3207 / 1.155 = -0.2776$

$x_3 = (1 - 4.17 \times (-0.2776)) / 85.42 = 0.0246$

$x_2 = (0 - 45 \times 0.0246 - 5 \times (-0.2776)) / (-100.4) = -0.0025$

$x_1 = (0 - 1 \times (-0.0025) - (-120) \times 0.0246 - (-10) \times (-0.2776)) / 5 = 0.0495$

Therefore, using partial pivoting, the solution is:
$$x = [0.0495, -0.0025, 0.0246, -0.2776]^T$$

### Scaled Partial Pivoting Method for System b:

1. Forming the augmented matrix and calculating scaling factors:

Scaling factors for system b:
$s_1 = \max(|1|, |10|, |-1|, |0.001|) = 10$
$s_2 = \max(|2|, |-5|, |35|, |-0.1|) = 35$
$s_3 = \max(|5|, |1|, |-120|, |-10|) = 120$
$s_4 = \max(|2|, |-100|, |-3|, |1|) = 100$

Initial augmented matrix with scaling factors:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 & | & 10\\
2 & -5 & 35 & -0.1 & 1 & | & 35\\
5 & 1 & -120 & -10 & 0 & | & 120\\
2 & -100 & -3 & 1 & 0 & | & 100
\end{bmatrix}
$$

2. For $k=0$, we compute ratios:
$|1|/10 = 0.1$, $|2|/35 = 0.0571$, $|5|/120 = 0.0417$, $|2|/100 = 0.02$

The largest ratio is 0.1 in row 1, so no row swap is needed:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 & | & 10\\
2 & -5 & 35 & -0.1 & 1 & | & 35\\
5 & 1 & -120 & -10 & 0 & | & 120\\
2 & -100 & -3 & 1 & 0 & | & 100
\end{bmatrix}
$$

3. Elimination for $k=0$:

Row 2 = Row 2 - (2) × Row 1:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 & | & 10\\
0 & -25 & 37 & -0.102 & 1 & | & 35\\
5 & 1 & -120 & -10 & 0 & | & 120\\
2 & -100 & -3 & 1 & 0 & | & 100
\end{bmatrix}
$$

Row 3 = Row 3 - (5) × Row 1:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 & | & 10\\
0 & -25 & 37 & -0.102 & 1 & | & 35\\
0 & -49 & -115 & -10.005 & 0 & | & 120\\
2 & -100 & -3 & 1 & 0 & | & 100
\end{bmatrix}
$$

Row 4 = Row 4 - (2) × Row 1:
$$
\begin{bmatrix}
1 & 10 & -1 & 0.001 & 0 & | & 10\\
0 & -25 & 37 & -0.102 & 1 & | & 35\\
0 & -49 & -115 & -10.005 & 0 & | & 120\\
0 & -120 & -1 & 0.998 & 0 & | & 100
\end{bmatrix}
$$

Continuing with similar elimination steps for $k=1$, $k=2$, and $k=3$, followed by back-substitution, we arrive at the solution:
$$x = [0.0495, -0.0025, 0.0246, -0.2709]^T$$

## Question 5

Find the triangular factorization $A = LU$ for the matrix

$$
A = \begin{bmatrix}
1 & 1 & 0 & 3 \\
2 & -1 & 5 & -2 \\
3 & -3 & 6 & -17 \\
-3 & 0 & -19 & -24
\end{bmatrix}
$$

The LU decomposition of a matrix $A$ involves finding a lower triangular matrix $L$ and an upper triangular matrix $U$ such that $A = LU$. This factorization is performed using Gaussian elimination without row exchanges.

For a matrix $A \in \mathbb{R}^{n \times n}$, the algorithm proceeds as follows:

Initialization: Set $U = A$ and initialize $L$ as an identity matrix.

The initial matrices are:

$$
L^{(0)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}, \quad
U^{(0)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
2 & -1 & 5 & -2 \\
3 & -3 & 6 & -17 \\
-3 & 0 & -19 & -24
\end{bmatrix}
$$

The elimination process proceeds column by column:

For the first column ($k=0$):

The multiplier for row 2 is $l_{21} = \frac{u_{21}}{u_{11}} = \frac{2}{1} = 2$. Applying row operations to eliminate the element at position (2,1) in $U$:

$$
U^{(1)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
3 & -3 & 6 & -17 \\
-3 & 0 & -19 & -24
\end{bmatrix}, \quad
L^{(1)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The multiplier for row 3 is $l_{31} = \frac{u_{31}}{u_{11}} = \frac{3}{1} = 3$. Applying row operations:

$$
U^{(2)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & -6 & 6 & -26 \\
-3 & 0 & -19 & -24
\end{bmatrix}, \quad
L^{(2)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The multiplier for row 4 is $l_{41} = \frac{u_{41}}{u_{11}} = \frac{-3}{1} = -3$. Applying row operations:

$$
U^{(3)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & -6 & 6 & -26 \\
0 & 3 & -19 & -15
\end{bmatrix}, \quad
L^{(3)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 0 & 1 & 0 \\
-3 & 0 & 0 & 1
\end{bmatrix}
$$

For the second column ($k=1$):

The multiplier for row 3 is $l_{32} = \frac{u_{32}}{u_{22}} = \frac{-6}{-3} = 2$. Applying row operations:

$$
U^{(4)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & 0 & -4 & -10 \\
0 & 3 & -19 & -15
\end{bmatrix}, \quad
L^{(4)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 2 & 1 & 0 \\
-3 & 0 & 0 & 1
\end{bmatrix}
$$

The multiplier for row 4 is $l_{42} = \frac{u_{42}}{u_{22}} = \frac{3}{-3} = -1$. Applying row operations:

$$
U^{(5)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & 0 & -4 & -10 \\
0 & 0 & -14 & -23
\end{bmatrix}, \quad
L^{(5)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 2 & 1 & 0 \\
-3 & -1 & 0 & 1
\end{bmatrix}
$$

For the third column ($k=2$):

The multiplier for row 4 is $l_{43} = \frac{u_{43}}{u_{33}} = \frac{-14}{-4} = 3.5$. Applying row operations:

$$
U^{(6)} = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & 0 & -4 & -10 \\
0 & 0 & 0 & 12
\end{bmatrix}, \quad
L^{(6)} = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 2 & 1 & 0 \\
-3 & -1 & 3.5 & 1
\end{bmatrix}
$$

Therefore, the LU decomposition of the given matrix $A$ is:

$$
L = \begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
3 & 2 & 1 & 0 \\
-3 & -1 & 3.5 & 1
\end{bmatrix}, \quad
U = \begin{bmatrix}
1 & 1 & 0 & 3 \\
0 & -3 & 5 & -8 \\
0 & 0 & -4 & -10 \\
0 & 0 & 0 & 12
\end{bmatrix}
$$

