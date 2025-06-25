import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_attractor(x, y, z, save_path=None):
    """Create 3D visualization of attractor"""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, lw=0.5, color='blue')
    ax.set_title("Lorenz Attractor")
    ax.set_xlabel("X"), ax.set_ylabel("Y"), ax.set_zlabel("Z")
    
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.close()

def plot_time_series(t, x, x_perturbed=None, save_path=None):
    """Plot time evolution and butterfly effect"""
    plt.figure(figsize=(10, 6))
    plt.plot(t, x, 'b', label="Original")
    if x_perturbed is not None:
        plt.plot(t, x_perturbed, 'r--', label="Perturbed", alpha=0.7)
    plt.title("Time Evolution of X(t)")
    plt.xlabel("Time"), plt.ylabel("X value")
    plt.legend()
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path, dpi=300)
    plt.close()