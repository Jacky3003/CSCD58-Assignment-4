# CSCD58-Assignment-4

- Programming portion for Computer Networks (CSCD58) Assignment 4 done by Jacky Chen. Please see below for a breif description for each question. This repository only contains Q3 and Q4. For more information on CSCD58, please click [here](https://utsc.calendar.utoronto.ca/course/cscd58h3).

- Each question is documented with a ```README.md``` and ```results.md``` file, the latter being in the form of an informal written analysis to hands on questions with regards to the problems investigated.

- ***DISCLAMER***: this mini-project was made for the programming portion of my assignment, but the testcases and additional documentaion are entirely done by my own discretion.

## Q3 - Simulating Ethernet Capture Effect

- This question focuses on doing a hands on experiment with the ***ethernet capture effect***, which can be found [here](https://intronetworks.cs.luc.edu/1/html/ethernet.html#:~:text=The%20capture%20effect%20is%20a,a%20packet%20ready%20to%20transmit.).

- The ```testcases``` folder has different testcases for Q3, feel free to add any as you see fit. There are also additional resources to see the results in [matplotlib](https://matplotlib.org/stable/index.html) for Python (TODO).

- There is also an additional file called ```Handsimulation.md``` that is a hands on activity for actually conducting host colisions when attempting to transmit data.

## Q4 - Simulating Intervals of Transmission

- This question focuses on simulating ethernet transmissions, where the interval between consecutive attempts can be defined using the following random variable:

    $$X = -\lambda log(u)$$
    $$\text{Where u is in the interval } 0 \leq u \leq 1$$

- The current attempt will collide with another attempt if it is close to its slot time.

- Again, the ```testcases``` folder has different testcases for Q4, plus additional resources to see the results in [matplotlib](https://matplotlib.org/stable/index.html) for Python (TODO).