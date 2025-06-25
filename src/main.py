import numpy as np
from pathlib import Path
import yaml
from .lorenz import solve_lorenz
from .visualize import plot_3d_attractor, plot_time_series

def run_simulation(config_path="config/params.yaml"):
    # Load parameters
    with open(config_path) as f:
        params = yaml.safe_load(f)
        # Create output directories
    Path("data").mkdir(exist_ok=True)
    Path("figs").mkdir(exist_ok=True)
    
    # Time grid
    t = np.linspace(0, params["t_max"], params["steps"])
    
    # Run simulations
    x, y, z = solve_lorenz(
        initial_state=params["initial_state"],
        t=t,
        sigma=params["sigma"],
        rho=params["rho"],
        beta=params["beta"]
    )
    
    # Perturbed simulation
    perturbed_state = [x + 0.001 for x in params["initial_state"]]
    x_p, _, _ = solve_lorenz(
        initial_state=perturbed_state,
        t=t,
        sigma=params["sigma"],
        rho=params["rho"],
        beta=params["beta"]
    )