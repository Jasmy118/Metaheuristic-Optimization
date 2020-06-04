# Travelling SalesMan Problem - Djibouti (38 cities)

Data can be retrieved from below link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
or 
[dj38tsp.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/dj38tsp.txt)

## Chosen algorithm

I solved this problem with satsp package which uses Simulated Annealing algorithm.
https://pypi.org/project/satsp/


## Parameters of the algorithm
city_list: a N*3 matrix containing three columns representing id, x coordinate and y coordinate of the N cities. Can be None.

dist_matrix: a N*N matrix containing the distances between the N cities. If None is passed and a None city_list is passed, the program will calculate the Eclidean distances between the cities. If both city_list and dist_matrix are None, a test instance with 48 cities will be solved.

start_temp: initial temperature for SA. If None is passed, the program will estimate the initial temperature using a small sample from the data.

stop_temp: stopping temperature for SA. Can be None.

alpha: cooling rate for SA. If None is passed, the program will calculate alpha if stop_temp and epochs are given. Otherwise alpha is set at 0.99.

epochs: number of epochs for SA. A decisive factor for the running time of the algorithm. The program will terminate after this number of epochs. If None is passed, and stop_temp and alpha are given, the program will calculate number of epochs. Otherwise, the stopping condition will be switched to no improvement after a certain number of epochs, where the number is decided by stopping_count.

epoch_length: number of iterations in each epoch. The default is min(100, N*(N-1) / 2).

epoch_length_factor: the rate at which epoch length increases at each epoch. Should be greater than or equal to 1. Default is 1.00. A small value is recommended for large instances.

stopping_count: the number of epochs after which the program will stop if no improvement is made. This stopping condition is only activated if the number of total epochs is neither specified by the user nor can be calculated by the program. Default is 100. 

screen_output: Parameters of SA, progress of the algorithm and the results will be displayed if set to True. Default is True.

## Results

The stopping criterion, number of epochs is set as 600. The initial temperature is estimated by the program. The cooling rate for Simulated Annealing, alpha is given the default value 0.99.

The problem converges to an optimum value at epoch 580.

The best TSP tour length obtained is 6659.431532931564.

The best path chosen is : 1  2  4  3  5  6  7  8  9 11 12 16 17 18 19 13 15 20 23 26 25 22 24 28 27 31 36 34 33 38 37 35 32 30 29 21 14 10

![image1](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/2.png)
![image2](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/1.png)
![image3](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/3.png)
![image4](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/path.png)

## Stopping criterion
The stopping criterion, number of epochs is set as 600.

## Computational time
Time taken to compute the solution is 15.58 seconds.

## Convergence curve
![image5](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Djibouti/Images/plot.png
