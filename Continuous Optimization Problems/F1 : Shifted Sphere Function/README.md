# F1: Shifted Sphere Function

![$F_1(X) = \sum_{i=1}^D z_i^2 + f\_bias_1 \ , Z = X-O \ , X=\[x_1,x_2,...,x_D\]$](https://render.githubusercontent.com/render/math?math=%24F_1(X)%20%3D%20%5Csum_%7Bi%3D1%7D%5ED%20z_i%5E2%20%2B%20f%5C_bias_1%20%5C%20%2C%20Z%20%3D%20X-O%20%5C%20%2C%20X%3D%5Bx_1%2Cx_2%2C...%2Cx_D%5D%24)

![$D: dimensions.$](https://render.githubusercontent.com/render/math?math=%24D%3A%20dimensions.%24)

![$O=\[o_1, o_2,...,o_D\]$](https://render.githubusercontent.com/render/math?math=%24O%3D%5Bo_1%2C%20o_2%2C...%2Co_D%5D%24) : the shifted global optimum

The optimum of the solution is calculated for dimensions 50 and 500 with a boundary limit of ![$X \in \[-100,100\]^D$](https://render.githubusercontent.com/render/math?math=%24X%20%5Cin%20%5B-100%2C100%5D%5ED%24)

Global optimum: ![$X^* = O , F_1(X^*) = f\_bias_1 = - 450$](https://render.githubusercontent.com/render/math?math=%24X%5E*%20%3D%20O%20%2C%20F_1(X%5E*)%20%3D%20f%5C_bias_1%20%3D%20-%20450%24)

![image11](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Images/1.png)

*Code Here* : [ShiftedSphere.py](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/ShiftedSphere.py)

## Chosen algorithm

The optimum was found using CMA-ES (covariance matrix adaptation evolution strategy) algorithm and differential evolution. But more time was required for differential evolution algorithm.

http://cma.gforge.inria.fr/cmaes_sourcecode_page.html#python

## Parameters of the algorithm
For the CMA-ES algorithm, the initial solution was set as 0 with an initial standard deviation(sigma0) of 1. All other parameters are left as the default values. Default values as below:

- population size, popsize = ![$4+int(3*np.log(Dimension))$](https://render.githubusercontent.com/render/math?math=%244%2Bint(3*np.log(Dimension))%24)
- maximum number of function evaluations, maxfevals = inf
- maximum number of iterations, maxiter = ![$100 + 150 * (N+3)^2 // popsize^0.5$](https://render.githubusercontent.com/render/math?math=%24100%20%2B%20150%20*%20(N%2B3)%5E2%20%2F%2F%20popsize%5E0.5%24)
- termination criterion: tolerance in x-changes, tolx = 1e-11
- termination criterion: tolerance in function value, tolfun = 1e-11

## Results
Even though the number of iterations required by differential evolution is less it takes more time to converge compared to cma-es. 

The outputs and epochs using CMA-ES algorithm in 50 and 500 dimension can be found in below link:

[CMAES_Output_50](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/CMAES/cmaes_output_50.txt)       ||      [CMAES_Epochs_50](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/CMAES/cmaes_epochs_50.txt)

[CMAES_Output_500](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/CMAES/cmaes_output_500.txt) ||  [CMAES_Epochs_500](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/CMAES/cmaes_epochs_500.txt)

The details of the results are as below:

### CMA-ES in 50D
Time taken to compute the optimum :  10.38 seconds

Number of iterations done :  894

Optimum value of function :  -449.9999999999999

Optimum values of x :  

[ 97.2499359   77.06098494 -19.03114881  25.42869792 -22.90880258
  69.5721758    5.36971386  61.48073078 -21.3006986   92.3468134
 -93.97588118  90.7459868   42.87698031  29.30964636 -10.6695484
 -65.07461778  67.04941631  94.01877031 -73.00502026 -49.80219859
  82.00142505  35.29318281  24.63214925   2.44313745 -99.30345088
 -54.62233888  95.69145816  72.25048083 -97.12295528  -2.84462702
 -16.719407    54.58048354  -2.37049342   4.51291375  56.40988584
  18.24586948 -74.72144478 -78.05614659  32.58107767  99.41862302
 -30.76381164 -64.7890968  -86.42220779 -38.12082256 -33.04804034
 -24.76648648  90.44136626  43.86410232  55.86848702  23.53173234]
 
 
### CMA-ES in 500D
Time taken to compute the optimum :  247.66 seconds (4.13 minutes)

Number of iterations done :  6424

Optimum value of function :  -449.9999999999993

Optimum values of x :

[ 9.72499359e+01  7.70609850e+01 -1.90311489e+01  2.54286980e+01 -2.29088026e+01  6.95721757e+01  5.36971390e+00  6.14807307e+01 -2.13006985e+01  9.23468134e+01 -9.39758812e+01  9.07459867e+01  4.28769803e+01  2.93096463e+01 -1.06695484e+01 -6.50746178e+01  6.70494163e+01  9.40187703e+01 -7.30050201e+01 -4.98021985e+01  8.20014250e+01  3.52931827e+01  2.46321492e+01  2.44313746e+00 -9.93034509e+01 -5.46223388e+01  9.56914582e+01  7.22504808e+01 -9.71229552e+01 -2.84462703e+00 -1.67194070e+01  5.45804836e+01 -2.37049344e+00  4.51291384e+00  5.64098858e+01  1.82458696e+01 -7.47214448e+01 -7.80561465e+01  3.25810776e+01  9.94186228e+01 -3.07638117e+01 -6.47890969e+01 -8.64222077e+01 -3.81208227e+01 -3.30480404e+01 -2.47664865e+01  9.04413663e+01  4.38641022e+01  5.58684871e+01  2.35317323e+01  2.98476668e+01  5.12566610e+01 -7.04331622e+01  1.98907355e+01  7.97217378e+01 -6.56134289e+01  6.37856216e+01 -8.61412482e+01  9.11374524e+01 -3.65324325e+01 -9.89597654e+01  5.19871014e+01 -3.82640361e+01  4.30511350e+01 -8.38104963e+01  6.91755848e+01  4.36752407e+01  7.40785997e+01  7.44319385e+01  5.23126448e+01  3.38912918e+01  8.04056543e+01  6.42924640e+01  6.65314539e+01  2.79835867e+01 -6.87591355e+01  5.66335889e+01  4.62810796e+01  1.29463920e+01  4.46698519e+01 -5.20523808e+01 -2.02829328e+00 -1.52794639e+01  5.91355104e+01  5.26819970e+01 -5.22222388e+01  2.70218659e+01 -5.36909573e+01  2.31876362e+01 -4.62990895e+01  9.82426296e+01  5.20637746e+01 -3.56652612e+00  8.90400672e+01 -2.78523461e+01 -8.31217928e+01  8.97027065e+01  3.81654977e+01  2.31017174e+01  7.89956118e+01 -9.74923578e+01 -3.98175925e+01  9.30161516e+01 -7.95818937e+01  1.92043452e+01 -6.20446460e+00  4.34651279e+01  7.17741866e+01 -6.28803181e+01 -7.52500586e+00  8.06599519e+01 -9.55790982e+01  5.20812307e+01  5.91703999e+01 -3.72298187e+01 -5.28349606e+01 -1.10964325e+00  3.70508912e+01  8.89267388e+01 -1.21376164e+01 -5.13129532e-01 -8.02764153e+01  1.08875030e+01 -1.28611361e+01 -6.37470854e+01 -6.92376377e+01  8.67458757e+01 -7.27468780e+01  9.97089994e+01  3.81241253e+01  9.22084912e+01  5.51003014e+01 -9.98551732e+01 -3.49057177e+01  8.82072628e+00 -3.86987362e+01  3.45407780e+01 -3.08573357e+01  9.61198833e+01 -2.92063380e+01 -9.60969043e+01  6.25504103e+01  9.65628875e+01 -3.76328383e+01 -2.42183136e+01  4.96058895e+01 -1.14339846e+01 -8.00216999e+01  9.85244902e+01  7.25239183e+00 -7.30904063e+01 -7.37399991e+01  7.27987361e+01  4.16544970e+01  9.96481396e+01  6.31513833e+01  5.64479730e+01  5.27231498e+01  8.09950485e+01 -7.93756258e+01 -5.76579249e+01  7.02177238e+01  4.85930321e+01 -1.89857999e+01 -3.89916375e+01 -5.16100520e+00 -7.10524668e+01 -1.13197000e+00  6.02484758e+00  2.04848516e+00 -5.45061691e+01  8.69987829e+01  3.53841689e+00 -8.14781923e+00  5.53475980e+01  4.67606491e+01  2.04763849e+01 -8.86141939e+01 -8.55993602e+01  2.71363270e+01  7.52667645e+01 -1.45041114e+01  4.16806839e+01 -8.59619759e+01 -9.61869677e+01  1.66197114e+00  7.38811985e+01  5.97098023e+01  5.98468112e+01 -6.07773399e+01  4.28748748e+01 -5.69983148e+01  5.73014841e+01 -6.55704947e+01 -5.87705540e+01 -7.10516184e+00 -8.50946991e+01  1.93161020e+01 -6.18019064e+01  8.69634732e+01 -3.84974988e+01 -7.62157595e+00  6.59506566e+01 -3.99724988e+01  4.19239703e+01 -8.50797851e+01  5.00431625e+01 -6.21891953e+00  8.89827930e+01 -9.72052204e+01 -8.91602310e+01  4.76897734e+01  2.71130162e+01  8.61944393e+01 -7.80787892e+00  2.57798873e+00 -1.51037774e+01 -1.68166127e+01 -2.23531432e+01  7.11074417e+01  6.46037824e+01  8.27820695e+01  6.72083883e+01  7.36175174e+01  5.51174512e+01 -1.36144152e+01 -1.27804028e+01 -5.51390547e+01 -9.73631320e+01 -2.48067500e+01  6.77124622e+01 -4.27513325e+01 -4.31741743e+01 -3.45839310e+01 -4.75814796e+00 -5.48033309e+01  9.24012391e+01 -3.87083549e+01  5.57851171e+01  7.90684887e+01 -4.92553363e+01 -7.08493326e+01 -3.17007455e+01  4.66269371e+01 -9.32272174e+01  8.84775198e+00  1.16890801e+01  3.39367445e+01  1.67853844e+01  3.71818178e+01  5.31967736e+01  7.95324231e+01  9.33579341e+01  8.11587058e+01 -6.42841228e+01  9.56976055e+01  7.95971485e+01 -9.41277194e+01 -4.35955288e+01 -6.24197703e+01  2.17507018e+01 -5.81291234e+01  9.95469327e+01 -9.66476359e+01 -1.20743678e+01 -7.03209621e+01  2.42891873e+01  5.08737570e+01 -4.38806095e+01  5.43593637e+00 -3.75118841e+01 -6.36518264e+01  5.58505888e+01  6.19018125e+01  4.46625892e+01 -9.09381021e+01  2.26599501e+01 -3.29570222e+01  1.67725189e+01  8.26355623e+01  2.54499213e-01 -1.64980913e+01  5.98915009e+01  7.81218323e+01  2.67066644e+00 -2.20547076e+01  8.61277403e+01 -4.34535700e+01  5.39874286e+01  4.55166425e+01  8.29215995e+01 -7.87759175e+01  7.77875221e+01  1.90080893e+01 -9.75840089e+01 -5.23371247e+01 -7.52752295e+01  7.61568628e+01  6.26464553e+01  5.26676610e+01  6.20774144e+01  3.64507735e+01  2.49604139e+01 -2.63842917e+01 -5.94439573e+01 -4.49897572e+01 -3.69122690e+00 -1.99617511e+01  4.04591669e+01 -3.57278104e+01 -9.03093668e+01  5.54972355e+01  1.06805746e+01 -8.64501300e+01 -7.64699783e-01  6.72210354e+01 -7.81317963e+00  5.60050804e+01 -1.65122656e+00  3.91427921e+01  9.70123806e+01 -2.93655481e+01  2.43983342e+01  3.17875094e+00  6.30064542e+01 -2.18720120e+00  4.62919131e+01  4.21148983e+01  6.68823267e+01 -9.78151645e+01 -9.03245933e+01  2.53468733e-01 -4.16621361e+01 -9.72414679e+01  5.88355695e+01 -8.65434654e+01 -3.79644303e+01 -3.19989167e+01  6.33555829e+01 -9.91254320e+01 -1.23679567e+00  2.26896082e+01 -2.51837592e+01 -6.03383598e+01  7.90135285e+01  9.73697166e+01  8.43560184e+01 -2.11165320e+01  3.24574960e+01  8.02198202e+00 -5.77841039e+01 -3.89340180e+01 -9.73195222e+01 -9.90876117e+01  9.75573822e+01  6.23593871e+01  5.40811381e+01  8.06570498e+01 -7.52451768e+01 -8.07840912e+01  1.02935129e+01 -9.86964822e+01 -7.48613403e+01 -8.88440138e+01  5.25347410e+01 -8.57196882e+01  4.36466705e+01 -7.19184006e+01  2.31396712e+01 -5.69816186e+00  2.07051432e+00 -3.09913848e+01 -8.30484073e+01 -4.88397308e+01  5.11437938e+00 -7.18930476e+01 -7.59058157e+01  5.47775061e-01 -4.28173577e+01 -7.76065606e+01  9.25288666e-03 -2.44198035e+01 -4.58882372e+01  9.13382052e+01 -8.38641293e+00 -5.09958826e+01  6.60914144e+01 -3.93652556e+01 -9.33561169e+01  9.75118638e+01 -4.04474934e+00  2.07071610e+01  3.24976075e+00  9.54521933e+01 -5.05603381e+01  3.36389167e+01 -7.06536762e+01 -1.89755340e+01 -7.15894264e+01 -3.11507967e+01  9.98641320e+00 -9.15136588e+01 -5.36080254e+01 -2.02418617e+01 -7.58617994e+01 -1.14739854e+01 -8.97095371e+01  9.93293236e+01  3.88752687e+01  2.30043346e+01  2.34309209e+01  6.59478367e+01  9.58571138e+01 -1.25130508e+01  6.92420669e+01 -2.05832728e+01 -1.59256398e+01  7.83976212e+01 -3.08676592e+01  6.16825905e+01  9.88552537e+01  5.62127503e+01  7.03617505e+01  3.21222067e+01 -4.55774503e+01 -5.18313535e+01 -1.48152802e+01  1.95116252e+01 -1.59917605e+01  5.35048312e+01 -9.48616574e+01  3.85586054e+01  5.06876465e+01  9.07115850e+01 -2.25355849e+01 -8.87687327e+01 -2.49319606e+01  3.15026358e+01  4.03533029e+01 -8.18526350e+01  8.95974178e+01  6.96976914e+00  8.20480760e+01 -3.81378251e+01  4.49790026e+01 -2.33082138e+01  7.97746125e+01 -8.63123881e+01 -4.70000661e+01  2.49122444e+01  3.60558274e+01  4.73801689e+01  8.65961091e+01  2.29342263e+01  4.76610213e+01  2.73051788e+01 -6.59733561e+01 -4.55328833e+01  6.24895598e+01 -1.93478069e+01  3.20165359e+01 -4.27882027e+01  9.22766815e+01  1.53111981e+01  9.33257655e+01  2.78418899e+00  7.28446634e+01 -5.49344985e+01 -5.13089937e+01  7.97652857e+01  4.18395157e+01  9.50286837e+01 -8.08714820e+00  4.83549124e+01  3.37934490e+01 -9.40775106e+01 -2.99287792e+01 -8.35867745e+01 -8.78325047e+01  5.20189886e+01  2.55661785e+01  6.09339204e+00  9.78523787e+01 -3.94075819e+01 -6.38597494e+01  1.38500188e+01 -6.68558329e+00 -2.15541733e+01 -9.45186325e+01 -3.17040942e+01  9.52698206e+01  1.53870003e+01  5.41280254e+01  2.52822929e+01  4.66099911e+01 -7.01317299e+01 -1.70717802e+01 -8.62030524e+01  7.68388125e+01  6.63988584e+01]


## Number of function evaluations
The function evaluations (Fevals) are done from 22 to 141328 using cma-es in 500D and from 15 to 13410 in 50D. The maximum number of function evaluations (maxfevals) is left as the default value (inf).

## Stopping criterion
- termination criterion: tolerance in x-changes, tolx = 1e-11
- termination criterion: tolerance in function value, tolfun = 1e-11
- maximum number of iterations, maxiter = ![$100 + 150 * (N+3)^2 // popsize^0.5$](https://render.githubusercontent.com/render/math?math=%24100%20%2B%20150%20*%20(N%2B3)%5E2%20%2F%2F%20popsize%5E0.5%24)

For both 50D and 500D, the optimization was stopped by the criterion tolflatfitness (iterations tolerated with flat fitness before termination) = 1

## Computational time
Time taken to compute the optimum CMA-ES 50D :  10.38 seconds

Time taken to compute the optimum CMA-ES 500D :  247.66 seconds (4.13 minutes)

## Convergence curve

### CMA-ES 50D
![image1](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Images/cmaes_50.jpg)

### CMA-ES 500D
![image1](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Images/cmaes_500.jpg)

### *Differential Evolution Trial*
(scipy.optimize.differential_evolution)

Differential Evolution required more time to converge even though number of iterations was less.

In 50D maximum iteration (maxiter) of 500, relative tolerance for convergence (tol) of 1e-4 and recombination constant or crossover probability (recombination) of 0.8 are given. For 500D, all the parameters are given the same except for iteration as 2000.

**Results** :

[DE_Output_50](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/DE/de_output_50.txt)  ||  [DE_Epochs_50](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/DE/de_epochs_50.txt)

[DE_Output_500](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/DE/de_output_500.txt)  ||  [DE_Epochs_500](https://github.com/Jasmy118/Metaheuristic-Optimization/blob/master/Continuous%20Optimization%20Problems/F1%20:%20Shifted%20Sphere%20Function/Outputs/DE/de_epochs_500.txt)

**DE in 50D**

Time taken to compute the optimum :  21.62 seconds

Message :  Optimization terminated successfully.

Number of iterations done :  245

Optimum value of function :  -449.99999999995885

**DE in 500D**

Time taken to compute the optimum :  11351.21 seconds (3.15 hrs)

Message :  Maximum number of iterations has been exceeded.

Number of iterations done :  2000

Optimum value of function :  -449.9999999995561
