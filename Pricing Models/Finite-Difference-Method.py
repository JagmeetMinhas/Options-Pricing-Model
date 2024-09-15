import numpy as np

def finite_difference(S0, K, T, r, sigma, Smax, M, N, option_type):
    """
    Price a European option (call or put) using the Finite Difference Method.
    
    Parameters:
    - S0: Current stock price
    - K: Strike price
    - T: Time to expiration (in years)
    - r: Risk-free rate
    - sigma: Volatility
    - Smax: Maximum stock price considered in the grid
    - M: Number of stock price steps
    - N: Number of time steps
    - option_type: 'call' for call option, 'put' for put option
    """
    # The underlying asset price and time need to be discretized 
    S = np.linspace(0, Smax, M+1)
    dt = T / N
    dS = Smax / M
    
    # Instantiating a value matrix with 0s as placeholders
    V = np.zeros((M+1, N+1))
    
    # Add in boundary conditions at maturity
    if option_type == 'call':
        V[:, -1] = np.maximum(S - K, 0)
    elif option_type == 'put':
        V[:, -1] = np.maximum(K - S, 0)
    
    # Calculate finite difference coefficients
    alpha = 0.25 * dt * (sigma**2 * (np.arange(M+1) ** 2) - (r - 0.5 * sigma**2) * np.arange(M+1))
    beta = -dt * (sigma**2 * (np.arange(M+1) ** 2) + r)
    gamma = 0.25 * dt * (sigma**2 * (np.arange(M+1) ** 2) + (r - 0.5 * sigma**2) * np.arange(M+1))
    
    # Time-stepping loop
    for j in range(N-1, -1, -1):
        for i in range(1, M):
            V[i, j] = alpha[i] * V[i-1, j+1] + beta[i] * V[i, j+1] + gamma[i] * V[i+1, j+1]
        
        # Boundary conditions
        V[0, j] = np.maximum(K - 0, 0) if option_type == 'put' else 0  # Put option boundary
        V[M, j] = (Smax - K) * np.exp(-r * (T - j * dt)) if option_type == 'call' else (K - Smax) * np.exp(-r * (T - j * dt))  # Call/Put option boundary

    return V[int(M/2), 0]  # Option price at S0

# Example usage
S0 = 50
K = 45
T = 0.5
r = 0.05
sigma = 0.20
Smax = 100
M = 100
N = 100

call_price = finite_difference(S0, K, T, r, sigma, Smax, M, N, option_type='call')
put_price = finite_difference(S0, K, T, r, sigma, Smax, M, N, option_type='put')

print(f'European Call Option Price (FDM): {call_price:.2f}')
print(f'European Put Option Price (FDM): {put_price:.2f}')
