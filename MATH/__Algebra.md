# Matrices
A matrix is a rectangular grid (or table) of numbers arranged in rows and columns. Matrices are typically denoted by uppercase letters (e.g., $A$).

## Matrix Dimensions (Size)
In this document, the dimensions of a matrix are defined as:

$$
(H, W)
$$

Where:
* **$H$** represents the number of rows (height).
* **$W$** represents the number of columns (width).

For example, a matrix with 3 rows and 5 columns has a size of $(3, 5)$.

# Vectors

A **vector** is a special case of a matrix that consists of only a single row or a single column.

Throughout this document, standard vectors are assumed to be **column vectors** and are denoted by a lowercase letter (e.g., $\mathbf{v}$). A row vector is treated as a column vector that has been oriented horizontally. This modification is called a **transpose**, which is denoted by the superscript $T$ (e.g., $\mathbf{v}^T$).

> **Note on Convention**
> Vectors can be represented as either rows or columns depending on the convention being used. Although this choice affects the notation of certain operations, both approaches are mathematically equivalent. In this document, vectors default to **column vectors**, and row vectors are explicitly represented using the **transpose operation**.

# Matrices & Vectors Operations
The theory of vectors and matrices was developed and formalized during the 19th century by mathematicians and physicists. Numerous definitions and notations were proposed, leading to extensive discussion regarding which operations should become part of the standard framework. These operations were judged according to their mathematical significance, their effectiveness in describing physical phenomena, and their simplicity and usefulness in practical applications.

## Transpose

The **transpose** of a matrix is obtained by swapping its rows and columns. In other words, each row of the original matrix becomes a column in the transposed matrix, and each column becomes a row.

The transpose of a matrix $A$ is denoted by:

$$
A^T
$$

### Example: Matrix Transpose

Given the matrix

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\\\
4 & 5 & 6
\end{bmatrix}
$$

its transpose is

$$
A^T =
\begin{bmatrix}
1 & 4 \\\\
2 & 5 \\\\
3 & 6
\end{bmatrix}
$$

### Example: Vector Transpose

A vector is commonly represented as a column matrix:

$$
v =
\begin{bmatrix}
1 \\\\
2 \\\\
3
\end{bmatrix}
$$

Its transpose is a row vector:

$$
v^T =
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
$$

The transpose operation allows us to convert between column vectors and row vectors.

## Matrix Addition (Matrix Sum)

The **sum of two matrices** is calculated by adding their corresponding elements. Because elements are added one-by-one, matrix addition is only defined for matrices that have the exact same dimensions (the same number of rows and columns).

### Example: Matrix Addition

Given two matrices $A$ and $B$ of the same size:

$$
A =
\begin{bmatrix}
1 & 2 \\\\
3 & 4
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
5 & 6 \\\\
7 & 8
\end{bmatrix}
$$

Their sum $A + B$ is:

$$
A + B =
\begin{bmatrix}
1 + 5 & 2 + 6 \\\\
3 + 7 & 4 + 8
\end{bmatrix}
=
\begin{bmatrix}
6 & 8 \\\\
10 & 12
\end{bmatrix}
$$

### Rules of matrices addition operation

Matrix addition satisfies the following algebraic properties (for matrices of matching dimensions):

| Property | Rule |
| --- | --- |
| **Closure** | If $A$ and $B$ are $m \times n$ matrices, then $A + B$ is also an $m \times n$ matrix. |
| **Commutative** | $A + B = B + A$ |
| **Associative** | $(A + B) + C = A + (B + C)$ |
| **Identity element** | $A + 0 = 0 + A = A$, where $0$ is the zero matrix. |
| **Additive inverse** | For every $A$, there exists $-A$ such that $A + (-A) = 0$. |
| **Cancellation law** | If $A + C = B + C$, then $A = B$. |



## Dot Product (Matrix Multiplication)

### The Fundamental Operation: Row-by-Column Multiplication

The elementary building block of matrix multiplication is the dot product between a row vector and a column vector.

For a row and a column of the same size, their dot product is defined as the sum of the products of their corresponding elements.

**Example:**
Given a row vector $R = \begin{bmatrix} a & b \end{bmatrix}$ and a column vector $C = \begin{bmatrix} x \\\\ y \end{bmatrix}$, their dot product is:

