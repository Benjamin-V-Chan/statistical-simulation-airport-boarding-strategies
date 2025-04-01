"""
1. Import necessary modules (os, random, numpy, pandas).
2. Define simulation parameters:
    - NUM_REPLICATIONS: number of simulation runs.
    - NUM_ROWS: total rows in the aircraft.
    - SEATS_PER_ROW: number of seats per row.
    - TIME_PER_ROW: constant time (seconds) to traverse one row.
    - OVERHEAD_DELAY_RANGE: min and max seconds for stow delay.
    - BOARDING_STRATEGIES: list of strategies ['Random', 'Back-to-Front', 'Block'].
3. Define a Passenger class with attributes: id, row, overhead_delay.
4. Define function simulate_boarding(passengers, strategy):
    a. Order the passengers according to the strategy:
         - For 'Random': randomly shuffle the list.
         - For 'Back-to-Front': sort passengers by row in descending order.
         - For 'Block': divide rows into blocks (e.g., groups of 5 rows) and board highest blocks first.
    b. Initialize current_time = 0.
    c. For each passenger in the ordered list:
         - Compute travel_time = passenger.row * TIME_PER_ROW.
         - Compute start_time = max(current_time, travel_time).
         - Compute finish_time = start_time + passenger.overhead_delay.
         - Update current_time = finish_time.
    d. Return the total boarding time.
5. Main simulation loop:
    a. For each replication (from 1 to NUM_REPLICATIONS):
         i. For each strategy in BOARDING_STRATEGIES:
              - Generate a list of passengers with:
                    * An id.
                    * A random row assignment (simulate a full flight: row chosen uniformly from 1 to NUM_ROWS).
                    * A random overhead_delay (from OVERHEAD_DELAY_RANGE).
              - Run simulate_boarding() and record the total boarding time.
              - Save replication number, strategy, and total_time to a results list.
6. Convert the results list to a pandas DataFrame.
7. Create the outputs/ folder (if not exists) and save the DataFrame as "simulation_results.csv".
"""

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