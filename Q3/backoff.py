import random
# Class for each host, includes the backoff, retransmission times, and 
# number of collisions for a host.

class host:
    def __init__(self, trialtime: int, numcollisions) -> None:
        self.trialtime = trialtime
        self.numcollisions = numcollisions

    def getbackoff(self, k: int) -> int:
        max = (2**k) - 1
        return random.randint(0, max)

    def update(self, globaltime: int) -> None:
        self.numcollisions += 1
        self.trialtime = self.getbackoff(self.numcollisions) + (globaltime + 1)

# Resets the simulation before each run
def reset() -> None:
    for eachhost in hostlist:
        eachhost.trialtime = 0
        eachhost.numcollisions = 0

# Runs the backoff simulation once, returns the time it took for one host to transmit
# without any collisions.
def runtime() -> int:
    globaltime = 0; reset()
    while True:
        hostcnt: int = 0
        for eachhost in hostlist:
            if eachhost.trialtime == globaltime:
                hostcnt+=1
        if hostcnt == 1:
            return globaltime
        elif hostcnt > 1:
            for eachhost in hostlist:
                if eachhost.trialtime == globaltime:
                    eachhost.update(globaltime)
        globaltime+=1

if __name__ == "__main__":

    # Check that the input is a valid integer value. 
    # "numhosts" is the N value in this question.
    numhosts = input("Enter the number of hosts for the simulation: ")
    runamount = input("Enter the number of times you want the simulation to be run: ")
    try:
        numhosts = int(numhosts)
        runamount = int(runamount)
    except:
        print("input: Not a valid number (try using an integer value).")
        exit()

    # Create the number of hosts required and put them into a single list.
    global hostlist
    hostlist : list[host] = []
    for i in range(0, numhosts):
        newhost: host = host(0, 0)
        hostlist.append(newhost)
    
    # Run the simulation for as many times to get an average value for a set number of hosts.
    cntruns: int = 0; sumruns: int = 0
    while cntruns < runamount:
        sumruns += runtime()
        cntruns+=1
    
    print(f"Average finish time for {numhosts} hosts and {runamount} trials was {float(sumruns/runamount)}.")

