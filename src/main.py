import numpy as np
from pathlib import Path
import yaml
from .lorenz import solve_lorenz
from .visualize import plot_3d_attractor, plot_time_series

def run_simulation(config_path="config/params.yaml"):
    # Load parameters
    with open(config_path) as f:
        params = yaml.safe_load(f)