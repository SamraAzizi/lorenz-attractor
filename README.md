# Lorenz Attractor Simulation


This project numerically simulates the Lorenz system, a set of ordinary differential equations known for its chaotic behavior, and visualizes the famous butterfly-shaped attractor in both 3D and time-series form.

## Project Structure

```bash
lorenz_attractor/
│
├── src/
│   ├── lorenz.py              # Lorenz system definition and numerical solver
│   ├── main.py                # Main simulation script (entry point)
│   ├── visualize.py           # Visualization functions (3D plot, time series)
│
├── config/
│   └── params.yaml            # Simulation parameters (initial state, sigma, rho, etc.)
│
├── data/                      # Output folder for simulation results (auto-created)
│
├── figs/                      # Output folder for generated plots (auto-created)
│
├── setup.py                   # Basic package setup for pip installation
└── README.md                  # You're here!
```

## Installation

1. CLone the repository:
```bash
git clone https://github.com/SamraAzizi/lorenz-attractor.git
cd lorenz_attractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt

```
Or manually install the main packages:
```bash
pip install numpy scipy matplotlib pyyaml

```

## Packaging(Optional)

if you want to install the project as a local package:
```bash
cd lorenz_attractor
pip install .

```
## Configuration (config/params.yaml)
Edit the params.yaml file to customiae your simulation:
```bash
initial_state: [1.0, 1.0, 1.0]
sigma: 10.0
rho: 28.0
beta: 2.6666666666666665
t_max: 40.0
steps: 10000

```
- `initial_state`: Starting coordinates `[x0, y0, z0]`
- `sigma`, `rho`, `beta`: Parameters of the Lorenz system
- `t_max`: Simulation time duration
- `steps`: Number of time steps in the simulation

## Running the simulation
Execute the following:
```bash
python src/main.py

```

This will:
- Solve the Lorenz equations using scipy.integrate.odeint
- Plot:
    - 3D Lorenz attractor: `figs/lorenz_3d.png`
    - Time-series plot of `X(t)` with and without a small perturbation: `figs/time_series.png`
- Save simulation data in:
    - `data/original.npy` — original solution
    - `data/perturbed.npy` — perturbed solution

## Visual Output
- `figs/lorenz_3d.png`
A beautiful 3D trajectory of the Lorenz attractor.

- `figs/time_series.png`
A 2D plot of `x(t)` and its divergence due to small perturbations — the butterfly effect in action.


## What is the Lorenz System?

The Lorenz system is a simplified mathematical model for atmospheric convection, defined by:


dt/dx =σ(y−x)
​
 
dt/dy =x(ρ−z)−y
​
 
dt/dz =xy−βz
​
 
​

 
It exhibits chaotic behavior for specific values of the parameters.