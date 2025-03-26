
### Question 1: Mean Value Theorem for Integrals

Find the number(s) $c$ referred to in the Mean Value Theorem for Integrals for each function, over the interval indicated.

#### (a) $f(x) = \sqrt{x}$ over $[0, 4]$
$$
c = \frac{16}{9}
$$

#### (b) $f(x) = \frac{x^2}{x + 1}$ over $[0, 1]$
$$
c \approx 0.5466
$$

### Problem 2

#### (a) $\sum_{n=0}^{\infty} \left(\frac{1}{3}\right)^n$
This is a geometric series with the first term $a = 1$ (when $n=0$, $\left(\frac{1}{3}\right)^0 = 1$) and a common ratio $r = \frac{1}{3}$. The sum of an infinite geometric series $\sum_{n=0}^{\infty} ar^n$ (where $|r| < 1$) is given by $\frac{a}{1-r}$.

- $a = 1$, $r = \frac{1}{3}$
- Sum = $\frac{1}{1 - \frac{1}{3}} = \frac{1}{\frac{2}{3}} = \frac{3}{2}$

**Answer:** $\frac{3}{2}$

---

#### (b) $\sum_{n=1}^{\infty} \left(\frac{3}{4}\right)^n$
This is a geometric series starting at $n=1$, with the first term $a = \frac{3}{4}$ (when $n=1$) and a common ratio $r = \frac{3}{4}$. Since $|r| = \frac{3}{4} < 1$, the series converges, and the sum of $\sum_{n=1}^{\infty} r^n$ is $\frac{r}{1-r}$.

- $r = \frac{3}{4}$
- Sum = $\frac{\frac{3}{4}}{1 - \frac{3}{4}} = \frac{\frac{3}{4}}{\frac{1}{4}} = 3$

**Answer:** $3$

---

#### (c) $\sum_{n=2}^{\infty} \frac{4}{(n-1)(n+1)}$
This series involves a rational function. We use partial fraction decomposition to simplify the general term:
$$
\frac{4}{(n-1)(n+1)} = \frac{A}{n-1} + \frac{B}{n+1}
$$
Solving for $A$ and $B$:
$$
4 = A(n+1) + B(n-1)
$$
- Set $n = 1$: $4 = A(1+1) + B(1-1) = 2A$, so $A = 2$
- Set $n = -1$: $4 = A(-1+1) + B(-1-1) = -2B$, so $B = -2$

Thus:
$$
\frac{4}{(n-1)(n+1)} = \frac{2}{n-1} - \frac{2}{n+1}
$$
Now the series is:
$$
\sum_{n=2}^{\infty} \left(\frac{2}{n-1} - \frac{2}{n+1}\right) = 2 \sum_{n=2}^{\infty} \left(\frac{1}{n-1} - \frac{1}{n+1}\right)
$$
This is a telescoping series. Let’s write out the first few terms to identify the pattern:
- For $n=2$: $\frac{1}{1} - \frac{1}{3}$
- For $n=3$: $\frac{1}{2} - \frac{1}{4}$
- For $n=4$: $\frac{1}{3} - \frac{1}{5}$
- And so on...

