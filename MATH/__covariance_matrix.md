# Covariance matrix

## 1. The Data Representation

We begin with a dataset consisting of $N$ events (samples), where each event contains $D$ distinct features. This dataset can be structured as a matrix where rows represent features and columns represent events:

|  | Event 1 | Event 2 | $\dots$ | Event $N$ |
| --- | --- | --- | --- | --- |
| **Feature 1** | $x_{11}$ | $x_{12}$ | $\dots$ | $x_{1N}$ |
| **Feature 2** | $x_{21}$ | $x_{22}$ | $\dots$ | $x_{2N}$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
| **Feature $D$** | $x_{D1}$ | $x_{D2}$ | $\dots$ | $x_{DN}$ |

Geometrically, this dataset represents **$N$ distinct points residing in a $D$-dimensional space**.

---

## 2. Statistical Metrics (2D Example)

To illustrate, let us consider a simplified case where $N$ points have only $2$ features ($x$ and $y$). The resulting data matrix $A$ has a dimension of $2 \times N$:

$$A  = \begin{bmatrix} x_1 & x_2 & \dots & x_N \\ y_1 & y_2 & \dots & y_N \end{bmatrix}$$

### The Mean Vector

The expected value (mean) vector, $E(A)$, calculates the average value for each individual feature across all samples:

$$E(A) = \begin{bmatrix} E(x) \\ E(y) \end{bmatrix} = \begin{bmatrix} \frac{1}{N}\sum x_i \\ \frac{1}{N}\sum y_i \end{bmatrix}$$

### Beyond Individual Variance: Covariance

Analyzing the variance of each feature independently is insufficient because it fails to capture the underlying behavior and geometric structure of the data. Two entirely different datasets can exhibit identical variances per feature while possessing drastically different relationships between those features.

To preserve as much informational behavior as possible, we must measure the variance and covariance between every pair of features: $V(x,x)$, $V(y,y)$, and $V(x,y)$.

Using Bessel's correction ($N-1$) to achieve an unbiased estimator, these metrics are defined as:

* **Variance of $x$:** $V(x,x) = E[(x-E(x))^2] = \frac{(x-E(x))(x-E(x))^T}{N-1}$
* **Variance of $y$:** $V(y,y) = E[(y-E(y))^2] = \frac{(y-E(y))(y-E(y))^T}{N-1}$
* **Covariance of $x$ and $y$:** $V(x,y) = E[(x-E(x))(y-E(y))] = \frac{(x-E(x))(y-E(y))^T}{N-1}$

### The Covariance Matrix

We can elegantly capture all variance and covariance interactions simultaneously using matrix operations. First, we define $X$ as the **mean-centered** data matrix:

$$X = A - E(A)$$

The covariance matrix $C$ is then constructed as:

$$C = E(X X^T) = \frac{X X^T}{N-1} = \begin{bmatrix} V(x,x) & V(x,y) \\ V(y,x) & V(y,y) \end{bmatrix}$$

---

## 3. Projecting Data Onto a Unit Vector

Let $\mathbf{v}$ be a unit vector representing a new direction in our feature space. We want to project our mean-centered data points onto this vector.

The resulting vector $\mathbf{u}$ contains the coordinates of the projected points along the axis defined by $\mathbf{v}$:

$$\mathbf{u} = X^T \mathbf{v} = \mathbf{v}^T X$$

*(Note: $\mathbf{u}$ is a column vector containing $N$ values).*

---

## 4. Maximizing Projected Variance

Our objective is to find the optimal direction $\mathbf{v}$ that maximizes the variance of the projected points.

Using Bessel's correction, the variance along this new projection axis is derived as follows:

$$\text{Var}(\mathbf{u}) = \frac{\mathbf{u}^T \mathbf{u}}{N-1}$$

$$\text{Var}(\mathbf{u}) = \frac{(X^T \mathbf{v})^T (X^T \mathbf{v})}{N-1}$$

