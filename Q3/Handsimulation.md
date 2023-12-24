# Question 3.(a), 3.(b) of CSCD58 A4

## 3.(a)
- We start by simulating our host collisions by hand, the results will be typed in this file.

- First, let the 5 hosts be named as A, B, C, D, and E simmilar to question 1 on this assignment.

- We also need to keep track of the trial number for the experiment specifically for each host so they know when to retrainsmit again. I will refer to this as T.X, where X is the host name, and T is the next retransmission attempt.

- I will use Global.T to represent the global transmission time, so each host knows when to transmit next.

- I will also use a integral random number generator to help perform this experiment to pick the backoff times X.k, where X is any of the 5 hosts. I used the following generator to do this experiment: 

    ```
    https://www.calculator.net/random-number-generator.html
    ```

- Without further ado, lets begin!

### Global.T = 0
- Hosts A, B, C, D, and E all transmit together and end up colliding. We get the following backoff times from the generator, all hosts will sample from backoff values k = {0 or 1}:

- A.k = 0, B.k = 0, C.k = 1, D.k = 1, E.k = 0

- And we also get the following retransmission times:

- A.T = 1, B.T = 1, C.T = 2, D.T = 2, E.T = 1

- That means A, B, and E will retransmit for Global.T = 1, and the rest will retransmit for Global.T = 2

### Global.T = 1

- Hosts A, B, and E will retransmit here and will reach collision with each other.

- All hosts here will sample from backoff values from 0 to 2^2 - 1 since these hosts are on their second collision. See below for the backoff values:

- A.k = 0, B.k = 3, E.k = 1

- And we also get the following retransmission times from adding the backoff to Global.T + 1:

- A.T = 2, B.T = 5, E.T = 4

### Global.T = 2

- Hosts A, C and D will retransmit here and will collide with each other.

- Host A is on its 3rd collision, so it will sample backoff values from 0 to 2^3 - 1

- Host C and D are on their second collision, so they will sample backoff values from 0 to 2^2 - 1

- See below for the newly generated backoff values:

- A.k = 3, C.k = 3, D.k = 0

- And we also get the following retransmission times from adding the backoff values to Global.T + 1:

- A.T = 6, C.T = 6, D.T = 3

### Global.T = 3

- Host D transmits here with no collision from other hosts, one host out of the five waiting hosts have succeeded and we are done.

## 3.(b)

- A key difference of this experiment versus a real ethernet system could be the fact that hosts that are closer together will detect their collisions earlier.

- So if 4 hosts (A, B, C, and D) all transmit at the same time, the actual times that these hosts choose their backoff times will vary, especially if two or three of these four hosts are closer to each other than the remaining hosts.

- Even worse, we could have many hosts close together, but one host far away that could cause the furthest host to be behind when choosing backoff times.