# Method of Least Squares Approximation

The method of least squares approximation is used to fit data given in
tabular for to a simple function (e.g straight line, general polynomial,
exponential functions, etc). Type type of approximation is known as
**discrete** least squares approximation. Least squares approximations
can also be used to approximate a continuous complicated function
expression using simple functions. In this case, the approximation is
referred to as continuous least squares approximation.

# Discrete Linear Least Squares Approximation

In linear least squares approximation, the aim is to find a least
squares line $y = a_1x  + a_0$ that approximates the set of $m$ data
points $(x_k,y_k)$ for $k = 1,2,\ldots,m$ given in a table.

 ```{admonition} definition
The linear least squares method involves finding the best approximating
line when the error involved is the sum of the squares of the
differences between the $y-$values on the approximating line and the
given $y-$values.
```

The general problem of fitting the best least squares line to a
collection of $m$ data points $\displaystyle \{x_i,y_i \}_{i = 1}^{m}$
involves minimizing the **least squares error**

$
  E(a_0,a_1) = \sum_{i = 1}^{m}\left[y_i - (a_1x_i + a_0)\right]^2
$
  
To obtain the minimum, we must solve

$\frac{\partial E}{\partial a_0} = 0,\;\;\;\text{and}\;\;\;\frac{\partial E}{\partial a_1} = 0.$

Applying the chain rule to evaluate the derivative gives,

$
 \begin{aligned}
    \frac{\partial E}{\partial a_0} &=\frac{\partial}{\partial a_0}\sum_{i=1}^{m}
    \left[y_i  - (a_1x_i + a_0) \right]^2,\\
    &=\sum_{i=1}^{m}\frac{\partial}{\partial a_0}\left[y_i  - (a_1x_i + a_0) \right]^2,\\
& = \sum_{i=1}^{m} 2 \left[y_i  - (a_1x_i + a_0) \right](-1).
\end{aligned}
$

$
 \begin{aligned}
\frac{\partial E}{\partial a_1} &=\frac{\partial}{\partial a_1}\sum_{i=1}^{m}
\left[y_i  - (a_1x_i + a_0) \right]^2,\\
&=\sum_{i=1}^{m}\frac{\partial}{\partial a_1}\left[y_i  - (a_1x_i + a_0) \right]^2,\\
& = \sum_{i=1}^{m}2\left[y_i  - (a_1x_i + a_0) \right](-x_i).{LLSA2}
\end{aligned}
$

Rearranging equations ()
 and ()
 gives the normal equations


```{admonition} definition
   $
    \begin{aligned}
       a_0 m + a_1\sum_{i = 1}^m x_i & =  \sum_{i=1}^{m}y_i,\\
        a_0 \sum_{i=1}^m x_i + a_1\sum_{i = 1}^m x_i^2 & = \sum_{i = 1^ {m}x_iy_i }
   \end{aligned} 
    $
    which can be written in matrix form as
   
 $ \begin{bmatrix}    \displaystyle m & \displaystyle \sum_{i = 1}^m x_i\\
   \displaystyle \sum_{i = 1}^m x_i & \displaystyle \sum_{i = 1}^m x_i^2 
    \end{bmatrix} 
  $

    $\begin{bmatrix}
    a_0\\a_1
    \end{bmatrix}
    =
    \begin{bmatrix}
    \displaystyle \sum_{i = 1}^{m}y_i\\
    \displaystyle \sum_{i = 1}^{m}x_iy_i
    \end{bmatrix}$
 The solution of this matrix equation is
    $\begin{aligned}
    a_0 &= \frac{1}{d}\left[\left(\sum_{i = 1}^m y_i \right)\left(\sum_>{i = 1}^m x_i^2 \right) - \left(\sum_{i = 1}^m x_i \right)\left(\sum_>{i = 1}^m x_iy_i \right) \right],\\
    a_1 &= \frac{1}{d}\left[m\left(\sum_{i = 1}^m x_iy_i \right)- \left(\sum_{i = 1}^m x_i \right)\left(\sum_{i = 1}^m y_i \right) \right],
    \end{aligned} $ where
    $\displaystyle{d = m\left(\sum_{i = 1}^m x_i^2 \right) - \left(\sum_{i = 1}^m x_i \right)^2}$
 ```   

As a concrete example, consider the example below


**example**
    Find the least squares line approximating the data given in the
    following table

     x    1     2     3     4     5     6     7      8      9      10
    ----- ----- ----- ----- ----- ----- ----- ------ ------ ------ ------
    y   1.2   3.6   4.1   5.1   7.0   9.0   10.0   12.4   12.9   15.5

    : Linear least squares example

    Plot the original data points and the least squares line using a fine
    set of grid points.

**Solution:** To find the least squares line that approximates this
data, we extend the table to include rows that give the sum and columns
for the products $x_i\cdot x_i$ and $x_i \cdot y_i$ as shown in Table
().


    $x_i$              $y_i$               $x_i^2$                $x_iy_i$
  ----------------- -------------------- -------------------- ------------------------
          1                 1.2                   1                     1.2
          2                 3.6                   4                     7.2
          3                 4.1                   9                     12.3
          4                 5.1                   16                    20.4
          5                 7.0                   25                    35.0
          6                 9.0                   36                    54.0
          7                 10.0                  49                    70.0
          8                 12.4                  64                    99.2
          9                 12.9                  81                   116.1
         10                 15.5                 100                   155\.

    
   $\sum x_i = 55$   $\sum y_i  = 80.8$   $\sum x_i^2 = 385$   $\sum x_i y_i = 570.4$

  : **Solution**: Linear least squares example


The least squares approximation leads to this system of two equations
$\begin{aligned}
 10 a_0 + 55 a_1 & = 80.8\\
 55 a_0 + 385 a_1 & = 570.4
\end{aligned}$
 
  whose solution is $a_0 = -0.32$ and $a_1 = 1.527$. So
$P_1(x) = 1.527x - 0.32$.

