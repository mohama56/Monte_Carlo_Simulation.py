"""
Variables like unit_cost, retail_price, and disposal_cost define the cost structure.
"""

import numpy as np   # Imports the NumPy library for numerical calculations

# simulating profits func
def simulate_earbuds_profit(unit_cost, retail_price, disposal_cost, num_earbuds):
    demands = np.random.normal(150, 20, 1000)  # Step 1: simulate randomly generated demand
    profits = []

    for demand in demands: # Step 2: profits are calculated for each simulated demand value 
        units_sold = min(num_earbuds, demand)
        unsold = max(0, num_earbuds - demand)
        profit = (units_sold * (retail_price - unit_cost)) - (unsold * disposal_cost)
        profits.append(profit)

    mean_profit = np.mean(profits)  # Step 3: calculating mean
    std_profit = np.std(profits)   # StDev
    return mean_profit, std_profit

# Step 4: explore potential values and identify the optimal solution
optimal_units = None
max_profit = float('-inf')
for units in range(0, 231):  # This loop evaluates every possible production level from 0 to 230
    mean_profit, _ = simulate_earbuds_profit(28.5, 150.0, 8.5, units)
    if mean_profit > max_profit:
        max_profit = mean_profit
        optimal_units = units

print(f"Optimal number of earbuds to manufacture: {optimal_units}, with maximum mean profit: {max_profit}")

# Bonus Question : additional simulation with tax
def simulate_with_tax(unit_cost, retail_price, disposal_cost, additional_disposal_cost, num_earbuds):
    demands = np.random.normal(150, 20, 1000)
    profits = []
    for demand in demands:
        additional_tax = np.random.choice([True, False], p=[0.5, 0.5]) # a 50% chance of additional disposal cost is simulated 
        effective_disposal_cost = disposal_cost if not additional_tax else additional_disposal_cost
        units_sold = min(num_earbuds, demand)
        unsold = max(0, num_earbuds - demand)
        profit = (units_sold * (retail_price - unit_cost)) - (unsold * effective_disposal_cost)
        profits.append(profit)

    mean_profit = np.mean(profits)
    std_profit = np.std(profits)
    return mean_profit, std_profit

bonus_optimal_units = None
bonus_max_profit = float('-inf')
for units in range(0, 231):
    mean_profit, _ = simulate_with_tax(28.5, 150.0, 8.5, 17.0, units) # calculates the mean profit per production level with taxes
    if mean_profit > bonus_max_profit:
        bonus_max_profit = mean_profit
        bonus_optimal_units = units

print(f"Bonus optimal number of earbuds: {bonus_optimal_units}, with maximum mean profit: {bonus_max_profit}")





