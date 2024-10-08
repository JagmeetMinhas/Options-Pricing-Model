#import dependencies
import numpy as np
from scipy.stats import norm

#INCORPORATE DIVIDENDS!
class blackScholesEquation:
    def __init__(self, currentPrice: float, strikePrice: float, yearsToExpiration: int, riskFreeRate: float, volatility: float, yearsElapsed: int, hasDividends: bool, optionType: str):
        self.currentPrice = currentPrice
        self.strikePrice = strikePrice
        self.yearsToExpiration = yearsToExpiration
        self.riskFreeRate = riskFreeRate
        self.volatility = volatility
        self.yearsElapsed = yearsElapsed
        self.optionType = optionType

    def getStrikePrice(self):
        '''To be used for per share profit calculation'''
        return self.currentPrice


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
        
    def getDelta(self):
        if self.optionType == "call":
            return norm.cdf(self.d1Calculation())
        elif self.optionType == "put":
            return norm.cdf(self.d1Calculation) - 1
        else:
            raise ValueError("The option type must be either a call or put.")
        
    def getGamma(self):
        numerator = norm.pdf(self.d1Calculation())
        denominator = self.currentPrice * self.volatility * ((self.yearsToExpiration - self.yearsElapsed)**0.5)

        return numerator/denominator
    
    def getVega(self):
        return self.currentPrice * norm.pdf(self.d1Calculation()) *  ((self.yearsToExpiration - self.yearsElapsed)**0.5)

    def getTheta(self):
        numerator = self.currentPrice * norm.pdf(self.d1Calculation()) * self.volatility
        denominator = 2 * ((self.yearsToExpiration - self.yearsElapsed)**0.5)

        thirdTerm = self.riskFreeRate * self.strikePrice * (np.e**(self.riskFreeRate * (self.yearsToExpiration - self.yearsElapsed))) * norm.cdf(self.d2Calculation())

        if self.optionType == "call":
            return (numerator/denominator) - thirdTerm
        else:
            return (numerator/denominator) + thirdTerm
        
    def getRho(self):
        if self.optionType == "call":
            return self.strikePrice * (self.yearsToExpiration - self.yearsElapsed) * (np.e**(self.riskFreeRate * (self.yearsToExpiration - self.yearsElapsed))) * norm.cdf(self.d2Calculation())
        else:
            return -self.strikePrice * (self.yearsToExpiration - self.yearsElapsed) * (np.e**(self.riskFreeRate * (self.yearsToExpiration - self.yearsElapsed))) * norm.cdf(-self.d2Calculation())
        
        
def main():
    model = blackScholesEquation(75, 85, 1, 0.04, 0.50, 0.5, False, "call")

    print(f'The fair market premium for this option is ${model.priceCalculation():.2f} per share.')
    print(f'The Greeks of this contract are:')
    print(f'Delta - {model.getDelta():.2f}')
    print(f'Gamma - {model.getGamma():.2f}')
    print(f'Vega - {model.getVega():.2f}')
    print(f'Theta - {model.getTheta():.2f}')
    print(f'Rho - {model.getRho():.2f}')


    profitCalc = input("Would you like to calculate your theoretical profit? (y/n)\n")

    while profitCalc == "y":
        price = float(input("Great! Provide the price you believe the asset will be at when the option will be exercised:\n"))
        while price < 0:
            raise ValueError("A price value can't be negative.")
        
        if model.optionType == "call":
            profit = price - model.getStrikePrice() - model.priceCalculation()
        else:
            profit = model.getStrikePrice() - model.priceCalculation()

        
        if profit < 0:
            print(f"At a price of ${price}, ${-profit:.2f} will be lost per share.")
        elif profit > 0:
            print(f"At a price of ${price:.2f}, ${profit:.2f} will be made per share.")
        else:
            print("No profit will be made at this price.")

        profitCalc = input("Would you like to try another theoretical profit calculation? (y/n)\n")

    print("Program closed.")

main()