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