$$
R \cdot C = a \cdot x + b \cdot y
$$

> **Key Rules:**
> 1. **Orientation:** The dot product is always calculated between a row vector on the left and a column vector on the right.
> 2. **Dimension Matching:** The row and the column must contain the exact same number of elements.
> 3. **Scalar:** The result of a row-column dot product is always a **scalar** (a single number), not a vector.

### Matrix Multiplication

The **dot product of two matrices** (commonly referred to as **matrix multiplication**) produces a new matrix. Each entry $(i, j)$ in the resulting matrix is calculated by taking the dot product of the $i$-th row of the left matrix and the $j$-th column of the right matrix.

For this operation to be valid, the number of columns in the left matrix must equal the number of rows in the right matrix. This ensures that the row from the left matrix and the column from the right matrix have the exact same number of elements.

### Example: Matrix Multiplication

Given a left matrix $A$ (dimensions $2 \times 3$) and a right matrix $B$ (dimensions $3 \times 4$):

$$
A =
\begin{bmatrix}
1 & 2 & 0 \\\\
3 & -1 & 4
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
1 & 2 & 3 & 4 \\\\
0 & 1 & -2 & 3 \\\\
2 & 0 & 1 & 1
\end{bmatrix}
$$

Their product $AB$ will be a $2 \times 4$ matrix, calculated as follows:

$$
AB =
\begin{bmatrix}
(1\cdot1 + 2\cdot0 + 0\cdot2) & (1\cdot2 + 2\cdot1 + 0\cdot0) & (1\cdot3 + 2\cdot(-2) + 0\cdot1) & (1\cdot4 + 2\cdot3 + 0\cdot1) \\\\
(3\cdot1 + (-1)\cdot0 + 4\cdot2) & (3\cdot2 + (-1)\cdot1 + 4\cdot0) & (3\cdot3 + (-1)\cdot(-2) + 4\cdot1) & (3\cdot4 + (-1)\cdot3 + 4\cdot1)
\end{bmatrix}
=
\begin{bmatrix}
1 & 4 & -1 & 10 \\\\
11 & 5 & 15 & 13
\end{bmatrix}
$$

### Example: Dot Product of Two Vectors

Given two column vectors:

$$
\mathbf{v}_1 =
\begin{bmatrix}
1 \\\\
2 \\\\
3
\end{bmatrix}
\qquad
\mathbf{v}_2 =
\begin{bmatrix}
4 \\\\
5 \\\\
6
\end{bmatrix}
$$

To multiply them using matrix notation, we transpose the first vector to turn it into a row vector:

$$
\mathbf{v}_1^T \mathbf{v}_2
=
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\begin{bmatrix}
4 \\\\
5 \\\\
6
\end{bmatrix}
=
1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6
=
32
$$

> **Note:** The result of a vector dot product is always a **scalar** (a single number), not a vector.



### Rules of matrices multiplication operation

Matrix multiplication satisfies the following algebraic properties (when the products are defined):

| Property | Rule |
| --- | --- |
| **Compatibility (defined only when dimensions match)** | If $A$ is $m \times n$ and $B$ is $n \times p$, then $AB$ is defined and has size $m \times p$. |
| **Closure** | If $AB$ is defined, then $AB$ is a matrix. |
| **Associative** | $(AB)C = A(BC)$ |
| **Not commutative (in general)** | $AB \neq BA$ |
| **Left distributive** | $A(B + C) = AB + AC$ |
| **Right distributive** | $(A + B)C = AC + BC$ |
| **Identity element** | $AI = IA = A$, where $I$ is the identity matrix of the appropriate size. |
| **Multiplication by the zero matrix** | $A0 = 0A = 0$, whenever the products are defined. |
| **Associativity with scalar multiplication** | $c(AB) = (cA)B = A(cB)$ |




# Inverse Matrix
If A*B = I, then 
A is inverse matrix of B and B is inverse matrix of A

We sign inverse of matrix by A^-1


## Rules 
if A*B = I,  then B*A=I
proof
A*B = I 
A*B*A = A = A*I = I*A
A*B*A = A*I = A*(B*A) 
A*B*A = I*A = (A*B)*A 


# Investigating 2D matrix

## Scaling & Reflection (about X axis and Y axis) 

## Rotation 

## Scaling + Rotation & Reflection about any direction 

## Shir 


    














