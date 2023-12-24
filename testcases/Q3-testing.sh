#!/bin/sh

# Testcases for Q3 of this repository

# Test 1: Running backoff.py with no arguements (be sure to respond to the terminal prompt)

python3 ../Q3/backoff.py

# Test 2: Testing that the program can accept arguements 

python3 ../Q3/backoff.py 10 10 10

# Test 3: Testing that an invalid amount of arguements will fail

python3 ../Q3/backoff.py 10 2
python3 ../Q3/backoff.py 10 2 1 3 10

# Test 4: Large values

