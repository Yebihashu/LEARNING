# Eigenvalues and Eigenvectors of Symmetric Matrices

## Rules

**Eigenvalues of symmetric matrix:** The eigenvalues of a real symmetric matrix (and by extension, a complex Hermitian matrix) are always strictly real numbers, even if we allow for complex vectors and scalars during the derivation.
<details>
<summary><B>Proof</B></summary>

> Let $A$ be an $n \times n$ real symmetric matrix ($A = A^T$), and let $\lambda$ be an eigenvalue with its corresponding non-zero eigenvector $\mathbf{x}$, such that:
>
> $$A\mathbf{x} = \lambda\mathbf{x}$$
>
> Taking the conjugate transpose (Hermitian conjugate, denoted by $\dagger$) of both sides gives:
>
> $$(\lambda\mathbf{x})^\dagger = (A\mathbf{x})^\dagger \implies \bar{\lambda}\mathbf{x}^\dagger = \mathbf{x}^\dagger A^\dagger$$
>
> Since $A$ is a real symmetric matrix, its conjugate transpose is simply its transpose, meaning $A^\dagger = A^T = A$. Substituting this back yields:
>
> $$\mathbf{x}^\dagger A = \bar{\lambda}\mathbf{x}^\dagger$$
>
> Now, we create a matching quadratic form by multiplying our two primary equations:
> * Multiply $A\mathbf{x} = \lambda\mathbf{x}$ from the left by $\mathbf{x}^\dagger$:
>
> $$\mathbf{x}^\dagger A\mathbf{x} = \lambda(\mathbf{x}^\dagger\mathbf{x})$$
>
> * Multiply $\mathbf{x}^\dagger A = \bar{\lambda}\mathbf{x}^\dagger$ from the right by $\mathbf{x}$:
>
> $$\mathbf{x}^\dagger A\mathbf{x} = \bar{\lambda}(\mathbf{x}^\dagger\mathbf{x})$$
>
> Equating the two expressions for $\mathbf{x}^\dagger A\mathbf{x}$ gives:
>
> $$\lambda(\mathbf{x}^\dagger\mathbf{x}) = \bar{\lambda}(\mathbf{x}^\dagger\mathbf{x}) \implies (\lambda - \bar{\lambda})(\mathbf{x}^\dagger\mathbf{x}) = 0$$
>
> Since $\mathbf{x}$ is a non-zero eigenvector, its squared norm $\mathbf{x}^\dagger\mathbf{x}$ must be strictly greater than zero ($\mathbf{x}^\dagger\mathbf{x} > 0$). Therefore, the scalar term must vanish:
>
> $$\lambda - \bar{\lambda} = 0 \implies \lambda = \bar{\lambda}$$
>
> Because $\lambda$ is equal to its own complex conjugate, $\lambda$ must be a real number. $\blacksquare$

</details><br>





**Eigenvectors of a symmetric matrix:** The eigenvectors of a symmetric matrix corresponding to distinct (non-repeated) eigenvalues are always orthogonal to one another.

<details>
<summary><B>Proof</B></summary>

> Let $A$ be a real symmetric matrix ($A = A^T$). Suppose $\lambda_1$ and $\lambda_2$ are two distinct eigenvalues ($\lambda_1 \neq \lambda_2$) with corresponding real eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$. This gives us:
> 1. $A\mathbf{v}_1 = \lambda_1\mathbf{v}_1$
> 2. $A\mathbf{v}_2 = \lambda_2\mathbf{v}_2$
>
> Consider the scalar quantity $\mathbf{v}_1^T A \mathbf{v}_2$. We can evaluate this in two different ways by associating the matrix multiplication either to the right or to the left:
> * **Evaluating to the right:**
>
> $$\mathbf{v}_1^T (A \mathbf{v}_2) = \mathbf{v}_1^T (\lambda_2 \mathbf{v}_2) = \lambda_2 (\mathbf{v}_1^T \mathbf{v}_2)$$
>
> * **Evaluating to the left:**
> Using the property $(A\mathbf{v}_1)^T = \mathbf{v}_1^T A^T$, and knowing $A^T = A$ due to symmetry:
>
> $$(\mathbf{v}_1^T A) \mathbf{v}_2 = (A \mathbf{v}_1)^T \mathbf{v}_2 = (\lambda_1 \mathbf{v}_1)^T \mathbf{v}_2 = \lambda_1 (\mathbf{v}_1^T \mathbf{v}_2)$$
>
> Equating the two results:
>
> $$\lambda_1 (\mathbf{v}_1^T \mathbf{v}_2) = \lambda_2 (\mathbf{v}_1^T \mathbf{v}_2) \implies (\lambda_1 - \lambda_2)(\mathbf{v}_1^T \mathbf{v}_2) = 0$$
>
> By our initial assumption, the eigenvalues are distinct, meaning $\lambda_1 - \lambda_2 \neq 0$. Consequently, the dot product must be zero:
>
> $$\mathbf{v}_1^T \mathbf{v}_2 = 0$$
>
> This proves that the eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are orthogonal. $\blacksquare$

</details><br>
