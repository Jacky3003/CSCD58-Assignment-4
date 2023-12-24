# Program to illustrate the values being presented in Fig 1 of A4
import lambdacalc

if __name__ == "__main__":

    numtimes = input("Enter the number of times you want the simulation to run for each lambda:")
    seedval = input("Enter the seed for the PRNG generator: ")

    try:
        numtimes = int(numtimes)
    except:
        print("Invalid number of times entered, please enter an integer.")
        exit()

    lambdacalc.seed(seedval)
    lambdaval: float = 1.0; sumval: float = 0.0
    while lambdaval <= 3.0:
        sumval = 0.0
        for i in range(0, numtimes):
            sumval+=lambdacalc.simulation(lambdaval)
        print(f"lambda = {lambdaval} gives {sumval/numtimes} as the average slot time.")
        lambdaval+=0.1
        lambdaval = round(lambdaval, 1)