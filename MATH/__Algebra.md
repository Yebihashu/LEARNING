# Matrices
A matrix is a rectangular grid (or table) of numbers arranged in rows and columns. Matrices are typically denoted by uppercase letters (e.g., $A$).

## Matrix Dimensions (Size)
In this document, the dimensions of a matrix are defined as:
$$(H, W)$$
Where:
* **$H$** represents the number of rows (height).
* **$W$** represents the number of columns (width).

For example, a matrix with 3 rows and 5 columns has a size of $(3, 5)$.

Here is the polished and refined version of this section, maintaining continuity with the previous edits and correcting the spelling mistakes (like "modificaiton").


# Vectors

A **vector** is a special case of a matrix that consists of only a single row or a single column.

Throughout this document, standard vectors are assumed to be **column vectors** and are denoted by a lowercase letter (e.g., $\mathbf{v}$). A row vector is treated as a column vector that has been oriented horizontally. This modification is called a **transpose**, which is denoted by the superscript $T$ (e.g., $\mathbf{v}^T$).

> **Note on Convention**
> Vectors can be represented as either rows or columns depending on the convention being used. Although this choice affects the notation of certain operations, both approaches are mathematically equivalent. In this document, vectors default to **column vectors**, and row vectors are explicitly represented using the **transpose operation**.

# Vectors and Matrix Operations
The theory of vectors and matrices was developed and formalized during the 19th century by mathematicians and physicists. Numerous definitions and notations were proposed, leading to extensive discussion regarding which operations should become part of the standard framework. These operations were judged according to their mathematical significance, their effectiveness in describing physical phenomena, and their simplicity and usefulness in practical applications.

## Transpose

The **transpose** of a matrix is obtained by swapping its rows and columns. In other words, each row of the original matrix becomes a column in the transposed matrix, and each column becomes a row.

The transpose of a matrix \(A\) is denoted by:

$$
A^T
$$

### Example: Matrix Transpose

Given the matrix

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

its transpose is

$$
A^T =
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
$$

### Example: Vector Transpose

A vector is commonly represented as a column matrix:

$$
v =
\begin{bmatrix}
1 \\
2 \\
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

Here is the polished and corrected version for the Matrix Sum section, complete with a clear explanation and a formatted mathematical example.

---

## Matrix Addition (Matrix Sum)

The **sum of two matrices** is calculated by adding their corresponding elements. Because elements are added one-by-one, matrix addition is only defined for matrices that have the exact same dimensions (the same number of rows and columns).


### Example: Matrix Addition

Given two matrices $A$ and $B$ of the same size:

$$A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}$$

Their sum $A + B$ is:

$$A + B =
\begin{bmatrix}
1 + 5 & 2 + 6 \\
3 + 7 & 4 + 8
\end{bmatrix}
=
\begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}$$


## Dot Product (Matrix Multiplication)

### The Fundamental Operation: Row-by-Column Multiplication

The elementary building block of matrix multiplication is the dot product between a row vector and a column vector.

For a row and a column of the same size, their dot product is defined as the sum of the products of their corresponding elements.

**Example:**
Given a row vector $R = \begin{bmatrix} a & b \end{bmatrix}$ and a column vector $C = \begin{bmatrix} x \\ y \end{bmatrix}$, their dot product is:


$$R \cdot C = a \cdot x + b \cdot y$$

> **Key Rules:**
> 1. **Orientation:** The dot product is always calculated between a row vector on the left and a column vector on the right.
> 2. **Dimension Matching:** The row and the column must contain the exact same number of elements.
> 3. **Scalar:** The result of a row-column dot product is always a **scalar** (a single number), not a vector.


### Matrix Multiplication

The **dot product of two matrices** (commonly referred to as **matrix multiplication**) produces a new matrix. Each entry $(i, j)$ in the resulting matrix is calculated by taking the dot product of the $i$-th row of the left matrix and the $j$-th column of the right matrix.


### Example: Matrix Multiplication

Given the matrices:

$$A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}$$

Their product $AB$ is calculated as:

$$AB =
\begin{bmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{bmatrix}
=
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}$$


### Example: Dot Product of Two Vectors

Given two column vectors:

$$\mathbf{v}_1 =
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
\qquad
\mathbf{v}_2 =
\begin{bmatrix}
4 \\
5 \\
6
\end{bmatrix}$$

To multiply them using matrix notation, we transpose the first vector to turn it into a row vector:

$$\mathbf{v}_1^T \mathbf{v}_2
=
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix}
\begin{bmatrix}
4 \\
5 \\
6
\end{bmatrix}
=
1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6
=
32$$

> **Note:** The result of a vectors dot product is always a **scalar** (a single number), not a vector.