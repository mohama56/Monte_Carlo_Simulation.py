# Monte_Carlo_Simulation.py
Using Python and the Numpy library to perform Monte Carlo simulations and statistical modeling for demand forecasting, optimizing production management, and profit maximization under normal distribution constraints while incorporating scenario analysis for cost uncertainties.

## 📋 Overview

This project models a production optimization problem for TwoPlus Earbuds X, a product with a limited sales window. Using Python and the Numpy library, we implemented Monte Carlo simulations to determine the optimal production quantity to maximize profits while accounting for demand variability and potential cost uncertainties.

## 🛠 Features

Simulates demand using a normal distribution (mean: 150, standard deviation: 20).
Calculates profitability based on production quantities, costs, and revenues.
Accounts for disposal costs of unsold units.
Performs scenario analysis to evaluate the impact of policy-driven tax increases on unsold products.
Identifies the optimal production quantity for maximum profitability under various scenarios.

## 📈 Results

Base Scenario:
Optimal Production Quantity: 184 units
Maximum Profit: $18,014.51
Bonus Scenario (50% chance of additional tax):

Optimal Production Quantity: 187 units
Average Profit: $17,921.85

## 🖥️ Installation

To run the project locally, follow these steps:

Clone this repository:
bash
Copy code
git clone https://github.com/mohama56/Monte_Carlo_Simulation.py.git
Navigate to the project directory:
bash
Copy code
cd TwoPlus-Earbuds-Problem
Install the required Python libraries:
pip install numpy

## ▶️ Usage

Run the simulation script to find the optimal production quantity:

python simulation.py
Input Parameters:
Unit cost: $28.50
Retail price: $150.00
Disposal cost: $8.50 (or $17.00 under the tax scenario)
Output:
Optimal production quantity for maximum profit.
Profitability for both base and tax-imposed scenarios.

## 🧰 Code Structure

simulation.py: Main Python script containing the simulation logic.
README.md: Documentation for the project.
results/: Folder for snapshots of outputs and any relevant logs.

## 📚 Methodology

Demand Simulation: Modeled demand as a normal distribution using Numpy's np.random.normal() function.
Profit Calculation: Iterated over possible production quantities to calculate profits under varying demand scenarios.
Scenario Analysis: Used np.random.choice() to simulate a 50% probability of additional tax costs for unsold units.

## 🚀 Applications

This project demonstrates the use of data-driven decision-making for:

Inventory management
Production optimization
Profit maximization

## ⚠️ Disclaimer
This project was created as part of the Python coursework at Cornell University's SC Johnson School of Business. It is shared here for educational and portfolio purposes only. Redistribution or commercial use is not permitted without explicit permission from the course instructor or the university.