$$\text{Var}(\mathbf{u}) = \frac{\mathbf{v}^T X X^T \mathbf{v}}{N-1}$$

$$\text{Var}(\mathbf{u}) = \mathbf{v}^T \left( \frac{X X^T}{N-1} \right) \mathbf{v} = \mathbf{v}^T C \mathbf{v}$$

We formulate this as a constrained optimization problem, where we maximize the projected variance while enforcing the condition that $\mathbf{v}$ remains a unit vector ($|\mathbf{v}| = 1$):

$$\max_{\mathbf{v}} \left( \mathbf{v}^T C \mathbf{v} \right) \quad \text{subject to} \quad \mathbf{v}^T \mathbf{v} = 1$$

Using the method of **Lagrange Multipliers**, we can integrate the constraint directly into our objective function via the Lagrangian function $L(\mathbf{v}, \lambda)$:

$$L(\mathbf{v}, \lambda) = \mathbf{v}^T C \mathbf{v} + \lambda (1 - \mathbf{v}^T \mathbf{v})$$



## 5. Solving the Optimization Problem

To find the direction $\mathbf{v}$ that maximizes our objective function, we must find the critical points of the Lagrangian function by taking its partial derivative with respect to $\mathbf{v}$ and setting it equal to zero.

### Step 1: Differentiate the Lagrangian Function

Recall our Lagrangian function:


$$L(\mathbf{v}, \lambda) = \mathbf{v}^T C \mathbf{v} + \lambda (1 - \mathbf{v}^T \mathbf{v})$$

We take the derivative with respect to the vector $\mathbf{v}$ using standard rules of matrix calculus:

* $\frac{\partial}{\partial \mathbf{v}}(\mathbf{v}^T C \mathbf{v}) = 2C\mathbf{v}$ *(since $C$ is a symmetric covariance matrix)*
* $\frac{\partial}{\partial \mathbf{v}}(\lambda \mathbf{v}^T \mathbf{v}) = 2\lambda\mathbf{v}$

Setting the gradient to the zero vector ($\mathbf{0}$):


$$\frac{\partial L}{\partial \mathbf{v}} = 2C\mathbf{v} - 2\lambda\mathbf{v} = \mathbf{0}$$

### Step 2: The Eigenvalue Equation Emerges

Divide the entire equation by 2 and move the constraint term to the right side:


$$C\mathbf{v} = \lambda\mathbf{v}$$

> **The Insight:** This is the foundational eigenvalue equation. It demonstrates that the direction $\mathbf{v}$ that maximizes the projected variance **must be an eigenvector** of the covariance matrix $C$, and the scalar $\lambda$ is its corresponding **eigenvalue**.

### Step 3: Determining Which Eigenvector Maximize Variance

To confirm what the maximum variance actually equals, let's substitute this result back into our original variance equation, $\text{Var}(\mathbf{u}) = \mathbf{v}^T C \mathbf{v}$:

$$\text{Var}(\mathbf{u}) = \mathbf{v}^T (C \mathbf{v})$$

Since $C\mathbf{v} = \lambda\mathbf{v}$:


$$\text{Var}(\mathbf{u}) = \mathbf{v}^T (\lambda \mathbf{v}) = \lambda (\mathbf{v}^T \mathbf{v})$$

Because $\mathbf{v}$ is a unit vector, its dot product with itself is exactly 1 ($\mathbf{v}^T \mathbf{v} = 1$):


$$\text{Var}(\mathbf{u}) = \lambda$$



## 6. Conclusion

1. The variance of the data projected onto any eigenvector of the covariance matrix is exactly equal to that eigenvector's corresponding eigenvalue ($\lambda$).
2. To maximize the variance, we must choose the eigenvector corresponding to the **largest eigenvalue** ($\lambda_{\max}$).

This optimal direction $\mathbf{v}_{\max}$ is precisely what we call the **First Principal Component**.


