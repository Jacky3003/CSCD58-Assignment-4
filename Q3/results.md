# Question 3.(c) of CSCD58 A4

## How to Run the Code
1. First, make sure you are in this current directory.

2. Enter the following in your terminal (for Linux users, running Python scripts may differ from machine, if such is the case, search up how to run Python scripts on your local machine). I use Python 3 for this example, use the Python version in your machine.

    ```Shell
    python3 backoff.py
    ```

3. You will be prompted with the following message: 
    ```
    Enter the number of hosts for the simulation:
    ```
    Be sure to answer with an integer value, don't worry if you make a mistake as the script will catch the excpetion. If this happens, repeat step 2.

4. And another prompt will come after:
    ```
    Enter the number of times you want the simulation to be run:
    ```
    Again, an exception will be caught if you enter a non integral value.

5. You should get the following output (assumming you entered 20 hosts and 1000 trials):
    ```
    Average finish time for 20 hosts and 1000 trials was 11.177.
    ```

6. BONUS: You can also run ```backoff.py``` with exactly three arguments as follows (assuming your current directory has ```backoff.py```):
    ```shell
    python3 backoff.py [hostamount] [trialamount] [seednumber]
    ```

- NOTE: import random uses the Mersenne Twister as its core generator for the random numbers, read more on it in the official documentation:
    ```
    https://docs.python.org/3/library/random.html
    ```

## Finding Average Delay

- For N = 20, we enter 20 hosts and run the simulation around 100,000 times. We get the following average result:
    ```
    Average finish time for 20 hosts and 100000 trials was 11.1687.
    ```

- For N = 40 and 100,000 simulations, we get the following average result:
    ```
    Average finish time for 40 hosts and 100000 trials was 18.82008.
    ```

- For N = 100 and 100,000 simulations, we get the following average result:
    ```
    Average finish time for 100 hosts and 100000 trials was 37.91242.
    ```

- A trend that can be noticed with N is that there is a nonlinear increase in the average delay before one stations transmits for an increasing amount of hosts/stations. This should make sense because the number of hosts (on average/in a perfect world) would be evenly split amongst time slots as the amount of available time slots by our 0 to 2^n-1 range is nonlinear.