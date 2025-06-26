import numpy as np
from scipy.integrate import odeint

def lorenz_system(state, t, sigma, rho, beta):
    """Define the Lorenz system of ODEs"""
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])  # Explicitly return as numpy array

def solve_lorenz(initial_state, t, sigma=10, rho=28, beta=8/3):
    """Numerically solve the Lorenz system"""
    initial_state = np.array(initial_state, dtype=float)  # Convert input to numpy array
    solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))
    return solution.T  # Returns (x, y, z) arrays