# Question 4 of CSCD58 A4

## How to Run the Code
1. First, make sure you are in the current directory.

2. Enter the following in your terminal (for Linux users, running Python scripts may differ from machine, if such is the case, search up how to run Python scripts on your local machine). I use Python 3 for this example, use the Python version in your machine.

    ```
    python3 lambdacalc.py
    ```
3. You will be prompted with the following message: 
    ```
    Enter the value of lambda that you want to test:
    ```
    Be sure to answer with a valid value, don't worry if you make a mistake as the script will catch the excpetion. If this happens, repeat step 2.

4. And another prompt will come after:
    ```
    Enter the number of times you want the simulation to be run:
    ```
    Again, an exception will be caught if you enter a non valid value.

5. The final prompt will ask you for the seed of the PRNG, note that the random module in Python
uses Mersenne Twister as its PRNG module:
    ```
    Enter the seed for the PRNG generator:
    ```

6. You should get the following sample output (for a PRNG of 234, 100000 runs, and a lambda of 1.0):
    ```
    Average number of slot times for given values is 6.386829672173832
    ```

7. BONUS: the script lambdatest.py can be ran with simmilar instructions, but instead gives an output that approximately reflects Fig 1 given in A4. 

## General Results:

- By using lambdatest.py to set the number of runs to 1,000,000 and the PRNG seed to 10, we then get the following output:

    ```
    lambda = 1.0 gives 6.384187291569054 as the average slot time.
    lambda = 1.1 gives 5.776594817829071 as the average slot time.
    lambda = 1.2 gives 5.3514189461684865 as the average slot time.
    lambda = 1.3 gives 5.050339711690474 as the average slot time.
    lambda = 1.4 gives 4.84179467667187 as the average slot time.
    lambda = 1.5 gives 4.695474452074307 as the average slot time.
    lambda = 1.6 gives 4.58125508199448 as the average slot time.
    lambda = 1.7 gives 4.505246336709513 as the average slot time.
    lambda = 1.8 gives 4.464561092857288 as the average slot time.
    lambda = 1.9 gives 4.44346657661625 as the average slot time.
    lambda = 2.0 gives 4.438022614165831 as the average slot time.
    lambda = 2.1 gives 4.4414405442606215 as the average slot time.
    lambda = 2.2 gives 4.45947812035877 as the average slot time.
    lambda = 2.3 gives 4.488211216113726 as the average slot time.
    lambda = 2.4 gives 4.5189992279436755 as the average slot time.
    lambda = 2.5 gives 4.561736545471605 as the average slot time.
    lambda = 2.6 gives 4.613482248147854 as the average slot time.
    lambda = 2.7 gives 4.659486685004927 as the average slot time.
    lambda = 2.8 gives 4.711164393972848 as the average slot time.
    lambda = 2.9 gives 4.7762081939739724 as the average slot time.
    lambda = 3.0 gives 4.836870882840236 as the average slot time.
    ```

- The minimum value for the contention interval by looking at our output is around where lambda = 2.0. The value itself is around 4.438022614165831 slot times until a successful transmission is sent.

- If we suppose that the average transmission lasts around 8 slot times, then for the minimum contention period we get (approximately):

    $$\frac{8}{8+4.438} = 0.648$$

- Or around 64.8% bandwidth usage, the sum of the time for each transmission and the minimum average contention interval is the total time used for the transmission + colision dealing.

- So all we need to do is divide the 8 seconds of transmission time by the total time it takes for frames to the transported on the network, which is transmit time + colision dealing time.