## 7. Finding the Second Principal Component

After finding the first direction $\mathbf{v}_1$ (the eigenvector corresponding to the largest eigenvalue $\lambda_1$), we want to find a second direction $\mathbf{v}_2$ that maximizes the remaining variance.

To ensure we capture entirely new structural information, **this second direction must be completely orthogonal to the first** ($\mathbf{v}_2^T \mathbf{v}_1 = 0$).

### Formulating the Constrained Optimization Problem

We want to maximize the variance along the new direction $\mathbf{v}_2$, subject to two constraints:

1. It must be a unit vector: $\mathbf{v}_2^T \mathbf{v}_2 = 1$
2. It must be orthogonal to $\mathbf{v}_1$: $\mathbf{v}_2^T \mathbf{v}_1 = 0$

Using the method of Lagrange Multipliers again, we introduce a second multiplier ($\alpha$) to handle this new orthogonality constraint:

$$L(\mathbf{v}_2, \lambda_2, \alpha) = \mathbf{v}_2^T C \mathbf{v}_2 + \lambda_2 (1 - \mathbf{v}_2^T \mathbf{v}_2) - \alpha (\mathbf{v}_2^T \mathbf{v}_1)$$



### Step 1: Differentiate and Optimize

We take the partial derivative of the Lagrangian with respect to $\mathbf{v}_2$ and set it to zero:

$$\frac{\partial L}{\partial \mathbf{v}_2} = 2C\mathbf{v}_2 - 2\lambda_2\mathbf{v}_2 - \alpha \mathbf{v}_1 = \mathbf{0}$$

### Step 2: Show that the Multiplier $\alpha$ Must Be Zero

To solve for $\alpha$, we multiply the entire equation from the left by $\mathbf{v}_1^T$:

$$2\mathbf{v}_1^T C\mathbf{v}_2 - 2\lambda_2\mathbf{v}_1^T\mathbf{v}_2 - \alpha \mathbf{v}_1^T \mathbf{v}_1 = 0$$

Now, we can simplify this expression using properties we already know:

* Because $\mathbf{v}_1$ and $\mathbf{v}_2$ are orthogonal, $\mathbf{v}_1^T\mathbf{v}_2 = 0$.
* Because $\mathbf{v}_1$ is a unit vector, $\mathbf{v}_1^T \mathbf{v}_1 = 1$.
* For the first term, because $C$ is symmetric, $\mathbf{v}_1^T C\mathbf{v}_2 = (C\mathbf{v}_1)^T \mathbf{v}_2$. Since $C\mathbf{v}_1 = \lambda_1 \mathbf{v}_1$, this becomes $\lambda_1 \mathbf{v}_1^T \mathbf{v}_2 = 0$.

Substituting these values back into the equation:


$$2(0) - 2\lambda_2(0) - \alpha(1) = 0 \implies \alpha = 0$$

### Step 3: The Second Eigenvalue Equation Emerges

Since $\alpha = 0$, the orthogonality constraint term completely drops out of our derivative equation, leaving us with:

$$2C\mathbf{v}_2 - 2\lambda_2\mathbf{v}_2 = \mathbf{0} \implies C\mathbf{v}_2 = \lambda_2\mathbf{v}_2$$


## 8. Final Conclusion

Just like the first direction, the second direction $\mathbf{v}_2$ **must also be an eigenvector** of the covariance matrix $C$.

* To maximize the remaining variance, we choose the eigenvector corresponding to the **second largest eigenvalue** ($\lambda_2$).
* Because $C$ is a symmetric matrix, the proof of orthogonality we derived earlier guarantees that this second eigenvector $\mathbf{v}_2$ will automatically be perpendicular to $\mathbf{v}_1$.

This direction is the **Second Principal Component**. This process repeats inductively for all $D$ dimensions, yielding an ordered, orthonormal basis of features.