The partial sum $S_N$ up to $N$ terms is:
$$
S_N = 2 \left[ \left(\frac{1}{1} - \frac{1}{3}\right) + \left(\frac{1}{2} - \frac{1}{4}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \cdots + \left(\frac{1}{N-1} - \frac{1}{N+1}\right) \right]
$$
Most terms cancel:
- $\frac{1}{1}$ remains.
- $\frac{1}{2}$ remains.
- The $-\frac{1}{3}$ from the first term cancels with $\frac{1}{3}$ from the third term, and this pattern continues.
- As $N \to \infty$, the remaining terms are $\frac{1}{N+1} \to 0$.

So:
$$
S_N = 2 \left[ 1 + \frac{1}{2} - \frac{1}{N+1} \right] = 2 \left[ \frac{3}{2} - \frac{1}{N+1} \right] = 3 - \frac{2}{N+1}
$$
As $N \to \infty$:
$$
\sum_{n=2}^{\infty} \frac{4}{(n-1)(n+1)} = 3
$$

**Answer:** $3$

---

#### (d) $\sum_{k=1}^{\infty} \frac{1}{4k^2 - 1}$
This series also involves a rational function. Let’s try partial fraction decomposition:
$$
\frac{1}{4k^2 - 1} = \frac{1}{(2k-1)(2k+1)} = \frac{A}{2k-1} + \frac{B}{2k+1}
$$
Solving for $A$ and $B$:
$$
1 = A(2k+1) + B(2k-1)
$$
- Set $2k-1 = 0$ (so $k = \frac{1}{2}$):
  $$
  1 = A(2 \cdot \frac{1}{2} + 1) + B(2 \cdot \frac{1}{2} - 1) = A(2) + B(0) \implies A = \frac{1}{2}
  $$
- Set $2k+1 = 0$ (so $k = -\frac{1}{2}$):
  $$
  1 = A(2 \cdot -\frac{1}{2} + 1) + B(2 \cdot -\frac{1}{2} - 1) = A(0) + B(-2) \implies B = -\frac{1}{2}
  $$
  Thus:
  $$
  \frac{1}{4k^2 - 1} = \frac{1/2}{2k-1} - \frac{1/2}{2k+1} = \frac{1}{2} \left( \frac{1}{2k-1} - \frac{1}{2k+1} \right)
  $$
  Now the series is:
  $$
  \sum_{k=1}^{\infty} \frac{1}{4k^2 - 1} = \frac{1}{2} \sum_{k=1}^{\infty} \left( \frac{1}{2k-1} - \frac{1}{2k+1} \right)
  $$
  This is another telescoping series. Let’s write out the first few terms:
- For $k=1$: $\frac{1}{1} - \frac{1}{3}$
- For $k=2$: $\frac{1}{3} - \frac{1}{5}$
- For $k=3$: $\frac{1}{5} - \frac{1}{7}$
- And so on...

The partial sum $S_N$ up to $N$ terms is:
$$
S_N = \frac{1}{2} \left[ \left(\frac{1}{1} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \left(\frac{1}{5} - \frac{1}{7}\right) + \cdots + \left(\frac{1}{2N-1} - \frac{1}{2N+1}\right) \right]
$$
Most terms cancel:
- $\frac{1}{1}$ remains.
- $-\frac{1}{3}$ from the first term cancels with $\frac{1}{3}$ from the second term, and this continues.
- As $N \to \infty$, the remaining terms $\frac{1}{2N+1} \to 0$.

The sum simplifies to:
$$
S_N = \frac{1}{2} \left[ 1 - \frac{1}{2N+1} \right]
$$
As $N \to \infty$:
$$
\sum_{k=1}^{\infty} \frac{1}{4k^2 - 1} = \frac{1}{2} \cdot 1 = \frac{1}{2}
$$

**Answer:** $\frac{1}{2}$

### Problem 3

### (a) $ 0.10111_{\text{two}} $

**Digits:**
- $ d_1 = 1 $
- $ d_2 = 0 $
- $ d_3 = 1 $
- $ d_4 = 1 $
- $ d_5 = 1 $

**Calculation:**
- $ 1 \times 2^{-1} = 1 \times \frac{1}{2} = 0.5 $
- $ 0 \times 2^{-2} = 0 \times \frac{1}{4} = 0 $
- $ 1 \times 2^{-3} = 1 \times \frac{1}{8} = 0.125 $
- $ 1 \times 2^{-4} = 1 \times \frac{1}{16} = 0.0625 $
- $ 1 \times 2^{-5} = 1 \times \frac{1}{32} = 0.03125 $

**Sum:**
$$
0.5 + 0 + 0.125 + 0.0625 + 0.03125 = 0.71875
$$

**Result:** $ 0.10111_{\text{two}} = 0.71875 $

---

### (b) $ 0.10101_{\text{two}} $

**Digits:**
- $ d_1 = 1 $
- $ d_2 = 0 $
- $ d_3 = 1 $
- $ d_4 = 0 $
- $ d_5 = 1 $

**Calculation:**
- $ 1 \times 2^{-1} = 0.5 $
- $ 0 \times 2^{-2} = 0 $
- $ 1 \times 2^{-3} = 0.125 $
- $ 0 \times 2^{-4} = 0 $
- $ 1 \times 2^{-5} = 0.03125 $

**Sum:**
$$
0.5 + 0 + 0.125 + 0 + 0.03125 = 0.65625
$$

**Result:** $ 0.10101_{\text{two}} = 0.65625 $

---

### (c) $ 0.10111101_{\text{two}} $

**Digits:**
- $ d_1 = 1 $
- $ d_2 = 0 $
- $ d_3 = 1 $
- $ d_4 = 1 $
- $ d_5 = 1 $
- $ d_6 = 1 $
- $ d_7 = 0 $
- $ d_8 = 1 $

**Calculation:**
- $ 1 \times 2^{-1} = 0.5 $
- $ 0 \times 2^{-2} = 0 $
- $ 1 \times 2^{-3} = 0.125 $
- $ 1 \times 2^{-4} = 0.0625 $
- $ 1 \times 2^{-5} = 0.03125 $
- $ 1 \times 2^{-6} = 1 \times \frac{1}{64} = 0.015625 $
- $ 0 \times 2^{-7} = 0 $
- $ 1 \times 2^{-8} = 1 \times \frac{1}{256} = 0.00390625 $

**Sum:**
$$
0.5 + 0 + 0.125 + 0.0625 + 0.03125 + 0.015625 + 0 + 0.00390625 = 0.73828125
$$

**Result:** $ 0.10111101_{\text{two}} = 0.73828125 $

---

### (d) $ 0.110110111_{\text{two}} $

**Digits:**
- $ d_1 = 1 $
- $ d_2 = 1 $
- $ d_3 = 0 $
- $ d_4 = 1 $
- $ d_5 = 1 $
- $ d_6 = 0 $
- $ d_7 = 1 $
- $ d_8 = 1 $
- $ d_9 = 1 $

**Calculation:**
- $ 1 \times 2^{-1} = 0.5 $
- $ 1 \times 2^{-2} = 0.25 $
- $ 0 \times 2^{-3} = 0 $
- $ 1 \times 2^{-4} = 0.0625 $
- $ 1 \times 2^{-5} = 0.03125 $
- $ 0 \times 2^{-6} = 0 $
- $ 1 \times 2^{-7} = 0.0078125 $
- $ 1 \times 2^{-8} = 0.00390625 $
- $ 1 \times 2^{-9} = 1 \times \frac{1}{512} = 0.001953125 $

**Sum:**
$$
0.5 + 0.25 + 0 + 0.0625 + 0.03125 + 0 + 0.0078125 + 0.00390625 + 0.001953125 = 0.857421875
$$

**Result:** $ 0.110110111_{\text{two}} = 0.857421875 $

---

### Final Answers

- (a) $ 0.10111_{\text{two}} = 0.71875 $
- (b) $ 0.10101_{\text{two}} = 0.65625 $
- (c) $ 0.10111101_{\text{two}} = 0.73828125 $
- (d) $ 0.110110111_{\text{two}} = 0.857421875 $

### Problem 4

### (a) 

Start with $ R = 1/3 $.

- **Step 1**: Compute $ 2R = 2 \times 1/3 = 2/3 $.  
  Since $ 2/3 < 1 $, the integer part is 0, so $ d_1 = 0 $.  
  Fractional part: $ F_1 = 2/3 $.

- **Step 2**: Compute $ 2F_1 = 2 \times 2/3 = 4/3 = 1 + 1/3 $.  
  Since $ 4/3 > 1 $, the integer part is 1, so $ d_2 = 1 $.  
  Fractional part: $ F_2 = 4/3 - 1 = 1/3 $.

- **Step 3**: Compute $ 2F_2 = 2 \times 1/3 = 2/3 $.  
  Since $ 2/3 < 1 $, $ d_3 = 0 $.  
  Fractional part: $ F_3 = 2/3 $, which matches $ F_1 $.

- **Step 4**: Compute $ 2F_3 = 2 \times 2/3 = 4/3 $.  
  $ d_4 = 1 $, $ F_4 = 1/3 $, which matches $ F_2 $.

At this point, the fractional parts repeat: $ F_1 = 2/3 $, $ F_2 = 1/3 $, $ F_3 = 2/3 $, $ F_4 = 1/3 $, and so on. Correspondingly, the digits repeat: $ d_1 = 0 $, $ d_2 = 1 $, $ d_3 = 0 $, $ d_4 = 1 $, etc. The binary representation is:

$$ 0.010101\ldots_2 $$

The repeating block is "01", so we denote it as:

$$ 1/3 = 0.\overline{01}_2 $$

---

### (b)

Start with $ R = 1/5 $.

- **Step 1**: $ 2R = 2 \times 1/5 = 2/5 $.  
  $ 2/5 < 1 $, so $ d_1 = 0 $, $ F_1 = 2/5 $.

- **Step 2**: $ 2F_1 = 2 \times 2/5 = 4/5 $.  
  $ 4/5 < 1 $, so $ d_2 = 0 $, $ F_2 = 4/5 $.

- **Step 3**: $ 2F_2 = 2 \times 4/5 = 8/5 = 1 + 3/5 $.  
  $ 8/5 > 1 $, so $ d_3 = 1 $, $ F_3 = 8/5 - 1 = 3/5 $.

- **Step 4**: $ 2F_3 = 2 \times 3/5 = 6/5 = 1 + 1/5 $.  
  $ 6/5 > 1 $, so $ d_4 = 1 $, $ F_4 = 6/5 - 1 = 1/5 $.

- **Step 5**: $ 2F_4 = 2 \times 1/5 = 2/5 $.  
  $ 2/5 < 1 $, so $ d_5 = 0 $, $ F_5 = 2/5 $, which matches $ F_1 $.

The fractional parts repeat: $ F_1 = 2/5 $, $ F_2 = 4/5 $, $ F_3 = 3/5 $, $ F_4 = 1/5 $, $ F_5 = 2/5 $, etc. The digits are: $ d_1 = 0 $, $ d_2 = 0 $, $ d_3 = 1 $, $ d_4 = 1 $, $ d_5 = 0 $, $ d_6 = 0 $, $ d_7 = 1 $, $ d_8 = 1 $, etc. The binary representation is:

$$ 0.00110011\ldots_2 $$

The repeating block is "0011", so:

$$ 1/5 = 0.\overline{0011}_2 $$

---

### (c) 

Start with $ R = 1/10 $.

- **Step 1**: $ 2R = 2 \times 1/10 = 1/5 $.  
  $ 1/5 < 1 $, so $ d_1 = 0 $, $ F_1 = 1/5 $.

- **Step 2**: $ 2F_1 = 2 \times 1/5 = 2/5 $.  
  $ 2/5 < 1 $, so $ d_2 = 0 $, $ F_2 = 2/5 $.

- **Step 3**: $ 2F_2 = 2 \times 2/5 = 4/5 $.  
  $ 4/5 < 1 $, so $ d_3 = 0 $, $ F_3 = 4/5 $.

- **Step 4**: $ 2F_3 = 2 \times 4/5 = 8/5 = 1 + 3/5 $.  
  $ 8/5 > 1 $, so $ d_4 = 1 $, $ F_4 = 8/5 - 1 = 3/5 $.

- **Step 5**: $ 2F_4 = 2 \times 3/5 = 6/5 = 1 + 1/5 $.  
  $ 6/5 > 1 $, so $ d_5 = 1 $, $ F_5 = 6/5 - 1 = 1/5 $, which matches $ F_1 $.

The fractional parts repeat: $ F_1 = 1/5 $, $ F_2 = 2/5 $, $ F_3 = 4/5 $, $ F_4 = 3/5 $, $ F_5 = 1/5 $, etc. The digits are: $ d_1 = 0 $, $ d_2 = 0 $, $ d_3 = 0 $, $ d_4 = 1 $, $ d_5 = 1 $, $ d_6 = 0 $, $ d_7 = 0 $, $ d_8 = 1 $, $ d_9 = 1 $, etc. The binary representation is:

$$ 0.0001100110011\ldots_2 $$

After the first three zeros, the pattern "1100" repeats: digits 4–7 are "1100", digits 8–11 are "1100", and so on. Thus:

$$ 1/10 = 0.000\overline{1100}_2 $$



Final answer is:

- (a) $ \frac{1}{3} = 0.\overline{01}_2 $  
- (b) $ \frac{1}{5} = 0.\overline{0011}_2 $  
- (c) $ \frac{1}{10} = 0.000\overline{1100}_2 $

### Problem 5


Base Case: $ N = 1 $

For $ N = 1 $, we have:

$$
2^{-1} = \frac{1}{2} = 0.5
$$

This clearly has exactly 1 digit after the decimal point. Hence, the statement holds for $ N = 1 $.

For $ N >=2 $

Assume that for some positive integer $ k $, the statement holds true, i.e.,

$$
2^{-k} = 0.d_1d_2d_3 \dots d_k
$$

where $ d_1d_2d_3 \dots d_k $ represents the decimal expansion of $ 2^{-k} $ and has exactly $ k $ digits.

We know that:

$$
2^{-(k+1)} = \frac{1}{2^{k+1}} = \frac{1}{2} \times 2^{-k}
$$

By the inductive hypothesis, we know that $ 2^{-k} = 0.d_1d_2d_3 \dots d_k $. Now, multiplying $ 2^{-k} $ by $ \frac{1}{2} $ shifts the decimal point one place to the right, giving us:

$$
2^{-(k+1)} = \frac{1}{2} \times 0.d_1d_2d_3 \dots d_k = 0.5 \times (0.d_1d_2d_3 \dots d_k)
$$

This results in a number with exactly $ k+1 $ digits, as required.

### Problem 6

### Final Answers:

- **Part (a)**:
  - Sum: 1.506
  - Product: 0.1162

- **Part (b)**:
  - Sum: 32.343
  - Product: 0.91342

### Problem 7

##### (a) $\ln(x + 3) - \ln(x)$ for large $ x $

We start with the given expression:

$$
\ln(x + 3) - \ln(x)
$$

By applying the logarithmic identity $ \ln(a) - \ln(b) = \ln\left( \frac{a}{b} \right) $, we rewrite the expression as:

$$
\ln(x + 3) - \ln(x) = \ln\left( \frac{x + 3}{x} \right)
$$

Simplifying the fraction inside the logarithm:

$$
\ln\left( \frac{x + 3}{x} \right) = \ln\left( 1 + \frac{3}{x} \right)
$$

For large $ x $, the term $ \frac{3}{x} $ becomes very small. Using the approximation $ \ln(1 + y) \approx y $ for small $ y $, we have:

$$
\ln\left( 1 + \frac{3}{x} \right) \approx \frac{3}{x}
$$

Thus, the equivalent formula for large $ x $ is:

$$
\ln(x + 3) - \ln(x) \approx \frac{3}{x}
$$

---

#####  (b) $ \sqrt{x^2 + 1} - x $ for large $ x $

Consider the expression:

$$
\sqrt{x^2 + 1} - x
$$

To avoid a loss of significance, we rationalize the expression by multiplying both the numerator and denominator by $ \sqrt{x^2 + 1} + x $:

$$
\sqrt{x^2 + 1} - x = \frac{\left(\sqrt{x^2 + 1} - x\right)\left(\sqrt{x^2 + 1} + x\right)}{\sqrt{x^2 + 1} + x}
$$

Using the difference of squares identity in the numerator:

$$
\left(\sqrt{x^2 + 1}\right)^2 - x^2 = (x^2 + 1) - x^2 = 1
$$

Thus, the expression simplifies to:

$$
\sqrt{x^2 + 1} - x = \frac{1}{\sqrt{x^2 + 1} + x}
$$

For large $ x $, $ \sqrt{x^2 + 1} \approx x $, so the denominator becomes approximately $ 2x $. Therefore, we have:

$$
\sqrt{x^2 + 1} - x \approx \frac{1}{2x}
$$

---

##### (c) $ \cos^2(x) - \sin^2(x) $ for $ x \approx \frac{\pi}{4} $

Using the well-known trigonometric identity for the difference of squares:

$$
\cos^2(x) - \sin^2(x) = \cos(2x)
$$

Thus, the expression simplifies to:

$$
\cos^2(x) - \sin^2(x) = \cos(2x)
$$

For $ x \approx \frac{\pi}{4} $, we have:

$$
2x \approx \frac{\pi}{2}
$$

Therefore:

$$
\cos(2x) = \cos\left( \frac{\pi}{2} \right) = 0
$$

Hence, for $ x \approx \frac{\pi}{4} $, the expression becomes:

$$
\cos^2(x) - \sin^2(x) = 0
$$

---

##### (d) $ \sqrt{\frac{1 + \cos(x)}{2}} $ for $ x \approx \pi $

Recognize that the given expression is related to the half-angle identity for cosine:

$$
\cos\left( \frac{x}{2} \right) = \sqrt{\frac{1 + \cos(x)}{2}}
$$

Thus, the expression simplifies to:

$$
\sqrt{\frac{1 + \cos(x)}{2}} = \cos\left( \frac{x}{2} \right)
$$

For $ x \approx \pi $, we have:

$$
\frac{x}{2} \approx \frac{\pi}{2}
$$

Therefore:

$$
\cos\left( \frac{x}{2} \right) = \cos\left( \frac{\pi}{2} \right) = 0
$$

Thus, for $ x \approx \pi $, the expression becomes:

$$
\sqrt{\frac{1 + \cos(x)}{2}} = 0
$$

### Problem 8

Firstly, we add the given expansions for $ \cos(h) $ and $ \sin(h) $.

$$
\cos(h) + \sin(h) = \left( 1 - \frac{h^2}{2!} + \frac{h^4}{4!} + O(h^6) \right) + \left( h - \frac{h^3}{3!} + \frac{h^5}{5!} + O(h^7) \right).
$$

Simplifying the right-hand side:

$$
\cos(h) + \sin(h) = \left( 1 + h \right) - \frac{h^2}{2!} - \frac{h^3}{3!} + \frac{h^4}{4!} + \frac{h^5}{5!} + O(h^6).
$$

The highest power of $ h $ in this expression is $ h^5 $, and the next order term is of order $ O(h^6) $.

Thus, the order of the approximation for the sum $ \cos(h) + \sin(h) $ is $ O(h^6) $.

Also, we consider the product of $ \cos(h) $ and $ \sin(h) $. We multiply the two given expansions:

$$
\cos(h) \cdot \sin(h) = \left( 1 - \frac{h^2}{2!} + \frac{h^4}{4!} + O(h^6) \right) \cdot \left( h - \frac{h^3}{3!} + \frac{h^5}{5!} + O(h^7) \right).
$$

Expanding the product:

$$
\cos(h) \cdot \sin(h) = 1 \cdot h + 1 \cdot \left( - \frac{h^3}{3!} \right) + 1 \cdot \left( \frac{h^5}{5!} \right) + \left( - \frac{h^2}{2!} \right) \cdot h + \left( - \frac{h^2}{2!} \right) \cdot \left( - \frac{h^3}{3!} \right) + O(h^7).
$$

Simplifying the terms:

$$
\cos(h) \cdot \sin(h) = h - \frac{h^3}{3!} + \frac{h^5}{5!} - \frac{h^3}{2!} + O(h^7).
$$

Combining the terms of order $ h^3 $:

$$
\cos(h) \cdot \sin(h) = h - \left( \frac{h^3}{3!} + \frac{h^3}{2!} \right) + \frac{h^5}{5!} + O(h^7).
$$

The highest power of $ h $ in this expression is $ h^5 $, and the next order term is of order $ O(h^7) $.

Thus, the order of the approximation for the product $ \cos(h) \cdot \sin(h) $ is $ O(h^6) $.
