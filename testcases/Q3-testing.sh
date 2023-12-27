#!/bin/sh

# Testcases for Q3 of this repository

# Test 1: Running backoff.py with no arguements (be sure to respond to the terminal prompt)
# Uncomment if you want to test this on your own

#python3 ../Q3/backoff.py

# Test 2: Testing that the program can accept arguements 

python3 ../Q3/backoff.py 10 10 10

# Test 3: Testing that an invalid amount of arguements will fail

python3 ../Q3/backoff.py 10 2
python3 ../Q3/backoff.py 10 2 1 3 10

# Test 4: Large values

python3 ../Q3/backoff.py 100 100 5

# Test 5: Small amount of hosts, with many trials

python3 ../Q3/backoff.py 2 10000 5

# Test 6: Many hosts, small amount of trials

python3 ../Q3/backoff.py 100000 2 5

# Test 7: Larger values, may take a long time to run
# Uncomment if you want to test this on your own

#python3 ../Q3/backoff.py 10000 10000 93
