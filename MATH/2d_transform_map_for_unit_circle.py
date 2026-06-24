import numpy as np
import matplotlib.pyplot as plt
import math


def _pi_ticks_0_to_2pi():
    ticks = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
    labels = [r"0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"]
    return ticks, labels


def plot_transformed_unit_circle(matrix, samples=1000):
    """
    Plot magnitude and direction of A*u(theta)
    where u(theta) is a unit vector on the unit circle.

    Parameters
    ----------
    matrix : array-like shape (2,2)
        Transformation matrix.
    samples : int
        Number of sampled angles.
    """

    A = np.asarray(matrix, dtype=float)

    # endpoint=False avoids duplicate direction at 0 and 2*pi.
    theta = np.linspace(0, 2 * np.pi, samples, endpoint=False)

    unit_vectors = np.vstack([
        np.cos(theta),
        np.sin(theta)
    ])

    transformed = A @ unit_vectors

    magnitude = np.linalg.norm(transformed, axis=0)

    angle = np.mod(np.arctan2(transformed[1], transformed[0]), 2 * np.pi)
    # Wrapped angular difference in [-pi, pi]. Same direction when close to 0.
    wrapped_delta = np.angle(np.exp(1j * (angle - theta)))
    angle_step = (2 * np.pi) / max(samples - 1, 1)
    match_tol = 1.5 * angle_step
    match_mask = np.abs(wrapped_delta) <= match_tol

    match_indices = []
    in_run = False
    run_start = 0
    for i, is_match in enumerate(match_mask):
        if is_match and not in_run:
            in_run = True
            run_start = i
        elif not is_match and in_run:
            run_end = i
            local = run_start + np.argmin(np.abs(wrapped_delta[run_start:run_end]))
            match_indices.append(local)
            in_run = False
    if in_run:
        run_end = len(match_mask)
        local = run_start + np.argmin(np.abs(wrapped_delta[run_start:run_end]))
        match_indices.append(local)

    match_indices = np.asarray(match_indices, dtype=int)
    pi_ticks, pi_labels = _pi_ticks_0_to_2pi()

    fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

    axes[0].plot(theta, magnitude, color="#d62728", linewidth=2)
    if match_indices.size:
        axes[0].plot(
            theta[match_indices],
            magnitude[match_indices],
            linestyle="None",
            marker="o",
            markersize=7,
            markerfacecolor="none",
            markeredgecolor="#d62728",
            markeredgewidth=2,
            label="same direction"
        )
    axes[0].set_ylabel("||A·u||")
    axes[0].set_title("Magnitude of transformed unit vectors")
    axes[0].set_xlim(0, 2 * np.pi)
    axes[0].set_xticks(pi_ticks, pi_labels)
    axes[0].grid(True, alpha=0.3)
    if match_indices.size:
        axes[0].legend(loc="best")

    axes[1].plot(theta, angle, color="#2ca02c", linewidth=2)
    if match_indices.size:
        axes[1].plot(
            theta[match_indices],
            angle[match_indices],
            linestyle="None",
            marker="o",
            markersize=7,
            markerfacecolor="none",
            markeredgecolor="#2ca02c",
            markeredgewidth=2
        )
    axes[1].set_xlabel("Input angle θ")
    axes[1].set_ylabel("Output angle (rad)")
    axes[1].set_title("Direction of transformed vectors")
    axes[1].set_xlim(0, 2 * np.pi)
    axes[1].set_ylim(0, 2 * np.pi)
    axes[1].set_xticks(pi_ticks, pi_labels)
    axes[1].set_yticks(pi_ticks, pi_labels)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_transformed_unit_circle_map(matrix, samples=1000):
    """
    Plot a map: in black the unit circle, and in red the transformed unit circle     

    Parameters
    ----------
    matrix : array-like shape (2,2)
        Transformation matrix.
    samples : int
        Number of sampled angles.
    """    
    A = np.asarray(matrix, dtype=float)
    if A.shape != (2, 2):
        raise ValueError("matrix must have shape (2, 2)")

    theta = np.linspace(0, 2 * np.pi, samples, endpoint=False)

    unit_circle = np.vstack([
        np.cos(theta),
        np.sin(theta)
    ])
    transformed_circle = A @ unit_circle

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.plot(
        unit_circle[0],
        unit_circle[1],
        color="black",
        linewidth=2,
        label="Unit circle"
    )
    ax.plot(
        transformed_circle[0],
        transformed_circle[1],
        color="#d62728",
        linewidth=2,
        label="A · unit circle"
    )

    ax.axhline(0, color="gray", linewidth=1, alpha=0.5)
    ax.axvline(0, color="gray", linewidth=1, alpha=0.5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Unit circle and transformed unit circle")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    all_x = np.concatenate([unit_circle[0], transformed_circle[0]])
    all_y = np.concatenate([unit_circle[1], transformed_circle[1]])
    max_range = max(
        np.max(np.abs(all_x)),
        np.max(np.abs(all_y)),
        1.0
    )
    margin = 0.15 * max_range
    lim = max_range + margin
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    plt.tight_layout()
    plt.show()


# identity matrix
matrix = np.eye(2)


# rotation matrix 45 degrees
θ = math.pi/4
matrix = np.array([[math.cos(θ), -math.sin(θ)], 
                   [math.sin(θ), math.cos(θ)]])


# 
matrix = np.array([[1, 0.7], 
                   [0.7, 1]])


#plot_transformed_unit_circle(matrix)
plot_transformed_unit_circle_map(matrix)