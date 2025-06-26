import numpy as np
from scipy.integrate import odeint

def lorenz_system(state, t, sigma, rho, beta):
    """Define the Lorenz system of ODEs"""
    x, y, z = map(float, state)  # Explicitly convert to float
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def solve_lorenz(initial_state, t, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """Numerically solve the Lorenz system"""
    initial_state = np.array(initial_state, dtype=np.float64)  # Force float64
    solution = odeint(lorenz_system, initial_state, t, args=(float(sigma), float(rho), float(beta)))
    return solution.T  # Returns (x, y, z) arrays