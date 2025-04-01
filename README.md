# statistical-simulation-airport-boarding-strategies

## Project Overview

This project simulates and statistically analyzes various airplane boarding strategies using a Monte Carlo approach. Each passenger is modeled as an independent stochastic agent with a travel delay based on row distance and a random luggage stowing time. The total boarding time for each simulation run is calculated and compared across different strategies.

## Folder Structure

The top-level folder is named `project-root`:

```
project-root/
├── scripts/
│   ├── 01_simulation.py       # Runs simulation of all boarding strategies
│   ├── 02_analysis.py         # Analyzes results and computes statistics
│   └── 03_visualization.py    # Generates plots from simulation data
├── outputs/
│   ├── simulation_results.csv # Raw simulation output
│   ├── analysis_results.csv   # Computed metrics (mean, median, std)
│   ├── boxplot.png            # Boxplot comparing strategies
│   └── barchart.png           # Bar chart of average boarding times
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Usage

### 1. Setup the Project:

Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 2. Run the Simulation:
Run the script to simulate multiple replications of each boarding strategy.
```bash
python scripts/01_simulation.py
```

### 3. Analyze the Results:
Compute statistical summaries like mean, median, and standard deviation for each strategy.
```bash
python scripts/02_analysis.py
```

### 4. Visualize the Data:
Generate comparative visualizations of the results.
```bash
python scripts/03_visualization.py
```

All outputs are saved to the `outputs/` directory.

## Requirements

The following Python packages are required:

- numpy
- pandas
- matplotlib

Install using:
```bash
pip install -r requirements.txt
```