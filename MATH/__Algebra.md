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

# Matrices & Vectors Operations
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


Here is the polished version of the text. I have also corrected a subtle but important mathematical distinction in your introductory paragraph: for matrix multiplication to be possible, the number of **columns** in the left matrix must match the number of **rows** in the right matrix (which ensures that the *length* of the left matrix's rows matches the *length* of the right matrix's columns).

The example has been completely updated to feature a left matrix with 2 rows and 3 columns, and a right matrix with 3 rows and 4 columns.


### Matrix Multiplication

The **dot product of two matrices** (commonly referred to as **matrix multiplication**) produces a new matrix. Each entry $(i, j)$ in the resulting matrix is calculated by taking the dot product of the $i$-th row of the left matrix and the $j$-th column of the right matrix.

For this operation to be valid, the number of columns in the left matrix must equal the number of rows in the right matrix. This ensures that the row from the left matrix and the column from the right matrix have the exact same number of elements.

### Example: Matrix Multiplication

Given a left matrix $A$ (dimensions $2 \times 3$) and a right matrix $B$ (dimensions $3 \times 4$):

$$A =
\begin{bmatrix}
1 & 2 & 0 \\
3 & -1 & 4
\end{bmatrix}
\qquad
B =
\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 1 & -2 & 3 \\
2 & 0 & 1 & 1
\end{bmatrix}$$

Their product $AB$ will be a $2 \times 4$ matrix, calculated as follows:

$$AB =
\begin{bmatrix}
(1\cdot1 + 2\cdot0 + 0\cdot2) & (1\cdot2 + 2\cdot1 + 0\cdot0) & (1\cdot3 + 2\cdot(-2) + 0\cdot1) & (1\cdot4 + 2\cdot3 + 0\cdot1) \\
(3\cdot1 + (-1)\cdot0 + 4\cdot2) & (3\cdot2 + (-1)\cdot1 + 4\cdot0) & (3\cdot3 + (-1)\cdot(-2) + 4\cdot1) & (3\cdot4 + (-1)\cdot3 + 4\cdot1)
\end{bmatrix}=\begin{bmatrix}
1 & 4 & -1 & 10 \\
11 & 5 & 15 & 13
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




# Eigenvalues and Eigenvectors of Symmetric Matrices

## Rules

**Eigenvalues of symmetric matrix:** The eigenvalues of a real symmetric matrix (and by extension, a complex Hermitian matrix) are always strictly real numbers, even if we allow for complex vectors and scalars during the derivation.
<details>
<summary><B>Proof</B></summary>

> Let $A$ be an $n \times n$ real symmetric matrix ($A = A^T$), and let $\lambda$ be an eigenvalue with its corresponding non-zero eigenvector $\mathbf{x}$, such that:
> 
> $$A\mathbf{x} = \lambda\mathbf{x}$$
> 
> 
> Taking the conjugate transpose (Hermitian conjugate, denoted by $\dagger$) of both sides gives:
> 
> $$(\lambda\mathbf{x})^\dagger = (A\mathbf{x})^\dagger \implies \bar{\lambda}\mathbf{x}^\dagger = \mathbf{x}^\dagger A^\dagger$$
> 
> 
> Since $A$ is a real symmetric matrix, its conjugate transpose is simply its transpose, meaning $A^\dagger = A^T = A$. Substituting this back yields:
> 
> $$\mathbf{x}^\dagger A = \bar{\lambda}\mathbf{x}^\dagger$$
> 
> 
> Now, we create a matching quadratic form by multiplying our two primary equations:
> * Multiply $A\mathbf{x} = \lambda\mathbf{x}$ from the left by $\mathbf{x}^\dagger$:
> 
> $$\mathbf{x}^\dagger A\mathbf{x} = \lambda(\mathbf{x}^\dagger\mathbf{x})$$
> 
> 
> * Multiply $\mathbf{x}^\dagger A = \bar{\lambda}\mathbf{x}^\dagger$ from the right by $\mathbf{x}$:
> 
> $$\mathbf{x}^\dagger A\mathbf{x} = \bar{\lambda}(\mathbf{x}^\dagger\mathbf{x})$$
> 
> 
> 
> 
> Equating the two expressions for $\mathbf{x}^\dagger A\mathbf{x}$ gives:
> 
> $$\lambda(\mathbf{x}^\dagger\mathbf{x}) = \bar{\lambda}(\mathbf{x}^\dagger\mathbf{x}) \implies (\lambda - \bar{\lambda})(\mathbf{x}^\dagger\mathbf{x}) = 0$$
> 
> 
> Since $\mathbf{x}$ is a non-zero eigenvector, its squared norm $\mathbf{x}^\dagger\mathbf{x}$ must be strictly greater than zero ($\mathbf{x}^\dagger\mathbf{x} > 0$). Therefore, the scalar term must vanish:
> 
> $$\lambda - \bar{\lambda} = 0 \implies \lambda = \bar{\lambda}$$
> 
> 
> Because $\lambda$ is equal to its own complex conjugate, $\lambda$ must be a real number. $\blacksquare$

</details><br>



**Eigen vectors of a symmetric matrix:** The eigenvectors of a symmetric matrix corresponding to distinct (non-repeated) eigenvalues are always orthogonal to one another.

<details>
<summary><B>Proof</B></summary>

> Let $A$ be a real symmetric matrix ($A = A^T$). Suppose $\lambda_1$ and $\lambda_2$ are two distinct eigenvalues ($\lambda_1 \neq \lambda_2$) with corresponding real eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$. This gives us:
> 1. $A\mathbf{v}_1 = \lambda_1\mathbf{v}_1$
> 2. $A\mathbf{v}_2 = \lambda_2\mathbf{v}_2$
> 
> 
> Consider the scalar quantity $\mathbf{v}_1^T A \mathbf{v}_2$. We can evaluate this in two different ways by associating the matrix multiplication either to the right or to the left:
> * **Evaluating to the right:**
> 
> $$\mathbf{v}_1^T (A \mathbf{v}_2) = \mathbf{v}_1^T (\lambda_2 \mathbf{v}_2) = \lambda_2 (\mathbf{v}_1^T \mathbf{v}_2)$$
> 
> 
> * **Evaluating to the left:**
> Using the property $(A\mathbf{v}_1)^T = \mathbf{v}_1^T A^T$, and knowing $A^T = A$ due to symmetry:
> 
> $$(\mathbf{v}_1^T A) \mathbf{v}_2 = (A \mathbf{v}_1)^T \mathbf{v}_2 = (\lambda_1 \mathbf{v}_1)^T \mathbf{v}_2 = \lambda_1 (\mathbf{v}_1^T \mathbf{v}_2)$$
> 
> 
> 
> 
> Equating the two results:
> 
> $$\lambda_1 (\mathbf{v}_1^T \mathbf{v}_2) = \lambda_2 (\mathbf{v}_1^T \mathbf{v}_2) \implies (\lambda_1 - \lambda_2)(\mathbf{v}_1^T \mathbf{v}_2) = 0$$
> 
> 
> By our initial assumption, the eigenvalues are distinct, meaning $\lambda_1 - \lambda_2 \neq 0$. Consequently, the dot product must be zero:
> 
> $$\mathbf{v}_1^T \mathbf{v}_2 = 0$$
> 
> 
> This proves that the eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are orthogonal. $\blacksquare$

</details><br>