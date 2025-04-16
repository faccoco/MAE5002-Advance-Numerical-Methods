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

To verify the decomposition, compute $LU$:

$$
LU = \begin{bmatrix}
1 & 1 & 0 & 3 \\
2 & -1 & 5 & -2 \\
3 & -3 & 6 & -17 \\
-3 & 0 & -19 & -24
\end{bmatrix} = A
$$

The maximum absolute error between the original matrix $A$ and the product $LU$ is 0.0, confirming that the decomposition is correct.

The LU decomposition is valuable for solving linear systems, computing determinants, and calculating matrix inverses efficiently. 