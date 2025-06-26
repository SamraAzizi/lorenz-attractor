import numpy as np
from pathlib import Path
import yaml
from lorenz import solve_lorenz
from visualize import plot_3d_attractor, plot_time_series

def run_simulation(config_path="config/params.yaml"):
    # Load parameters
    with open(config_path) as f:
        params = yaml.safe_load(f)
    
    # Convert all values to float explicitly
    params = {k: float(v) if isinstance(v, (int, float)) else v 
              for k, v in params.items()}
    
    # Create output directories
    Path("data").mkdir(exist_ok=True)
    Path("figs").mkdir(exist_ok=True)
    
    # Time grid
    t = np.linspace(0, float(params["t_max"]), int(params["steps"]))
    
    # Ensure initial_state is list of floats
    initial_state = [float(x) for x in params["initial_state"]]
    
    # Run simulations
    x, y, z = solve_lorenz(
        initial_state=initial_state,
        t=t,
        sigma=params["sigma"],
        rho=params["rho"],
        beta=params["beta"]
    )
    
    # Rest of your code remains the same...
    # Generate plots and save data
    plot_3d_attractor(x, y, z, save_path="figs/lorenz_3d.png")
    
    # Perturbed simulation
    perturbed_state = [x + 0.001 for x in initial_state]
    x_p, _, _ = solve_lorenz(
        initial_state=perturbed_state,
        t=t,
        sigma=params["sigma"],
        rho=params["rho"],
        beta=params["beta"]
    )
    plot_time_series(t, x, x_p, save_path="figs/time_series.png")
    
    # Save data
    np.save("data/original.npy", np.vstack((x, y, z)))
    np.save("data/perturbed.npy", x_p)

if __name__ == "__main__":
    run_simulation()