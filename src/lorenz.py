import numpy as np
from scipy.integrate import odeint

def lorenz_system(state, t, sigma, rho, beta):
    """Define the Lorenz system of ODEs"""
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def solve_lorenz(initial_state, t, sigma=10, rho=28, beta=8/3):
    """Numerically solve the Lorenz system"""
    solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))
    return solution.T  # Returns (x, y, z) arrays