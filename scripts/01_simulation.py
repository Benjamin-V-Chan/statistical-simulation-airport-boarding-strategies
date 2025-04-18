import os
import random
import numpy as np
import pandas as pd

# Simulation parameters
NUM_REPLICATIONS = 100
NUM_ROWS = 30
SEATS_PER_ROW = 6  # not used explicitly in this simulation model
TIME_PER_ROW = 1  # seconds per row traversal
OVERHEAD_DELAY_RANGE = (2, 5)  # seconds delay for stowing luggage
BOARDING_STRATEGIES = ['Random', 'Back-to-Front', 'Block']

# Define Passenger class
class Passenger:
    def __init__(self, pid, row, overhead_delay):
        self.pid = pid
        self.row = row
        self.overhead_delay = overhead_delay

# Function to simulate boarding for a given strategy
def simulate_boarding(passengers, strategy):
    if strategy == 'Random':
        random.shuffle(passengers)
    elif strategy == 'Back-to-Front':
        passengers.sort(key=lambda p: p.row, reverse=True)
    elif strategy == 'Block':
        block_size = 5
        # Group passengers into blocks by row
        blocks = {}
        for p in passengers:
            block = (p.row - 1) // block_size
            blocks.setdefault(block, []).append(p)
        # Order blocks in descending order (highest rows first) and flatten list
        ordered_blocks = []
        for b in sorted(blocks.keys(), reverse=True):
            ordered_blocks.extend(blocks[b])
        passengers = ordered_blocks
    else:
        raise ValueError("Unknown boarding strategy")
    
    current_time = 0
    for p in passengers:
        travel_time = p.row * TIME_PER_ROW
        start_time = max(current_time, travel_time)
        finish_time = start_time + p.overhead_delay
        current_time = finish_time
    return current_time

def main():
    results = []
    for rep in range(1, NUM_REPLICATIONS + 1):
        for strategy in BOARDING_STRATEGIES:
            passengers = []
            total_passengers = NUM_ROWS * SEATS_PER_ROW
            for pid in range(1, total_passengers + 1):
                row = random.randint(1, NUM_ROWS)
                overhead_delay = np.random.uniform(*OVERHEAD_DELAY_RANGE)
                passengers.append(Passenger(pid, row, overhead_delay))
            total_time = simulate_boarding(passengers, strategy)
            results.append({'Replication': rep, 'Strategy': strategy, 'Total_Time': total_time})
    
    df = pd.DataFrame(results)
    os.makedirs("outputs", exist_ok=True)
    df.to_csv(os.path.join("outputs", "simulation_results.csv"), index=False)

if __name__ == '__main__':
    main()