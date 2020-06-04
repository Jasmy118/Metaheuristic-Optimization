# Traveling SalesMan Problem - Qatar (194 cities)

Data can be retrieved from below link:
http://www.math.uwaterloo.ca/tsp/world/countries.html
or
[qa194tsp.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/qa194tsp.txt)

## Chosen algorithm

I solved this problem with satsp package which uses Simulated Annealing algorithm. Simulated Annealing is a conventional method to obtain the global optimum by adjusting parameters temperature.
https://pypi.org/project/satsp/


## Parameters of the algorithm

city_list: a N*3 matrix containing three columns representing id, x coordinate and y coordinate of the N cities.

start_temp: initial temperature for SA is passed as 1000.

alpha: cooling rate for SA is set at 0.99.

epochs: number of epochs for SA is given as 1000.

epoch_length_factor: the rate at which epoch length increases at each epoch. Should be greater than or equal to 1. This value is passed as 1.02.

## Results

The problem converges to an optimum value at epoch 600.

The best TSP tour length obtained is 9385.531964421118.

The best path chosen is : 1   6   8  16  13  23  25  14  11   7  17  26  24  21  18  28  29  22  27  37  45  57  33  60  69  74  72  78  75  76  87  80  71  82  62  59  36  63  20  65  85  86  98  90  89  94  99 101 104 111 130 127 125 126 132 134 137 140 145 156 149 146 142 138 139 154 157 153 150 144 141 152 147 151 155 162 158 159 165 168 167 170 180 178 181 177 175 173 174 179 172 164 163 161 169 176 182 194 190 187 186 183 184 189 192 191 188 193 185 171 166 160 148 143 136 131 129 135 133 128 124 123 120 121 117 116 115 112 110 100 108 107 105 106 118 122 119 114 113 109 102 103  91  93  96  95  97  92  88  83  79  81  84  77  70  64  68  66  73  67  61  51  39  47  58  56  53  52  48  54  55  49  50  42  44  46  41  38  43  40  34  31  35  32  30  19  15  12  10   9   5   3   2   4

The iterations and output is attached in below links:

[Output.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/output.txt)

[Epochs.txt](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/epochs.txt)

![image2](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/Images/2.png)

![image1](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/Images/1.png)

![image3](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/Images/3.png)

![image4](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/Images/plot194.png)

## Stopping criterion
The stopping criterion, number of epochs is set as 1000.

## Computational time
Time taken to compute the solution is 27.9 minutes.

## Convergence curve
![image5](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Discrete%20Optimization%20Problems/Travelling%20SalesMan%20Problem%20-%20Qatar/Images/convergence194.png)


