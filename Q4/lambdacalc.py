import random
import math 

# function to specify the seed of the PRNG generator
def seed(i) -> None:
    random.seed(i)

# function to calculate the random variable given, which is x = -lambda*log(u)
def rv(lambdaval: float) -> float:
    u: float = random.random()
    return -math.log(u)*lambdaval

# function to simulate the amount of slot times before a successful transmission, returns the time
# in which the transmission was sent.
def simulation(lambdaval: float) -> float:
    interval: float = rv(lambdaval)
    nextinterval: float = interval + rv(lambdaval)
    previnterval: float = -1.0 # -1 to signify that previous interval does not exist yet
    while previnterval > interval - 1 or nextinterval < interval + 1:
        previnterval = interval
        interval = nextinterval
        nextinterval += rv(lambdaval)
    return interval

if __name__ == "__main__":
    lambdaval = input("Enter the value of lambda that you want to test: ")
    numtimes = input("Enter the number of time you want the simulation to be run: ")
    seedval = input("Enter the seed for the PRNG generator: ")

    try:
        lambdaval = float(lambdaval)
        numtimes = int(numtimes)
    except:
        print("Please enter valid values, float for lambda and int for the number of experiments:")
        exit()
    
    seed(seedval)

    sumval: float = 0.0
    
    for i in range(0, numtimes):
        sumval+=simulation(lambdaval)
    
    print(f"Average number of slot times for given values is {sumval/numtimes}")
