#import dependencies
import numpy as np
from scipy.stats import norm

class blackScholesEquation:
    def __init__(self, currentPrice: float, strikePrice: float, yearsToExpiration: int, riskFreeRate: float, volatility: float, optionType = str):
        self.currentPrice = currentPrice
        self.strikePrice = strikePrice
        self.yearsToExpiration = yearsToExpiration
        self.riskFreeRate = riskFreeRate
        self.volatility = volatility
        self.optionType = optionType

    def d1Calculation(self):
        numerator = np.log(self.currentPrice/self.strikePrice) + (self.riskFreeRate + (((self.volatility**2)/2)) * self.yearsToExpiration)
        denominator =  self.volatility * (self.yearsToExpiration**0.5)

        return (numerator/denominator)
    
    def d2Calculation(self):
        return self.d1Calculation() - (self.volatility * (self.yearsToExpiration**0.5))
    
    def priceCalculation(self):
        if self.optionType == "call":
            return self.currentPrice * norm.cdf(self.d1Calculation()) - (self.strikePrice * np.exp(-self.riskFreeRate * self.yearsToExpiration) * norm.cdf(self.d2Calculation()))
        elif self.optionType == "put":
            return (self.strikePrice * np.exp(-self.riskFreeRate * self.yearsToExpiration) * norm.cdf(-self.d2Calculation())) - (self.currentPrice * norm.cdf(-self.d1Calculation())) 
        else:
            raise ValueError("The option type must be either a call or put.")


def main():
    model = blackScholesEquation(50, 45, 0.5, 0.05, 0.20, "put")

    print(model.priceCalculation())

main()