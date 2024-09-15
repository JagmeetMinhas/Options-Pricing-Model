import numpy as np

def monte_carlo_call(S0, K, T, r, sigma, N_simulations):
    """
    Price a European call option using Monte Carlo Simulation.
    
    Parameters:
    - S0: Current stock price
    - K: Strike price
    - T: Time to expiration (in years)
    - r: Risk-free rate
    - sigma: Volatility
    - N_simulations: Number of simulated paths
    """
    np.random.seed(0)
    dt = T
    Z = np.random.normal(0, 1, N_simulations)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    payoff = np.maximum(ST - K, 0)
    price = np.exp(-r * T) * np.mean(payoff)
    return price

# Example usage
S0 = 50
K = 45
T = 0.5
r = 0.05
sigma = 0.20
N_simulations = 100000

price = monte_carlo_call(S0, K, T, r, sigma, N_simulations)
print(f'European Call Option Price (Monte Carlo): {price:.2f}')
