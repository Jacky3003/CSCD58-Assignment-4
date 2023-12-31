#!/bin/sh

# Testcases for Q3 of this repository

# Test 1: Running backoff.py with no arguements (be sure to respond to the terminal prompt)
# Uncomment if you want to test this on your own, you should also verify this on your own.

#python3 ../Q3/backoff.py

# Test 2: Testing that the program can accept arguements
correct="Average finish time for 10 hosts and 10 trials was 5.4."
test2="$(python3 ../Q3/backoff.py 10 10 10)"
# echo $test2
if [ "$correct" = "$test2" ]; then
    echo "Test case 2 passed."
else
    echo "Test case 2 failed."
fi

# Test 3: Testing that an invalid amount of arguements will fail
correct="input: not enough or too much arguements given to the program."

test31="$(python3 ../Q3/backoff.py 10 2)"
echo $test31
if [ "$correct" = "$test31" ]; then
    echo "Test case 3.1 passed."
else
    echo "Test case 3.1 failed."
fi

test32="$(python3 ../Q3/backoff.py 10 2 1 3 10)"
echo $test32
if [ "$correct" = "$test32" ]; then
    echo "Test case 3.2 passed."
else
    echo "Test case 3.2 failed."
fi

# Test 4: Large values
correct="Average finish time for 100 hosts and 100 trials was 38.0."
test4="$(python3 ../Q3/backoff.py 100 100 5)"
echo $test4
if [ "$correct" = "$test4" ]; then
    echo "Test case 4 passed."
else
    echo "Test case 4 failed."
fi

# Test 5: Small amount of hosts, with many trials
correct="Average finish time for 2 hosts and 10000 trials was 2.7248."
test5="$(python3 ../Q3/backoff.py 2 10000 5)"
echo $test5
if [ "$correct" = "$test5" ]; then
    echo "Test case 5 passed."
else
    echo "Test case 5 failed."
fi

# Test 6: Many hosts, small amount of trials
correct="Average finish time for 10000 hosts and 2 trials was 1800.0."
test6="$(python3 ../Q3/backoff.py 10000 2 5)"
echo $test6
if [ "$correct" = "$test6" ]; then
    echo "Test case 6 passed."
else
    echo "Test case 6 failed."
fi

# Test 7: Larger values, may take a long time to run
# Uncomment if you want to test this on your own (WARNING: It takes a long time to run)

#python3 ../Q3/backoff.py 10000 10000 93
