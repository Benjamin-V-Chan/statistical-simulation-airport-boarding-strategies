# statistical-simulation-airport-boarding-strategies

## Project Overview

This project simulates and statistically analyzes various airplane boarding strategies using a Monte Carlo approach. Each passenger is modeled as an independent stochastic agent with a travel delay based on row distance and a random luggage stowing time. The total boarding time for each simulation run is calculated and compared across different strategies.

### Mathematical Model

Let $N$ be the total number of passengers, each with a designated row $r_i$ where $1 \leq r_i \leq R$ for total rows $R$. Let $t_r$ be the constant time to walk past one row, and $\delta_i$ be the luggage stowing delay of passenger $i$, drawn from a uniform distribution:
$$\delta_i \sim \mathcal{U}(a, b)$$

Let the entry time $T_i$ be defined recursively:
$$T_i = \max(T_{i-1}, r_i \cdot t_r) + \delta_i$$
with $T_0 = 0$.

This represents a queuing process with blocking, where:
- $r_i \cdot t_r$ is the earliest possible arrival time at the seat,
- $T_{i-1}$ is when the previous passenger clears the aisle.

### Total Boarding Time

The total boarding time $T_{\text{total}}$ is:
$$T_{\text{total}} = \max_{1 \leq i \leq N} T_i$$

As $N \to \infty$, the distribution of $T_{\text{total}}$ converges (by the Central Limit Theorem) to a normal distribution if $\delta_i$ are i.i.d. Additionally, using queuing theory and renewal reward processes, the expected boarding time can be approximated:
$$\mathbb{E}[T_{\text{total}}] \approx N \cdot \mathbb{E}[\delta] + \sum_{i=1}^{N} \mathbb{E}[\max(0, r_i \cdot t_r - T_{i-1})]$$

### Boarding Strategies

Each strategy modifies the sequence $\{r_i\}$:
- **Random**: $r_i$ are randomly permuted.
- **Back-to-Front**: passengers are sorted descending by $r_i$.
- **Block Boarding**: passengers are grouped by row ranges (blocks), then sorted within each block.

By simulating each strategy over many replications, we derive their empirical distributions and comparative statistics.

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