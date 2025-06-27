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
##