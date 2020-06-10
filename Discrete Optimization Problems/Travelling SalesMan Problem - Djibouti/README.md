# Travelling SalesMan Problem - Djibouti (38 cities)

Data can be retrieved from below link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
or 
[dj38tsp.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/dj38tsp.txt)

*Code Here* : [dj38TSP.py](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/dj38TSP.py)

## Chosen algorithm

This problem is solved with satsp package which uses Simulated Annealing algorithm.
https://pypi.org/project/satsp/


## Parameters of the algorithm

city_list: a N*3 matrix containing three columns representing id, x coordinate and y coordinate of the N cities.

start_temp: initial temperature for SA is estimated by the program.(None is passed).

alpha: cooling rate for SA is set at 0.99.

epochs: number of epochs for SA. A decisive factor for the running time of the algorithm. The program will terminate after this number of epochs. It is given as 600.

## Results

The problem converges to an optimum value at epoch 580.

The best TSP tour length obtained is 6659.431532931564.

The best path chosen is : 1  2  4  3  5  6  7  8  9 11 12 16 17 18 19 13 15 20 23 26 25 22 24 28 27 31 36 34 33 38 37 35 32 30 29 21 14 10

The iterations and output is attached in below links:

[Output.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/output.txt)

[Epochs.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/epochs.txt)

![image1](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/2.png)
![image2](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/1.png)
![image3](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/3.png)
![image4](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/path.png)

## Stopping criterion
The stopping criterion, number of epochs is set as 600.

## Computational time
Time taken to compute the solution is 15.58 seconds.

## Convergence curve
![image5](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/plot.png)
