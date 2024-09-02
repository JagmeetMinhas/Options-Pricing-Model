# Options Pricing Models in Python
This project provides an in-depth exploration of different methods for pricing European and American-style options. By implementing three distinct models — Black-Scholes, Monte Carlo Simulation, and the Finite Difference Method — this project aims to demonstrate the strengths and limitations of various approaches used in quantitative finance for options pricing.

# Introduction
Options are financial derivatives that provide the right, but not the obligation, to buy or sell an underlying asset at a specified price on or before a certain date. Accurate pricing of options is crucial for investors, traders, and risk managers to make informed decisions. There are several methods to price options, each with its unique advantages and constraints:

Black-Scholes Model: The Black-Scholes model is a closed-form analytical solution that assumes a lognormal distribution of stock prices and continuous trading. It is widely used for pricing European-style options due to its simplicity and efficiency. However, it is not suitable for American-style options, which can be exercised at any time before expiration.

Monte Carlo Simulation: This model uses stochastic processes to simulate the underlying asset's price paths and calculates the expected payoff of the option across numerous simulated scenarios. Monte Carlo methods are highly flexible and can accommodate complex features such as path dependency or varying volatility but can be computationally expensive.

Finite Difference Method (FDM): FDM is a numerical technique that solves the partial differential equations (PDEs) that govern option prices. This approach is particularly effective for American-style options, which may require early exercise. By discretizing time and space, FDM can accurately approximate the value of both European and American options, accounting for a wide range of conditions and features.

# Objectives
The goal of this project is to:

- Implement and compare three different options pricing models.
- Analyze the advantages and limitations of each model.
- Provide a hands-on learning experience for understanding options pricing in financial markets.
- Extend the models to include real-world data, varying market conditions, and different types of options.

# Project Structure
This project is organized into three main Python scripts, each dedicated to a specific model:

Black-Scholes.py: Implements the Black-Scholes model for European-style options.
Monte-carlo.py: Uses Monte Carlo simulation to price options based on stochastic processes.
Finite_Difference.py: Utilizes the Finite Difference Method to solve the differential equations for pricing both European and American-style options.