Figure [1](#figLLSA1){reference-type="ref" reference="figLLSA1"} is a
plot of the given data and the linear least squares line.

![Linear least squares example](Chapter1LLSA1.eps){#figLLSA1}


# Discrete Polynomial Least Squares Approximation

The method of least squares approximation of a set of data
$\{(x_i,y_i)| i = 1,2,\ldots,m\}$ can be extended to approximation using
a general polynomial of degree $n < m - 1$
$P_n(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0 = \sum_{k = 0}^na_kx^k.$
The aim it to determine the parameters $a_0,a_1,a_2,\ldots,a_n$ to
minimize the least squares error

$E(a_0,a_1,a_2,\ldots,a_n) = \sum_{i = 1}^m \left[y_i - P_n(x_i) \right]^2.$
The minimum for $E$ is obtained by solving
$\displaystyle \frac{\partial E}{\partial a_j}$, for each
$j = 0,1,\ldots,n$. That is, we must solve

$\frac{\partial E}{\partial a_0} = 0,\;\;
 \frac{\partial E}{\partial a_1} = 0,\;\;
 \frac{\partial E}{\partial a_2} = 0,\;\; \cdots,\;\;
 \frac{\partial E}{\partial a_n} = 0.
$

 Thus, we must have

 $
 \begin{aligned}
  \frac{\partial E}{\partial a_j} &= \sum_{i = 1}^m \frac{\partial}{\partial a_j}\left[y_i - P_n(x_i) \right]^2 = 0,\\
  0 & =   \sum_{i = 1}^m 2\left[y_i - P_n(x_i) \right](-1)\frac{\partial P_n(x_i)}{\partial a_j}.
 \end{aligned}
 $ 
 
 Rearranging gives,
$\sum_{i = 1}^m P_n(x_i) \frac{\partial P_n(x_i)}{\partial a_j} = 
 \sum_{i = 1}^m y_i  \frac{\partial P_n(x_i)}{\partial a_j}$ for
$j = 0,1,2,\ldots,n$.

Given that $\displaystyle P_n(x_i) = \sum_{k = 0}^n a_k x_i^k$, we have

$\frac{\partial P_n(x_i)}{\partial a_j} = \frac{\partial}{\partial a_j}\left( \sum_{k = 0}^n a_k x_i^k\right) = x_i^j.$
Thus, the normal equations are given as
$\sum_{i = 1}^m \sum_{k = 0}^n a_k x_i^k x_i^j = \sum_{i =  1}^m y_i x_i^j$
or, in another form,
$\sum_{k = 0}^n a_k \left(\sum_{i = 1}^m x_i^{j+k} \right) = \sum_{i = 1}^m y_i x_i^j$
for $j  = 0,1,2,\ldots,n$. It is helpful to write the normal equations
in expandable form as

 $\begin{aligned}
 a_0\sum x_i^0 + a_1 \sum x_i^1 + a_2 \sum x_i^2 + \cdots + a_n \sum x_i^n &= \sum y_i x_i^0,\\
  a_0\sum x_i^1 + a_1 \sum x_i^2 + a_2 \sum x_i^3 + \cdots + a_n \sum x_i^{n+1} &= \sum y_i x_i^1,\\
 a_0\sum x_i^2 + a_1 \sum x_i^3 + a_2 \sum x_i^4 + \cdots + a_n \sum x_i^{n+2} &= \sum y_i x_i^2,\\
 & \vdots \\
 a_0\sum x_i^n + a_1 \sum x_i^{n+1} + a_2 \sum x_i^{n+2} + \cdots + a_n \sum x_i^{2n} &= \sum y_i x_i^n. 
 \end{aligned} \\
 $

In matrix form, the normal equations can be written as

$$
    \begin{bmatrix}
    \sum x_i^0 & \sum x_i^1 & \sum x_i^2 & \cdots & \sum x_i^n \\
    \sum x_i^1 & \sum x_i^2 & \sum x_i^3 & \cdots & \sum x_i^{n+1} \\
    \sum x_i^2 & \sum x_i^3 & \sum x_i^4 & \cdots & \sum x_i^{n+2} \\
    \vdots   &    \vdots  &    \vdots  &  \vdots& \vdots \\ 
    \sum x_i^n & \sum x_i^{n+1} & \sum x_i^{n+2} & \cdots & \sum x_i^{2n} \\
    \end{bmatrix}
    \begin{bmatrix}
    a_0\\a_1\\a_2\\\vdots\\a_n
    \end{bmatrix}
    = 
    \begin{bmatrix}
    \sum y_i x_i^0\\
    \sum y_i x_i^1\\
    \sum y_i x_i^2\\
        \vdots \\
    \sum y_i x_i^n
    \end{bmatrix}
$$

 example
Find the quadratic polynomial that best fits the following data in the
sense of least squares

  $x$   -2   -1   0   1   2
  ----- ---- ---- --- --- ---
  $y$   2    1    1   1   2

  : Quadratic least squares example

**Solution:** We rearrange the table as follows

$x_i$             $y_i$             $x_i^2$            $x_i^3$             $x_i^4$             $x_iy_i$             $x_i^2y_i$
---------------- ----------------- ------------------- ------------------ ------------------- -------------------- -----------------------
    -2                2                  4                  -8                 16                   -4                     8
    -1                1                  1                  -1                  1                   -1                     1
    0                 1                  0                  0                   0                   0                      0
    1                 1                  1                  1                   1                   1                      1
    2                 2                  4                  8                  16                   4                      8
$\sum x_i = 0$   $\sum y_i  = 7$   $\sum x_i^2 = 10$   $\sum x_i^3 = 0$   $\sum x_i^4 = 34$   $\sum x_i y_i = 0$   $\sum x_i^2 y_i = 18$

  : Solution: Quadratic least squares example


For this problem, the normal equations are

 $ \begin{aligned}
 a_0\sum x_i^0 + a_1 \sum x_i^1 + a_2 \sum x_i^2  &= \sum y_i x_i^0,\\
  a_0\sum x_i^1 + a_1 \sum x_i^2 + a_2 \sum x_i^3 &= \sum y_i x_i^1,\\
 a_0\sum x_i^2 + a_1 \sum x_i^3 + a_2 \sum x_i^4  &= \sum y_i x_i^2,\\\end{aligned} $
Evaluating the sums gives $\begin{array}{cccccccc}
5a_0 & + & & & 10 a_2 & = & 7 \\
     &   &10a_1& &  & =& 0 \\
10a_0&+&& &34a_2&=&18     
\end{array}$ Solving the above system gives
$a_0 = \frac{29}{35},\;\;\;a_1 = 0,\;\;\; a_2 = \frac{2}{7}.$ Thus,
the least squares polynomial of degree 2 that fits the data is
$P_2(x) = \frac{2}{7}x^2 + \frac{29}{35}$ The total error is
$E = \sum_{i  = 1}^{5}\left[y_i - P(x_i)\right]^2 = \frac{2}{35} = 0.0571429$
This is the least that can be obtained by using a polynomial of degree
at most 2.


# Non-polynomial least squares approximation

The least squares approximation method is not limited to approximating
using polynomials. Occasionally, it can be assumed that the data are
exponentially related. This requires the approximating function to be of
the form $y = b e^{ax}\;\;\;\; \text{or}\;\;\;\; y = bx^a.$ The
corresponding least square error to be minimized is

$E(a,b) = \sum_{i = 1}^m (y_i - b e^{ax_i})^2\;\;\;\; \text{or}\;\;\;\; 
E(a,b) = \sum_{i = 1}^m (y_i - b x_i^a)^2$
To avoid ending up with nonlinear equations that cannot be solved exactly, it may be necessary
to simplify the approximating equation using properties of logarithms
$\ln y = \ln b + ax\;\;\; \text{or}\;\;\; \ln y = \ln b + a \ln x$

Another commonly used function is the combination between logarithmic,
trigonometric and exponential functions
$y = a \ln x + b \cos x + c  e^x$ with least squares error

$E(a,b,c) = \sum_{i = 1}^m \left[y_i - (a\ln x_i + b \cos x_i + ce^{x_i}) \right]^2$

# Discrete Least Squares Using Basis Functions

The least squares principle can be extended general functions in exactly
the same way as was done in previous sections. Suppose that data points
conform to the general relationship

$
 y = \sum_{k = 0}^{n} c_k \phi_k(x) $ in which the **basis
functions** $\phi_0, \phi_1,\ldots, \phi_n$ are known and held fixed.
The coefficients $c_0,c_1,c_2,\ldots,c_n$ are determined according to
the principle of least squares in the usual way. Proceeding as before,
the least squares error expression is

$
E(c_0,c_1,\ldots,c_n) = \sum_{j = 1}^{m}\left[y_j - \sum_{k = 0}^n c_k \phi_k(x_j) \right]^2$

It can be shown that the normal equations in this situation are given by

$$
 \sum_{k = 0}^n \left[\sum_{j=1}^m \phi_i(x_j) \phi_{k}(x_j)\right]c_k = \sum_{j = 1}^m y_j \phi_i(x_j),\;\;\;\text{where $0 \leq i \leq n$}
 $$

Equation [\[LSABasis3\]](#LSABasis3){reference-type="eqref"
reference="LSABasis3"} forms a linear matrix system that depends on the
nature of the basis $\{\phi_0(x),\phi_1(x),\ldots,\phi_n(x)\}$. The
resulting matrix system has an identity matrix as coefficient matrix if
the basis has the property of orthonormality.

 ```{admonition} definition
The basis $\{\phi_0(x),\phi_1(x),\ldots,\phi_n(x)\}$ is said to be an
orthornomal set of functions if
$\sum_{j=1}^m \phi_i(x_j) \phi_{k}(x_j)  = 
\left\{\begin{array}{cc}
1~~&~~i  =  k\\
0~~&~~i \neq k 
\end{array} \right.$
```

Applying the orthonormality property on equation
[\[LSABasis3\]](#LSABasis3){reference-type="eqref"
reference="LSABasis3"} simplifies the equation to

{Orthonormal2}
$$c_i = \sum_{j = 1}^{m}y_j\phi_i(x_j),\;\;\;\;\; 0 \leq i \leq n$$

Equation [\[Orthonormal2\]](#Orthonormal2){reference-type="eqref"
reference="Orthonormal2"} is an explicit formula for evaluating the
coefficients $c_i$.

## Summary:Discrete Least Squares Approximation

**Keywords:** Minimax Problem, Absolute Deviation, Least Squares, Normal
equations

**Intended learning outcomes (ILOs):**

1.  **Discrete Least squares approximation**

    -   Derive the normal equations based on minimizing the linear least
        squares error
        $E(a_0,a_1) = \sum_{i=1}^{m} \left[y_i - (a_1 x + a_0) \right]^2$

    -   Compute the least squares line approximating the data from a
        given table.

    -   Derive the normal equations based on minimizing the polynomial
        least squares error
        $E(a_0,a_1,a_2,\ldots,a_n) = \sum_{i=1}^{m} \left[y_i - P_n(x_i) \right]^2$
        where $\displaystyle { P_n(x) = \sum_{k=0}^n a_k x^k }$.

    -   Find data given in a table with discrete least squares
        polynomials of degree at most $n = 2,3,4,\ldots$.

    -   *Use Matlab to compute the coefficients,
        $a_0,a_1,a_2,\ldots,a_n$, of the discrete least squares
        polynomials.*

## Practice Problems

1.  Find an equation of the form $y = ae^{x^2} + bx^3$ that best fits
    the points (-1,0), (0,1) and (1,2) in the least-squares sense.

2.  Find the equation of a parabola of the form $y = ax^2 + b$ that best
    represents the following data using the method of least squares.

     center
      $x$   -1    0     1
      ----- ----- ----- -----
      $y$   3.1   0.9   2.9
    

3.  What constant $c$ makes the expression
    $\sum_{k = 0}^m [f(x_k) - c e^{x_k}]^2$ as small as possible?

4.  Show that the formula for the best line to fit data $(k,y_k)$ at the
    integers $k$ for $1 \leq k \leq n$ is $y = ax + b$ where
     \begin{aligned}
    a&= \frac{6}{n(n^2-1)}\left[2\sum_{k=1}^n ky_k - (n+1)\sum_{k=1}^ny_k\right]\\
    b&=\frac{2}{n(n-1)}\left[(2n+1)\sum_{k=1}^ny_k - 3\sum_{k=1}^nky_k\right]\end{aligned}

5.  Find the best function (in the least squares sense) that fits the
    following data points and is of the form
    $f(x) = a \sin \pi x + b \cos \pi x$

     center
      $x$   -1   $-\frac{1}{2}$   0   $\frac{1}{2}$   1
      ----- ---- ---------------- --- --------------- ---
      $y$   -1   0                1   2               1
    

6.  Find the quadratic polynomial that best fits the following data in
    the sense of least squares

     center
      $x$      -2       -1       0       1       2  
      ------  -------- -------- ------- ------- -------
    $y$     2        1        1       1       2
    

7.  Find the least squares polynomials of degrees 1,2 and 3 for the data
    in the following tables. Compute the error $E$ in each case. Graph
    the data and the polynomials.

    1.   center
          $x$   0     0.15    0.31    0.5     0.6     0.75
          ----- ----- ------- ------- ------- ------- -------
          $y$   1.0   1.004   1.031   1.117   1.223   1.422
        

    2.   center
          $x$   1.0     1.1    1.3    1.5    1.9    2.1
          ----- ------- ------ ------ ------ ------ ------
          $y$   1.84    1.96   2.21   2.45   2.94   3.18
        

# Continuous Least Squares Approximation

In the last section we discussed Discrete Least Squares Approximation in
which a collection of data points were fitted into a continuous
function. In this section, we consider the approximation of a continuous
function by another continuous function (e.g a polynomial function).

Suppose $f \in C[a,b]$ and that a polynomial
$\displaystyle P_n(x) = \sum_{k=0}^n a_k x^k$ is required to minimize
the error

$
\int_a^b \left[f(x) - P_n(x) \right]^2~dx.
$ 
The above expression
denotes the total square of the deviation (error) of $P_n(x)$ from
$f(x)$. For continuous least squares approximation using polynomials,
the aim is to determine the coefficients $a_0,a_1,\ldots,a_n$ that will
minimize the error $E$ defined as
$E(a_0,a_1,\ldots,a_n) = \int_a^b \left( f(x) - \sum_{k=0}^n a_k x^k \right)^2~ dx$

The necessary condition for the coefficients to minimize $E$ is that
$\frac{\partial E}{\partial a_j} = 0,\;\;\;\;\;\text{for each}\;\; j=0,1,2,\ldots,n.$
Differentiating the integral gives

$
 \begin{aligned}
\frac{\partial E}{\partial a_j}& = \int_a^b 2\left[f(x) - P_n(x)\right](-1)\frac{\partial P_n}{\partial a_j}~dx = 0,\\
\int_a^b P_n \frac{\partial P_n}{\partial a_j}~dx& = \int_a^b f(x) \frac{\partial P_n}{\partial a_j}~dx\\
\int_a^b \sum_{k=0}^n a_k x^k \cdot x^j~dx &= \int_{a}^b f(x) x^j~dx,\;\;\;\; \left[\text{Note that:}\;\; \frac{\partial P_n}{\partial a_j} = x^j \right]\\
\sum_{k = 0}^n a_k \int_a^b x^{k+j}~dx &= \int_a^b x^j f(x)~dx{CLSAnormal}.\end{aligned}
$
Hence, to determine $a_0,a_1,\ldots,a_n$, and the polynomial $P_n(x)$,
the **normal equations** given by
[\[CLSAnormal\]](#CLSAnormal){reference-type="eqref"
reference="CLSAnormal"} must be solved.

 example
Find the linear least squares approximation to $f(x) = e^x$ on \[-1,1\]
and determine the relative error at $x = 0.5$.

**Solution:** For this example we have $n = 1$ and
$P_1(x) = a_0 + a_1x$. The normal equations are  $\begin{aligned}
\sum_{k = 0}^1 a_k \int_{-1}^{1} x^{k+j}~dx = \int_{-1}^{1} x^j f(x)~dx,\;\;\;j = 0,1\end{aligned}$
Evaluating the summations gives  $\begin{aligned}
a_0\int_{-1}^{1} x^0 dx + a_1 \int_{-1}^{1} x dx & = \int_{-1}^{1} x^0 e^x dx,\\
a_0\int_{-1}^{1} x^1 dx + a_1 \int_{-1}^{1} x^2 dx & = \int_{-1}^{1} x^1 e^x dx,\\\end{aligned}$
Evaluating the integrals gives  $\begin{aligned}
2a_0& = e - e^{-1},\\
\frac{2}{3}a_1 & = 2e^{-1}\end{aligned}$ Thus,  $\begin{aligned}
a_0  &= \frac{1}{2}(e - e^{-1}) = 1.1752\\
a_1  &=  3e^{-1} = 1.1037\
\text{Hence};\;\;\;P_1(x) &= 1.1752 + 1.1037x \end{aligned}$ At
$x = 0.5$, $P_1(0.5) = 1.7271$ (approximation) and
$f(0.5) = e^{0.5} = 1.6487$ (exact value). Thus, the relative error is

$\frac{|f(0.5) - P_1(0.5)|}{|f(0.5)|} = 0.0476$


**example**
Find the least squares approximation of degree 2 for the function
$f(x) = e^x$ on \[-1,1\].

**Solution:** The normal equations for $n = 2$,
$P_2(x) = a_0 + a_1x + a_2x^2$ are

$$
    \begin{bmatrix}
    \int_{-1}^{1} x^0~dx & \int_{-1}^{1} x^1~dx & \int_{-1}^{1} x^2~dx \\
    \int_{-1}^{1} x^1~dx & \int_{-1}^{1} x^2~dx & \int_{-1}^{1} x^3~dx \\
    \int_{-1}^{1} x^2~dx & \int_{-1}^{1} x^3~dx & \int_{-1}^{1} x^4~dx \\
    \end{bmatrix}

    \begin{bmatrix}
    a_0\\a_1\\a_2
    \end{bmatrix}
    = 
    \begin{bmatrix}
    \int_{-1}^{1} x^0e^x\\
    \int_{-1}^{1} x^1e^x\\
    \int_{-1}^{1} x^2e^x
    \end{bmatrix}
$$
  Performing the integration yields

$$
\begin{bmatrix}
2 & 0 & \frac{2}{3}\\
0 & \frac{2}{3}& 0 \\
\frac{2}{3}& 0& \frac{2}{5}
\end{bmatrix}
\begin{bmatrix}
a_0 \\a_1\\a_2
\end{bmatrix} 
= 
\begin{bmatrix}
e - e^{-1}\\ 2e^{-1} \\ e - 5e^{-1}
\end{bmatrix} =
$$
 Solving gives
$a_0 = 0.9963,\;\;\;a_1 = 1.1037,\;\;\;a_2 = 0.5368$ Thus,
$P_2(x) = 0.9963 + 1.1037x + 0.5368x^2$


 example
Find the least squares quadratic function of the form $ax^2 + b$, which
best fits the curve $y = \sqrt{2x +1}$ over the interval
$0 \leq  x \leq \frac{3}{2}$.

**Solution:** Define the least squares error as
$E(a,b) = \int_{0}^{\frac{3}{2}} \left[ y - (ax^2+b)\right]^2dx$ To
minimize the least squares error, we differentiate $E(a,b)$ with respect
to $a$ and $b$, in turn, and equate the derivative to zero.

$
 \begin{aligned}
\frac{\partial E}{\partial a} = \int_{0}^{\frac{3}{2}} 2\left[ y - (ax^2+b)\right](-x^2)dx &= 0,\\
\Rightarrow   \int_{0}^{\frac{3}{2}}  (ax^4+bx^2)dx &= 
\int_{0}^{\frac{3}{2}}  yx^2dx\\
  a\int_{0}^{\frac{3}{2}}  x^4dx + b\int_{0}^{\frac{3}{2}}  x^2~dx &= \int_{0}^{\frac{3}{2}} x^2\sqrt{2x+1}~dx\end{aligned}
$

$
 \begin{aligned}
\frac{\partial E}{\partial b} = \int_{0}^{\frac{3}{2}} 2\left[ y - (ax^2+b)\right](-1)dx &= 0,\\
\Rightarrow   \int_{0}^{\frac{3}{2}}  (ax^2+b)dx &= 
\int_{0}^{\frac{3}{2}}  ydx\\
  a\int_{0}^{\frac{3}{2}}  x^2~dx + b\int_{0}^{\frac{3}{2}}  ~dx &= \int_{0}^{\frac{3}{2}} \sqrt{2x+1}~dx\end{aligned}
$

Thus, the normal equations are
$
 \begin{aligned}
  a\int_{0}^{\frac{3}{2}}  x^4~dx + b\int_{0}^{\frac{3}{2}}  x^2~dx &= \int_{0}^{\frac{3}{2}} x^2\sqrt{2x+1}~dx\\
  a\int_{0}^{\frac{3}{2}}  x^2~ dx + b\int_{0}^{\frac{3}{2}}  ~dx &= \int_{0}^{\frac{3}{2}} \sqrt{2x+1}~dx\end{aligned}
$

To compute the integral
$\displaystyle I_2 =  \int_{0}^{\frac{3}{2}} x^2\sqrt{2x+1}~dx$ we set
$u = 2x + 1$ and note that $dx = \frac{1}{2}du$. Also, when $x = 0$,
$u = 1$ and when $x = \frac{3}{2}$, $u = 4$. Thus,

$$
 \begin{aligned}
I_1 &=  \int_{0}^{\frac{3}{2}} x^2\sqrt{2x+1}~dx\\
    &= \int_{1}^{4}\left[\frac{1}{2}(u-1)\right]^2u^{\frac{1}{2}}\left(\frac{1}{2}~du\right)\\
     &= \frac{1}{8} \int_{1}^{4}\left(u^{\frac{5}{2}} - 2u^{\frac{3}{2}} + u^{\frac{1}{2}}\right)~du\\
     &= \frac{1}{8} \left[ \frac{2}{7}u^{\frac{7}{2}} - \frac{4}{5}u^{\frac{5}{2}} + \frac{2}{3}u^{\frac{3}{2}}\right]_{1}^{4}\\
     &= \frac{1}{8}\left(\frac{2}{7}(128) - \frac{4}{5}(32) + \frac{2}{3}(8)\right) - \frac{1}{8}\left(\frac{2}{7} - \frac{4}{5} + \frac{2}{3}\right)\\
     &=\frac{214}{105} - \frac{2}{105} = \frac{212}{105}\end{aligned}

 \begin{aligned}
I_2 &=  \int_{0}^{\frac{3}{2}} \sqrt{2x+1}~dx\\
    &= \int_{1}^{4}u^{\frac{1}{2}}\left(\frac{1}{2}~du\right) = \frac{1}{2}\int_{1}^{4}u^{\frac{1}{2}}~du\\
    &= \left.\frac{1}{2}\frac{2}{3}u^{\frac{3}{2}}\right]_{1}^{4}= \frac{1}{3}(8-1) = \frac{7}{3}\end{aligned}

 \begin{aligned}
I_3 = \int_{0}^{\frac{3}{2}} x^4~dx = \left.\frac{1}{5}x^5\right|_{0}^{\frac{3}{2}} = \frac{243}{160}\\
I_4 = \int_{0}^{\frac{3}{2}} x^2~dx = \left.\frac{1}{3}x^2\right|_{0}^{\frac{3}{2}} = \frac{9}{8}\\
I_5 = \int_{0}^{\frac{3}{2}} dx = \frac{3}{2}\end{aligned}
$$
Substituting in the normal equations gives  
$
\begin{aligned}
\frac{243}{160}a  + \frac{9}{8}b & = \frac{212}{105}\\
\frac{9}{8}a + \frac{3}{2}b & = \frac{7}{3} \end{aligned} 
$
Thus,

$
 \begin{aligned}
a & = \frac{\left|\begin{array}{cc}
\frac{212}{105}&\frac{9}{8}\\
\frac{7}{3}& \frac{3}{2}
\end{array} \right|}{\left|\begin{array}{cc}
\frac{243}{160}&\frac{9}{8}\\
\frac{9}{8}& \frac{3}{2}
\end{array} \right|}  = \frac{\frac{113}{280}}{\frac{81}{80}} = \frac{226}{567},\;\;\;\;\;\;\;
b  =\frac{\left|\begin{array}{cc}
\frac{243}{160}&\frac{212}{105}\\
\frac{9}{8}& \frac{7}{3}
\end{array} \right|}{\left|\begin{array}{cc}
\frac{243}{160}&\frac{9}{8}\\
\frac{9}{8}& \frac{3}{2}
\end{array} \right|}  = \frac{\frac{285}{224}}{\frac{81}{80}} = \frac{475}{378}.\end{aligned}
$
Thus, the least squares approximating polynomial is
$\displaystyle y  = \frac{226}{567}x^2 + \frac{475}{378}$


## Summary:Continuous Least squares approximation

1.  **Intended learning outcomes (ILOs):**

    -   Derive the normal equations based on minimizing the least
        squares error

        $E(a_0,a_1,a_2,\ldots,a_n) = \int_a^b \left[f(x) - P_n(x) \right]^2dx$
        where $\displaystyle { P_n(x) = \sum_{k=0}^n a_k x^k }$.

    -   Compute the least squares approximating polynomial of degree
        $n = 2,3,\ldots$, for a given function $f(x)$ on a given
        interval $[a,b]$

    -   *Use Matlab to compute the coefficients,
        $a_0,a_1,a_2,\ldots,a_n$, of the continuous least squares
        polynomials.*

## Practice Problems 

1.  Find the linear least squares approximation to $f(x) = x^2 + 3x + 2$
    on \[0,1\].

2.  Find the least squares quadratic approximation to
    $\displaystyle \frac{1}{x}$ on \[1,4\]

3.  Find the least squares approximations to $\displaystyle \sqrt{x}$ on
    \[0,1\] of degrees 1, 2 and 3.

4.  Find the least squares approximating polynomial of degree 2 to the
    following functions on the given intervals

    1.  $\displaystyle f(x) = e^x$ on \[0,2\]

    2.  $\displaystyle f(x) = \frac{1}{x+2}$ on \[-1,1\]

5.  Find the least squares approximating polynomial of degree 3 to the
    following functions on the interval $[-1,1]$

    1.  $\displaystyle f(x) = e^x$

    2.  $\displaystyle f(x) = \cos(\pi x)$

# Continuous Least Squares Approximation using Orthogonal Basis Functions

In the previous section, we considered least squares approximation using
a general $n$-th degree polynomial of the form
$P_n(x) = a_0 + a_1x + a_2x^2 + \cdots + a_{n-1}x^{n-1} + a_nx^n = \sum_{k = 0}^{n} a_k x^k$
which is a linear combination of the *basis functions*
$\{1,x,x^2,\ldots,x^{n-1},x^n \}.$

The disadvantage of using a polynomial constructed using monomial basis
in least squares approximation is that the coefficient matrix in the
linear system used to determine the unknown coefficients
$a_0,a_1,\ldots,a_n$ is ill-conditioned and leads to round-off error
problems. The entries of the coefficient matrix are obtained from the
integral
$
\int_{a}^b x^{j+k}~dx = \frac{b^{j+k+1} - a^{j+k+1}}{j+k+1}.
$ The
matrix is known as the **Hilbert matrix**. Linear systems involving the
Hilbert matrix cannot be computed efficiently and are known to be
susceptible to errors such as round off errors.

In this section, we consider a computationally efficient way of
obtaining the coefficients used to determine $P_n(x)$ in least squares
approximation. We also discuss the use of **orthogonal** polynomials is
dealing with the difficulties that arise in solving large,
ill-conditioned systems of linear equations. To facilitate the
discussions we present some new concepts and definitions.

 ```{admonition} definition
The set of functions $\{\phi_0,\phi_1,\phi_2,\ldots,\phi_n \}$ is said
to be **linearly independent** on $[a,b]$ if, whenever
$c_0\phi_0(x) + c_1\phi_1(x) + \cdots + c_n\phi_n(x)=0,\;\;\;\text{for all}\;\; x \in [a,b]$
we have $c_0 = c_1 = \cdots = c_n = 0.$ Otherwise the set of functions
is said to be **linearly dependent.**
```

 theorem
Suppose that $\phi_j(x)$ is a polynomial of degree $j$ for each
$j = 0,1,2,\ldots,n$. Then the set $\{\phi_0,\phi_1,\ldots,\phi_n \}$ is
linearly independent on any interval $[a,b]$.


 ```{admonition} definition
An integrable function $w(x)$ is said to be a weight function on the
interval $I = [a,b]$ if $w(x) \geq 0$, for all $x$ in $I$, but
$w(x)\neq 0$ on any subinterval of $I$.
```

The purpose of a weight function is to give more "weight\" or influence
to approximations on certain portions of the interval.

Given that

1.  $\{\phi_0,\phi_1,\ldots,\phi_n \}$ is a set of linearly independent
    functions on $[a,b]$

2.  $w(x)$ is a weight function for $[a,b]$.

3.  $f(x)$ is continuous on $[a,b]$

We seek a linear combination $P(x) = \sum_{k=0}^n a_k \phi_k(x)$ to
minimize the error
$E(a_0,a_1,\ldots,a_n) = \int_a^b w(x)\left[f(x) - \sum_{k=0}^n a_k \phi_k(x) \right]^2~dx$

It should be noted that when $w(x) = 1$ and $\phi_k(x) = x^k$, the
problem reduces to the continuous least squares approximation using
monomials that was discussed earlier.

The normal equations are obtained by solving
$\displaystyle{\frac{\partial E}{\partial a_j} = 0}$ for each
$j = 0,1,\ldots,n$. Thus, we have

$\frac{\partial E}{\partial a_j} = 2\int_{a}^bw(x)\left[f(x) - \sum_{k=0}^n a_k \phi_k(x) \right]\phi_j(x)~dx.$
The **normal equations** can be written as ${NormalOrthogonal}
\int_a^b w(x) f(x)\phi_j(x)~dx = \sum_{k=0}^{n}a_k \int_a^b w(x)\phi_k(x)\phi_j(x)~dx,\;\;\;\;j = 0,1,2,\ldots,n.$
Suppose that the functions $\phi_i$, for $i = 0,1,\ldots,n$, are chosen
in such a way that 
$$
    \int_a^b w(x)\phi_k(x)\phi_j(x)~dx = \left\{
    \begin{array}{ll}
    0, &\text{when $j \neq k$},\\
    \alpha_j > 0,& \text{when $j = k$}
\end{array}\right.
$$

 then, for each $j = 0,1,\ldots,n$, the normal
equations will reduce to

$\int_a^b w(x) f(x)\phi_j(x)~dx = a_j \int_a^b w(x) [\phi_j(x)]^2 = a_j\alpha_j$
and $a_j = \frac{1}{\alpha_j}\int_a^b w(x)f(x)\phi_j(x)~dx$ Hence the
least squares approximation problem is greatly simplified when the
functions $\phi_0,\phi_1,\ldots,\phi_n$ are chosen to satisfy condition
reference="orthogonality1"}, known as the **orthogonality condition.**

 ```{admonition} definition
The set $\{\phi_0,\phi_1,\ldots,\phi_n \}$ is said to be an **orthogonal
set of functions** for the interval $[a,b]$ with respect to the weight
function $w(x)$ if
```
$$
\int_a^b w(x)\phi_k(x)\phi_j(x)~dx = \left\{
    \begin{array}{ll}
0, &\text{when $j \neq k$},\\
\alpha_j > 0,& \text{when $j = k$}
\end{array}\right.
$$

 If, in addition, $\alpha_j = 1$ for each
$j = 0,1,\ldots,n$, the set is said to be **orthonormal**.


 theorem
If $\{\phi_0,\phi_1,\ldots,\phi_n\}$ is an orthogonal set of functions
on an interval $[a,b]$ with respect to the weight function $w(x)$, then
the least squares approximation to $f(x)$ on $[a,b]$ with respect to
$w(x)$ is $P_n(x) = \sum_{j = 0}^{n}a_j\phi_j(x)$ where, for each
$j = 0,1,\ldots,n$,
$a_j = \frac{\int_a^bw(x)\phi_j(x)f(x)~dx}{\int_a^b w(x)[\phi_j(x)]^2} = \frac{1}{\alpha_j}\int_a^b w(x)\phi_j(x)f(x)~dx$


The following theorem, called the **Gram-Schmidt process**, can be used
to recursively generate an orthogonal set of polynomials.

 theorem
The set of polynomials $\{\phi_0,\phi_1,\ldots,\phi_n \}$ defined in the
following way is orthogonal on $[a,b]$ with respect to the weight
function $w(x)$,
$\phi_0(x) = 1,\;\;\; \phi_1(x) = x  - B_1,\;\;\; \text{for each}\;\;x\in [a,b]$
where,
$B_1 = \frac{\int_{a}^b x w(x)[\phi_0(x)]^2~dx}{\int_a^b w(x)[\phi_0(x)]^2~dx}$
and when $k \geq 2$,
$\phi_k(x) = (x-B_k)\phi_{k-1}(x) - C_k\phi_{k-2}(x),\;\;\text{for each}\;\;x\in [a,b]$
where
$B_k  = \frac{\int_a^b xw(x)[\phi_{k-1}(x)]^2~dx}{\int_a^b w(x)[\phi_{k-1}(x)]^2~dx}$
and
$C_k  = \frac{\int_a^b xw(x)\phi_{k-1}(x)\phi_{k-2}(x)~dx}{\int_a^b w(x)[\phi_{k-2}(x)]^2~dx}$


 example
1.  Use the Gram-Schmidt process to construct the Legendre polynomials
    $\phi_1(x), \phi_2(x), \phi_3(x), \phi_4(x)$. Here,
    $\{\phi_0,\phi_1,\phi_2,\phi_3,\phi_4\}$ is an orthogonal set on
    $[-1,1]$ with respect to the weight $w(x) = 1$, given that
    $\phi_0(x) = 1$.

2.  Use the Legendre polynomials obtained in (i) above to approximate
    $f(x) = |x|$ using on the interval $[-1,1]$.

**Solution**\
The orthogonal functions will be given by
$$
    \begin{aligned}
    \phi_1(x) &= x - B_1\\
    \phi_2(x) &= (x - B_2)\phi_1(x) - C_2\phi_0(x)\\
    \phi_3(x) &= (x - B_3)\phi_2(x) - C_3\phi_1(x)\\
    \phi_4(x) &= (x - B_4)\phi_3(x) - C_4\phi_2(x)\end{aligned}
$$
Since
$B_1 = \frac{\displaystyle \int_{-1}^{1}xdx}{\displaystyle \int_{-1}^{1}dx} = 0$
then $\phi_1(x) = x$. The values of $B_2$ and $C_2$ are given by

$B_2 = \frac{\displaystyle \int_{-1}^{1}x[\phi_1(x)]^2dx}{\displaystyle \int_{-1}^{1}[\phi_1(x)]^2dx} = \frac{\displaystyle \int_{-1}^{1}x^3dx}{\displaystyle \int_{-1}^{1}x^2dx} = 0$
$c_2 =\frac{\displaystyle \int_{-1}^{1}x\phi_1(x)\phi_0(x)dx}{\displaystyle \int_{-1}^{1}[\phi_0(x)]^2dx} = \frac{\displaystyle \int_{-1}^{1}x^2dx}{\displaystyle \int_{-1}^{1}dx} =\frac{1}{3}$

Therefore,
$\phi_2(x) = (x - B_2)\phi_1(x) - C_2\phi_0(x) = x^2 - \frac{1}{3}$

$
B_3 = \frac{\displaystyle \int_{-1}^{1}x[\phi_2(x)]^2dx}{\displaystyle \int_{-1}^{1}[\phi_2(x)]^2dx} = \frac{\displaystyle \int_{-1}^{1}x\left(x^2 - \frac{1}{3}\right)^2dx}{\displaystyle \int_{-1}^{1}\left(x^2 - \frac{1}{3}\right)^2dx} =
0
$
 and

$
 \begin{aligned}
C_3&=\displaystyle \frac{\displaystyle \int_{-1}^{1}x\phi_2(x)\phi_1(x)dx}{\displaystyle \int_{-1}^{1}[\phi_1(x)]^2dx}
=\displaystyle  \frac{\displaystyle \displaystyle \int_{-1}^{1}x^2\left(x^2 - \frac{1}{3}\right)dx}{\displaystyle \int_{-1}^{1}x^2dx} =
\frac{4}{15}\end{aligned}
$
 Therefore,
$\displaystyle \phi_3(x) = (x - B_3)\phi_2(x) - C_3\phi_1(x) = x^3 - \frac{3}{5}x$.

Lastly, we have

$B_4 = \frac{\displaystyle \int_{-1}^{1}x[\phi_3(x)]^2dx}{\displaystyle \int_{-1}^{1}[\phi_3(x)]^2dx} = \frac{\displaystyle \int_{-1}^{1}x\left(x^3 - \frac{3}{5}x\right)^2dx}{\displaystyle \int_{-1}^{1}\left(x^3 - \frac{3}{5}x\right)^2dx} =
0$ and
$$
 \begin{aligned}
C_4&=\displaystyle \frac{\displaystyle \int_{-1}^{1}x\phi_3(x)\phi_2(x)dx}{\displaystyle \int_{-1}^{1}[\phi_2(x)]^2dx}
=\displaystyle  \frac{\displaystyle \displaystyle \int_{-1}^{1}x\left(x^3 - \frac{3}{5}x\right)\left(x^2 - \frac{1}{3} \right)dx}{\displaystyle \int_{-1}^{1}\left(x^2 - \frac{1}{3}\right)^2dx} =
\frac{9}{35}\end{aligned}
$$
Therefore,
$\displaystyle \phi_4(x) = (x - B_4)\phi_3(x) - C_4\phi_2(x) = x^4 - \frac{6}{7}x^2 + \frac{3}{35}$

We want to find
$P_4(x) = a_0 \phi_0(x) + a_1 \phi_1(x) + a_2 \phi_2(x) + a_3\phi_3(x) +  a_4\phi_4(x)$
with
$\displaystyle{a_j = \frac{\int_{-1}^{1} w(x) f(x) \phi_j(x) ~dx}{\int_{-1}^{1} w(x) \phi_j^2(x) ~dx} }$

$
 \begin{aligned}
a_0 & = \frac{\int_{-1}^{1} |x|  ~dx}{\int_{-1}^{1}  ~dx} =  \frac{2\int_{-1}^{1} x  ~dx}{\int_{-1}^{1}  ~dx} = \frac{1}{2}\\
a_1 & = \frac{\int_{-1}^{1} |x|x  ~dx}{\int_{-1}^{1} x^2 ~dx} = 0\\
a_2 & = \frac{\int_{-1}^{1} |x|\left(x^2 - \frac{1}{3}\right)  ~dx}{\int_{-1}^{1} \left(x^2-\frac{1}{3}\right)^2 ~dx} =  \frac{2\int_{0}^{1} x \left(x^2 - \frac{1}{3}\right)    ~dx}{\int_{-1}^{1} \left(x^2-\frac{1}{3}\right)^2 ~dx} = \frac{15}{16} \\
a_3 & = \frac{\int_{-1}^{1} |x|\left(x^3 - \frac{3x}{5}\right)  ~dx}{\int_{-1}^{1} \left(x^3-\frac{3x}{5}\right)^2 ~dx} =  \frac{2\int_{0}^{1} x \left(x^3 - \frac{3x}{5}\right)    ~dx}{\int_{-1}^{1} \left(x^3-\frac{3x}{5}\right)^2 ~dx} = 0 \\
a_4 & = \frac{\int_{-1}^{1} |x|\left(x^4 - \frac{6}{7}x^2 + \frac{3}{35}\right)  ~dx}{\int_{-1}^{1} \left(x^4 - \frac{6}{7}x^2 + \frac{3}{35}\right)^2 ~dx} =  \frac{2\int_{0}^{1} x \left(x^4 - \frac{6}{7}x^2 + \frac{3}{35}\right)    ~dx}{\int_{-1}^{1} \left(x^4 - \frac{6}{7}x^2 + \frac{3}{35}\right)^2 ~dx} = -\frac{105}{128} \end{aligned}
$

$\displaystyle{P_4(x) = \frac{1}{2} + \frac{15}{16}\left(x^2 - \frac{1}{3} \right) - \frac{105}{128}\left(x^4 - \frac{6}{7}x^2 + \frac{3}{35}\right) = -\frac{105 x^4}{128} + \frac{105 x^2}{64} + \frac{15}{128}  }$

The figure below, shows a comparison between $f(x) = |x|$ and $P_4(x)$.

![Comparison between $f(x) = |x|$ and
$P_4(x)$](Orthogonal.eps){#figorthogonal}


## Summary: Least Squares Approximation - Orthogonal functions

**Keywords:**Linear independent functions, Orthogonal functions,
Gram-Schmidt process, normal equations

**Intended learning outcomes (ILOs):**

1.  Describe the disadvantages of least squares polynomial approximation

2.  Define linear independent functions

3.  Define weight function

4.  Outline the uses of weight functions in least squares approximation

5.  Define orthogonal and orthonormal set of functions
    $\int_{a}^b w(x) \phi_k(x)\phi_j(x)  = \left\{ \begin{array}{ll}
     0,&\;\;\;\;\;j \neq k \\
     \alpha_j > 0,&\;\;\;\;\;j = k 
    \end{array}  \right.$

6.  Derive normal equations for least squares approximation using
    orthogonal functions with weight function $f(x)$.
    $\int_a^b w(x)f(x)\phi_j(x) dx = a_j \int_a^b w(x) \phi_j^2(x) dx,\;\; \text{where}\;\;
    a_j = \frac{1}{\alpha_j}\int_{a}^b w(x)f(x) \phi_j(x) dx$

7.  Use the Gram-Schmidt process to construct orthogonal polynomials
    with respect to a weight function $w(x)$.\
    The set of polynomials $\{\phi_0,\phi_1,\ldots,\phi_n \}$ defined in
    the following way, is orthogonal on $[a,b]$ with respect to the
    weight function $w(x)$.  $$\begin{aligned}
    \phi_0(x) &= 1,\;\;\; \phi_1(x) = x - B_1,\;\;
     B_1 = \frac{\displaystyle{\int_a^b x w(x) \phi_0^2~dx }}{\displaystyle{\int_a^b w(x) \phi_0^2~dx}},\\
    \phi_k & = (x-B_k)\phi_{k-1} - C_k\phi_{k-2},\;\;\;\text{when}\;\; k \geq 2, \\
       B_k & = \frac{\displaystyle{\int_a^b x w(x) \phi_{k-1}^2~dx }}{\displaystyle{\int_a^b w(x) \phi_{k-1}^2~dx}},\;\;C_k  = \frac{\displaystyle{\int_a^b x w(x) \phi_{k-1}\phi_{k-2}~dx }}{\displaystyle{\int_a^b w(x) \phi_{k-2}^2~dx}}\end{aligned}$$

8.  Use orthogonal polynomials in least squares approximation of
    functions.

## Practice Problems 

1.  Use the Gram-Schmidt process to construct
    $\phi_0(x), \phi_1(x), \phi_2(x)$ and $\phi_3(x)$ for the following
    intervals

    (a)   \[0,1\]                    (b)   \[0,2\]                     (c)   \[1,3\]

2.  Use the results from 1. above to find the least squares polynomials
    of degree two that approximates the following functions on the given
    intervals.

    1.  $f(x) = x^2 + 3x + 2,\;\;\;\;\;\;[0,1]$

    2.  $f(x) = e^x,\;\;\;\;\;\;\;\;\;\;[0,2]$

    3.  $f(x) = \frac{1}{x},\;\;\;\;\;\;\;\;\;[1,3]$

    4.  $f(x) = x\ln(x),\;\;\;\;\;\;\;\;\;[1,3]$

3.  Use the Gram-Schmidt process to calculate $L_1, L_2, L_3$, where
    $\{L_0(x), L_1(x), L_2(x), L_3(x)\}$ is an orthogonal set of
    polynomials on $(0,\infty)$ with respect to the weight functions
    $w(x) = e^{-x}$ and $L_0(x) = 1$. The polynomials obtained from this
    procedure are called the Laguerre polynomials.

4.  Use the Laguerre polynomials calculated above to compute the least
    squares polynomials of degree one, two and three on the interval
    $(0,\infty)$ with respect to the weight function $w(x) = e^{-x}$ for
    the following functions

    (a)   $f(x) = x^2$             (b)   $f(x) = e^{-x}$            (c)   $f(x) = x^3$

5.  Use the Gram-Schmidt procedure to calculate $L_1,L_2$ and $L_3$
    where $\{L_0,L_1,L_2,L_3\}$ is an orthogonal set of polynomials on
    $(0,\infty)$ with respect to the weight function $w(x) = e^{-x}$ and
    $L_0(x) = 1$. Use the above polynomials, known as Laguerre
    polynomials, to compute the least squares polynomial of degree 3 on
    the interval $(0,\infty)$ with respect to the weight function
    $w(x) = e^{-x}$ for the function $e^{-2x}$.

6.  Show that the functions $\phi_n(x) = \cos(nx)$, $n = 0,1,2,\ldots,$
    form an orthogonal family of functions on the interval $[-\pi,\pi]$
    with weight function $w(x) = 1$.

7.  The Legendre polynomials are given by $\phi_0(x) = 1$,
    $\phi_1(x) = x$ and satisfy the recurrence relation
    $\phi_{n+1}(x) = \frac{2n+1}{n+1} x \phi_n(x) - \frac{n}{n+1}\phi_{n-1}(x),\;\;\;\;\text{for}\;\; n \geq  1.$

    1.  Use the recurrence relation to find $\phi_2(x), \phi_3(x)$ and
        $\phi_4(x)$.

    2.  Use Legendre polynomials to prove that the least squares
        approximation of order $2$ for $f(x) = \cos(\pi x)$ on $[-1, 1]$
        is $P_2(x) = \frac{15}{2\pi^2} - \frac{45}{2\pi^2}x^2$

# Chebyshev Polynomials

Chebyshev polynomials are a wonderful family polynomials that are
orthogonal on $[-1,1]$ with respect to the weight function
$w(x) = \frac{1}{\sqrt{1-x^2}}.$

```{admonition} definition
 The set of polynomials defined by
$T_n(x) = \cos[n \arccos x],\;\;\;\; n \geq 0$ on $[-1,1]$ are called
**Chebyshev Polynomials**


The Chebyshev polynomials can be generated using the following recursive
relation
```

To derive the recurrence formula we first note that
$T_0(x) = \cos 0 = 1,\;\;\;\;\text{and}\;\;\; T_1(x) = \cos(\arccos x) = x.$
If we set $\theta = \arccos x$, then  \begin{aligned}
T_n(x)& = \cos(n\theta),\;\;\;\;\text{where}\;\; \theta \in [0,\pi]\\
T_{n+1}(x)& = \cos[(n+1)\theta] = \cos \theta \cos(n\theta ) - \sin \theta \sin(n\theta)\\
T_{n-1}(x)& = \cos[(n-1)\theta] = \cos \theta \cos(n\theta ) + \sin \theta \sin(n\theta).\end{aligned}
Adding the last two equations gives
$T_{n+1}(x) + T_{n-1}(x) = 2\cos(n\theta)\cos \theta.$ Substituting
back the variable $\theta = \arccos x$ gives  \begin{aligned}
T_{n+1}(x)& = 2x\cos(n\arccos x) - T_{n-1}(x)\\
          & = 2xT_{n}(x) - T_{n-1}(x).\end{aligned}

Using the recurrence formula, successive Chebyshev polynomials can be
obtained as follows:  $$\begin{aligned}
n &= 1;\;\;\; T_{2}(x) = 2xT_1 - T_0 = 2x^2 - 1,\\
n &= 2;\;\;\; T_{3}(x) = 2xT_2 - T_1 = 2x(2x^2 - 1)-x = 4x^3-3x,\\
n &= 3;\;\;\; T_{4}(x) = 2xT_3 - T_2 = 2x(4x^3-3x)-(2x^2 - 1) = 8x^4-8x^2+1,\end{aligned}$$
and so on.

Note that

1.  $T_n(x)$ is always a polynomial of degree $n$ with leading
    coefficients $2^{n-1}$

2.  If $n$ is odd, $T_n(x)$ is an odd function

3.  If $n$ is even, $T_n(x)$ is an even function

We now show that the Chebyshev polynomials are orthogonal with respect
to the weight function
$w(x) = \frac{1}{\sqrt{1-x^2}}\;\;\;\;\; \text{in the interval }[-1,1]$

 center


To prove the orthogonality property, we first consider the case when
$m \neq n$. Using the fact that $T_n(x) = \cos(n\arccos(x))$ and
$T_m(x) = \cos(m\arccos(x))$, then,

$\int_{-1}^{1}\frac{T_m(x)T_n(x)}{\sqrt{1-x^2}}dx = \int_{-1}^{1}\frac{ \cos(m\arccos(x))\cos(n\arccos(x))}{\sqrt{1-x^2}}dx$
Let $\theta = \arccos(x)$, then $\cos(\theta) = x$ and hence $dx =
-\sin(\theta)d\theta = -\sqrt{1 - x^2}d\theta$. Note that $x = -1$
corresponds to $\theta = \pi$ and $x = 1$ corresponds to $\theta =
0$.

$d\theta = -\frac{dx}{\sqrt{1 - x^2}}$ Then

$\int_{-1}^{1}\frac{T_m(x)T_n(x)}{\sqrt{1-x^2}}dx =
    -\int_{\pi}^{0}\cos(n\theta)\cos(m\theta)d\theta = \int_{0}^{\pi}\cos(n\theta)\cos(m\theta)d\theta$

When $m \neq n$, we have $\cos(n\theta)\cos(m\theta) =
\frac{\cos((n+m)\theta) + \cos((n-m)\theta)}{2}$ Therefore, we have
$
 \begin{aligned}
\int_{-1}^{1}\frac{T_m(x)T_n(x)}{\sqrt{1-x^2}}dx &=
\int_{0}^{\pi}\cos(n\theta)\cos(m\theta)d\theta\\
&=\int_{0}^{\pi}\frac{\cos((n+m)\theta) + \cos((n-m)\theta)}{2}\\
&=\int_{0}^{\pi}\frac{\cos((n+m)\theta)}{2} + \int_{0}^{\pi}\frac{\cos((n-m)\theta)}{2}\\
&=\left.\frac{\sin((n+m)\theta)}{2(n+m)}
+\frac{\sin((n-m)\theta)}{2(n-m)}\right|_{0}^{\pi}\\
&=\frac{\sin((n+m)\pi)}{2(n+m)} +\frac{\sin((n-m)\pi)}{2(n-m)}=0\end{aligned}
$
Note that $m$ and $n$ are both integers, so the sum and difference of
$m$ and $n$ are integers too. We can therefore conclude that
$\sin((n+m)\pi) = \sin((n-m)\pi) = 0$.

When $m = n$, we have
$
 \begin{aligned}
    \int_{-1}^{1}\frac{T_n(x)T_n(x)}{\sqrt{1-x^2}}dx
    &=\int_{-1}^{1}\frac{[T_n(x)]^2}{\sqrt{1-x^2}}dx\\
    &=-\int_{\pi}^{0}\cos^2(n\theta)d\theta = \int_{0}^{\pi}\cos^2(n\theta)d\theta\end{aligned}
$
Note that $\cos^2(n\theta) =
\frac{\cos(2n\theta) + 1}{2}$ and hence
$
 \begin{aligned}
    \int_{-1}^{1}\frac{T_n(x)T_n(x)}{\sqrt{1-x^2}}dx
    &= \int_{0}^{\pi}\cos^2(n\theta)d\theta\\
    &= \int_{0}^{\pi}\frac{\cos(2n\theta) + 1}{2}\\
    &= \left.\frac{\sin(2n\theta)}{4n} + \frac{\theta}{2}\right|_{0}^{\pi} =\frac{\pi}{2}\end{aligned}
$
When $m = n = 0$, we have
$
 \begin{aligned}
    \int_{-1}^{1}\frac{T_0(x)T_0(x)}{\sqrt{1-x^2}}dx
    &=\int_{-1}^{1}\frac{[T_0(x)]^2}{\sqrt{1-x^2}}dx\\
    &=\int_{-1}^{1}\frac{dx}{\sqrt{1-x^2}} =\int_{0}^{\pi}d\theta = \pi
\end{aligned}
$

The next theorem concerns the zeros and extreme points of $T_n(x)$.

 theorem
. The Chebyshev polynomials $T_n(x)$ of degree $n \geq 1$ has the
following properties:

1.  $T_n(x)$ has simple roots in $[-1,1]$ at
    $\bar{x}_k = \cos\left(\frac{2k-1}{2n}\pi \right),\;\;\;\;\text{for each}\;\;k = 1,2,\ldots,n$

$T_n(x)$ assumes an absolute extrema at
$\tilde{x} = \cos \left( \frac{\pi k}{n}\right)\;\;\;\;\text{with}\;\; T_n(\tilde{x}_k) = (-1)^k,\;\;\text{for each}\;\; k = 0,1,\ldots,n$


 proof
*Proof.* Let $T_n(x) = \cos (n \arccos x) = \cos n\theta$. The roots are
obtained as
$
 \begin{aligned}
T_n(x) &= \cos n\theta = 0 \Longrightarrow n\theta = (2k-1)\frac{\pi}{2},\;\;\;k = 1,2,3,\ldots \\
\theta & = (2k-1)\frac{\pi}{2n},\\
\arccos x & = (2k-1)\frac{\pi}{2n},\\
 \bar{x}_k & = \cos \left[(2k-1)\frac{\pi}{2n} \right],\;\; k = 1,2,\ldots,n\end{aligned}
$
are the zeros in $[-1,1]$.

To prove the second results, we find the derivative of $T_n(x)$ and
equate it to zero as follows:
$
 \begin{aligned}
\frac{dT_n}{dx}&= \frac{dT_n}{d\theta} \frac{d\theta}{dx} = (-n \sin n\theta)\left(- \frac{1}{\sqrt{1-x^2}}\right) = 0,\\
\therefore \sin n\theta & = 0,\Longrightarrow  n \theta = k \pi,\;\;\; k = 1,2,\ldots,n-1,\\
 \arccos x & = \frac{k \pi}{n}\\
 \tilde{x}_k &= \cos\left( \frac{k \pi}{n}\right)\end{aligned}
 $
 Note
that $T_n(x)$ has degree $n$, thus $\displaystyle \frac{dT_n}{dx}$ has
degree $n-1$. Other possibilities for extrema of $T_n(x)$ occur at the
end points $[-1,1]$. That is at $\tilde{x}_0 = 1$ and
$\tilde{x}_n = -1$. Thus, for only $k = 0,1,2,\ldots,n$, we have
$
 \begin{aligned}
T_n(\tilde{x}_k)&= \cos[n \arccos \tilde{x}_k]\\
 & = \cos\left[n \arccos \cos\left( \frac{k \pi}{n}\right) \right]
 & = \cos k \pi = (-1)^k\end{aligned}
 $
  Thus,
$T_n(\tilde{x}_k) = (-1)^k$. ◻


## Least Squares Approximation using Chebyshev Polynomials

Like any orthogonal set of polynomials, the Chebyshev polynomials can be
used to find least squares approximations of functions $f(x)$. Recall,
the that if $\{\phi_0,\phi_1,\ldots,\phi_n\}$ is an orthogonal set of
functions on an interval $[a,b]$ with respect to the weight function
$w(x)$, then the least squares approximation to $f(x)$ on $[a,b]$ with
respect to $w(x)$ is $P_n(x) = \sum_{j = 0}^{n}a_j\phi_j(x)$ where,
for each $j = 0,1,\ldots,n$,
$\alpha_j = \frac{\int_a^bw(x)\phi_j(x)f(x)~dx}{\int_a^b w(x)[\phi_j(x)]^2} = \frac{1}{\alpha_j}\int_a^b w(x)\phi_j(x)f(x)~dx$

Thus, for Chebyshev polynomials, we set $w(x) = \frac{1}{\sqrt{1-x^2}}$,
$\phi_j(x) = T_j(x)$ and $[a,b] = [-1,1]$. Then, using the orthogonal
property of Chebyshev polynomials, it can be seen that  \begin{aligned}
\alpha_0& = \int_{-1}^{1}\frac{T_0^2(x)}{\sqrt{1-x^2}}~dx = \pi,\\
\alpha_j& = \int_{-1}^{1}\frac{T_j^2(x)}{\sqrt{1-x^2}}~dx = \frac{\pi}{2},\;\;\;\;j = 1,2,\ldots,n\end{aligned}
Thus, we obtain the following formula the least squares approximation
using Chebyshev polynomials

 center


 example
Find a **quadratic** least-squares approximation of $f(x) = x^4$ using
Chebyshev polynomials.

**Solution:** We want to find
$P_2(x) = a_0T_0(x) + a_1T_1(x) + a_2T_2(x)$ where

$
 \begin{aligned}
a_0& = \frac{1}{\pi}\int_{-1}^1 \frac{x^4}{\sqrt{1-x^2}}~dx = \frac{3}{8}\\
a_1& = \frac{2}{\pi}\int_{-1}^1 x\frac{x^4}{\sqrt{1-x^2}}~dx = 0\\
a_2& = \frac{2}{\pi}\int_{-1}^1 (2x^2-1)\frac{x^4}{\sqrt{1-x^2}}~dx = \frac{1}{2}\end{aligned}
$
Thus,
$P_2(x) = \frac{3}{8} + \frac{1}{2}(2x^2 - 1)  = x^2  - \frac{1}{8}$

The figure below, shows a comparison between $f(x) = x^4$ and $P_2(x)$.

![Comparison between $f(x) = x^4$ and
$P_2(x)$](Othogonalcheb.eps){#figorthogonalcheb}


# Trigonometric Polynomial Approximation

It can be observed that for each integer $n > 0$, the set
$\{\phi_0,\phi_1,\ldots,\phi_{2n-1} \}$, where  \begin{aligned}
\phi_0(x) &= \frac{1}{2},\\
\phi_k(x) &= \cos kx,\;\;\;\;\;\;\;\text{for each}\;\; k = 1,2,\ldots,n\\
\phi_{n+k}(x) &= \sin kx,\;\;\;\;\;\;\text{for each}\;\; k = 1,2,\ldots,n-1\end{aligned}
is orthogonal on $[-\pi,\pi]$ with respect to the weight $w(x) = 1$. The
orthogonality follows from the fact that for every integer $j$, the
integrals of $\sin jx$ and $\cos jx$ over $[-\pi,\pi]$ are 0, and the
products involving sine and cosine can be written as sums using the
following trigonometric identities
$
 \begin{aligned}
\sin \theta_1 \sin \theta_2 & = \frac{1}{2}[\cos(\theta_1 - \theta_2) - \cos(\theta_1 +\theta_2)],\\
\cos \theta_1 \cos \theta_2 & = \frac{1}{2}[\cos(\theta_1 - \theta_2) + \cos(\theta_1 + \theta_2)],\\
\sin \theta_1 \cos \theta_2 & = \frac{1}{2}[\sin(\theta_1 - \theta_2) + \sin(\theta_1 +\theta_2)]\end{aligned}
$
 center


 example
Determine the trigonometric polynomial from $S_n$ that approximates
$f(x) = |x|,;\;\;\;\;\;\text{for}\;\; -\pi < x < \pi$

**Solution:** We first determine the coefficients 
$
 \begin{aligned}
a_0& = \frac{1}{\pi} \int_{-\pi}^{\pi} |x|~dx  = -\frac{1}{\pi} \int_{-\pi}^0 x~dx + \frac{1}{\pi}\int_{0}^{\pi} x~dx = \frac{2}{\pi}\int_{0}^{\pi}x~dx = \pi,\\
a_k& = \frac{1}{\pi}\int_{-\pi}^{\pi}|x|\cos kx~dx = \frac{2}{\pi}\int_{0}^{\pi} x\cos kx~dx = \frac{2}{\pi k^2}[(-1)^k - 1],\end{aligned}
$
for each $k = 1,2,\ldots,n$ and
$b_k = \frac{1}{\pi}\int_{-\pi}^{\pi}|x|\sin kx~dx = 0,\;\;\;\;\text{for each}\;\;k=1,2,\ldots,n-1$
The trigonometric polynomial that approximates $f(x) = |x|$ is
$S_n(x) = \frac{\pi}{2} + \frac{2}{\pi}\sum_{k=1}^n \frac{(-1)^k - 1}{k^2}\cos kx$
Setting $n = 1$ and $n = 3$ gives

$S_1(x) = \frac{\pi}{2}  - \frac{4}{\pi}\cos x,\;\;\; S_3(x) = \frac{\pi}{2} - \frac{4}{\pi}\cos x - \frac{4}{9\pi}\cos 3x$
Figure [4](#triglsa1){reference-type="ref" reference="triglsa1"} shows a
comparison between $f(x)$ and $S_1(x)$ and $S_3(x)$

![Comparison between $f(x) = |x|$ and $S_1(x)$ and
$S_3(x)$](triglsa1.eps){#triglsa1}


 example
Let $f(x)$ be a function of period $2\pi$ such that
$\displaystyle{ f(x) = \left\{\begin{array}{cc}
~1~ , &~~~ -\pi < x < 0\\
~0~ , &~~~~ 0 < x < \pi.
\end{array} \right. }$

1.  Show that the least squares trigonometric polynomial that
    approximates $f(x)$ in the interval $-\pi < x < \pi$ is
     $
     \begin{aligned}
     S_n(x)& =  \frac{1}{2} + \sum_{k = 1}^{n}\frac{1}{k\pi} \left[(-1)^k - 1 \right]\sin k x  \\ 
     &=  \frac{1}{2} - \frac{2}{\pi}\left[ \sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x + \ldots + \frac{1}{(2n-1)}\sin[(2n-1)x] \right]\end{aligned}
     $
    for $n = 1,2,\ldots$

2.  By giving an appropriate value to $x$, show that as
    $n \rightarrow \infty$.

    $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots$

**Solution:** The coefficients are defined as

1.  $ \begin{aligned}
    a_0 & = \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)~dx =\frac{1}{\pi}\int_{-\pi}^{0} 1~dx + \frac{1}{\pi}\int_{0}^{\pi}0~dx \\
        & = \frac{1}{\pi}\int_{-\pi}^{0}~dx = \left.\frac{1}{\pi} ~ x \right|_{-\pi}^{0} = 1 \end{aligned}$

    $
     \begin{aligned}
    a_k & = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(kx)~dx\\
        & = \frac{1}{\pi}\int_{-\pi}^{0}\cos(kx)~dx + \frac{1}{\pi}\int_{0}^{\pi}0\cdot \cos(kx)~dx \\
        & = \frac{1}{\pi}\int_{-\pi}^{0}\cos(kx)~dx = \left.\frac{1}{\pi k} \sin(kx)\right|_{-\pi}^{0} = 0.\end{aligned}
    $
     $
     \begin{aligned}
    b_k & = \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(kx)~dx,\\
        & = \frac{1}{\pi}\int_{-\pi}^{0}\sin(kx)~dx  + \frac{1}{\pi}\int_{0}^{\pi}0\cdot\sin(kx)~dx \\  
        & = \frac{1}{\pi}\int_{-\pi}^{0}\sin(kx)~dx  = \left. -\frac{\cos(kx)}{\pi k}\right|_{-\pi}^{0} \\
        & = -\frac{1}{\pi k}[1 - \cos(k\pi)] = \frac{1}{\pi k}[\cos(k\pi)-1] = \frac{1}{k\pi}\left[(-1)^k - 1\right]\end{aligned}$
    Thus,  $\begin{aligned}
    S_n(x)& = \frac{1}{2} + \sum_{k = 1}^{n-1}\frac{1}{k\pi} \left[(-1)^k - 1 \right]\sin k x,\\\end{aligned}$

2.  Suppose that
    $\displaystyle \lim_{n \rightarrow \infty} S_n(x) = S(x)$.
    $S(x) =\frac{1}{2} - \frac{2}{\pi}\left[\sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x + \frac{1}{7}\sin 7x + \ldots \right]$
    Set $x = \frac{\pi}{2}$ in $S(x)$. Note that when
    $x = \frac{\pi}{2}$, $f(x) = 0$, thus

    $ \begin{aligned}
    0 & = \frac{1}{2} - \frac{2}{\pi}\left[\sin\frac{\pi}{2} + \frac{1}{3}\sin\frac{3\pi}{2} + \frac{1}{5}\sin \frac{5\pi}{2} + \frac{1}{7}\sin \frac{7\pi}{2} + \ldots \right]\\
    0 & = \frac{1}{2} - \frac{2}{\pi}\left[1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots \right]\\
    \frac{\pi}{4}&=1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots  \end{aligned}$

```{note}

1.  If $f(x)$ is continuous at $x = a$, and the series
    $S_{\infty} = S(x)$ approximates $f(x)$, then $f(a) = S(a)$.

2.  If $f(x)$ is discontinuous at $x = a$, then the series converges to
    a value that is halfway between the two possible values that is
    $S(a) = \frac{1}{2}(f(a^{-} + a^{+}))$
```

# Summary: Least Squares Approximation using Trigonometric polynomials 

**Keywords:**Orthogonal trigonometric functions, Fourier Series

**Intended learning outcomes (ILOs):**

1.  Prove that the set
    $\mathcal{T}_n(x) = \left\{\phi_0, \phi_1,\ldots, \phi_{2n-1} \right\}$
    with
    $\phi_0 = \frac{1}{2},\;\;  \phi_k(x) = \cos(k x), k = 0,1,\ldots,n,\;\; \phi_{k+n}(x) = \sin(k x),\;\;k = 1,2,\ldots,n-1$
    is orthogonal on $[-\pi,\pi]$ with respect to $w(x) = 1$.

2.  Describe the continuous least squares approximation using
    trigonometric polynomial functions  $\begin{aligned}
     S_n(x)&= \frac{a_0}{2} + a_n \cos (n x) + \sum_{k=1}^{n-1} \left[ a_k \cos (kx) + b_k \sin(kx)\right],\\
       a_k &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos (kx)~dx,\;\;\;k = 0,1,\ldots,n,\\
       b_k &= \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin (kx)~dx,\;\;\;k = 1,2,\ldots,n-1,\\
     \end{aligned}$

3.  Describe how the Fourier series of a function $f(x)$ is obtained
    from the continuous least squares approximation using
    $\mathcal{T}_n(x)$

4.  Apply the trigonometric polynomial least squares approximation to
    approximate a given function.

5.  *Compare approximate solution obtained using trigonometric
    polynomial least squares approximation with the exact value of the
    function (Matlab exercise)*

# Practice Problems

1.  Find the continuous least squares trigonometric polynomial $S_3(x)$
    for $f(x) = x$ on $[-\pi,\pi]$.

2.  Find the continuous least-squares trigonometric polynomial $S_2(x)$
    for $f(x) = x^2$ on $[-\pi,\pi]$.

3.  Find the general general continuous least-squares trigonometric
    polynomial $S_n(x)$ for the following functions on the interval
    $[-\pi,\pi]$

    1.  $f(x) = \left\{\begin{array}{rl}
        -1,&\;\;\; \text{if},\;\; -\pi < x < 0,\\
        1,&\;\;\;  \text{if},\;\; 0 \leq x \leq \pi.
        \end{array} \right.$

    2.  $f(x) = \left\{\begin{array}{rl}
        0,&\;\;\; \text{if},\;\; -\pi < x < 0,\\
        1,&\;\;\;  \text{if},\;\; 0 \leq x \leq \pi.
        \end{array} \right.$

    3.  $\displaystyle{ f(x) = \left\{\begin{array}{cc}
        0~ , &~~~ -\pi < x < 0\\
        x~ , &~~~~~~  0 < x < \pi
        \end{array} \right. }$

    4.  $\displaystyle{ f(x) = 1 + x }$           on $[-\pi,\pi]$ with
        period $2\pi$

4.  Let $f(x)$ be a function of period $2\pi$ such that
    $\displaystyle{ f(x) = \left\{\begin{array}{cc}
    ~1~ , &~~~ -\pi < x < 0\\
    ~0~ , &~~~~ 0 < x < \pi.
    \end{array} \right. }$

    1.  Show that the continuous least-squares trigonometric polynomial
        for $f(x)$ in the interval $-\pi < x < \pi$ is
        $S(x) =  \frac{1}{2} - \frac{2}{\pi}\left[ \sin x + \frac{1}{3}\sin 3x + \frac{1}{5}\sin 5x + \ldots \right]$
        as $n \rightarrow \infty$

    2.  By giving an appropriate value to $x$, show that
        $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots$

5.  Let $f(x)$ be a function of period $2\pi$ such that
    $\displaystyle{ f(x) = \left\{\begin{array}{cc}
    ~0~ , &~~~ -\pi < x < 0\\
    ~x~ , &~~~~ 0 < x < \pi.
    \end{array} \right. }$

    1.  Show that the continuous least-squares trigonometric polynomial
        for $f(x)$ in the interval $-\pi < x < \pi$ is  $\begin{aligned}
        S(x) = \frac{\pi}{4} & - \frac{2}{\pi}\left[\cos x + \frac{1}{3^2}\cos 3x + \frac{1}{5^2}\cos 5x + \ldots \right]\\
                       & + \left[\sin x - \frac{1}{2}\sin 2x + \frac{1}{3}\sin 3x - \ldots \right]\end{aligned}$
        as $n \rightarrow \infty$

    2.  By giving an appropriate value to $x$, show that

        1.  $\displaystyle{ \frac{\pi}{4}   = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \ldots}$

        2.  $\displaystyle{\frac{\pi^2}{8} = 1 + \frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} + \ldots}$

6.  Let $f(x)$ be a function of period $2\pi$ such that
    $f(x) = x \;\;\;\;\text{over the interval}\;\; -\pi < x < \pi$

    1.  Show that the Fourier series for $f(x)$ in the interval
        $-\pi < x < \pi$ is
        $S(x) =  2\left[ \sin x - \frac{1}{2}\sin 2x + \frac{1}{3}\sin 3x + \ldots \right]$
        as $n \rightarrow \infty$

    2.  By giving an appropriate value to $x$, show that
        $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} +  \ldots$

7.  Let $f(x)$ be a function of period $2\pi$ such that
    $f(x) = x^2 \;\;\;\;\text{over the interval}\;\; -\pi \leq x \leq \pi$

    1.  Show that the continuous least-squares trigonometric polynomial
        for $f(x)$ in the interval $-\pi \leq x \leq \pi$ is
        $S(x) = \frac{\pi^2}{3} - 4\left[ \cos x - \frac{1}{2^2}\cos 2x + \frac{1}{3^2}\cos 3x  -  \ldots \right]$
        as $n \rightarrow \infty$

    2.  By giving an appropriate value to $x$, show that
        $\frac{\pi^2}{6} = 1 + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \ldots$

# Answers 

1.  $S_3(x) = 2\sin x - \sin 2x$

2.  $S_2(x) = \frac{\pi^2}{3} - 4\cos x + \cos 2x$

3.  1.  $\displaystyle{S_n(x) = \frac{2}{\pi} \sum_{k=1}^{n-1} \left(\frac{1 - (-1)^k}{k} \right)\sin(kx)}$

    2.  $\displaystyle{S_n(x) = \frac{1}{2} +  \frac{1}{\pi} \sum_{k=1}^{n-1} \left(\frac{1 - (-1)^k}{k} \right)\sin(kx)}$

    3.  $\displaystyle{ \frac{\pi}{4} + \sum_{k=1}^{n} \frac{(-1)^k - 1}{\pi k^2}\cos k x  + \sum_{k=1}^{n-1}+\frac{(-1)^{k+1}}{k}\sin kx}$

    4.  $\displaystyle{1  + \sum_{k = 1}^{n-1} \frac{2(-1)^{k+1}}{k} \sin k x}$
