# Data-Driven Models in Engineering Problems

2nd semester course of <a href="https://dsml.ece.ntua.gr/studies/courses/montela-odegoymena-apo-ta-dedomena-se-problemata-mechanikoy">Data Science and Machine Learning MSc program</a> of National Technical University of Athens.

Course description: \
<i>Sensor data (types, spatial and temporal coverage). Data categorisation and information retrieval; correlation structures. Fourier and Principal Component analysis. Analysis of data from fixed sensors. Analysis of data from moving sensors. Processing of data from mobile phone sensors (smartphone orientation, data cleaning, filtering, fusion, dimensionality reduction, feature engineering). Probabilistic machine learning methods such as Markov, Kriging, Polynomial Chaos etc. Modelling by reduction to reduced order parametric spaces (reduced order models). Applications to engineering problems.
</i>

The course includes 4 assignments containing both analytical and programming tasks.
## Assignment 0 - Random Walks
Random walk sample generation. Estimation of Expected Value and Variance and proof that the process is not ergodic. 

Short problem description:
Random walk $X(t_n)$ with the properties:
- Each sample starts from zero at at $t_0=0$
- Consists of 1000 time steps
- The probability at each step to go up or down is equal

Prove that: 
- $E\left[ X(t_n) \right] = 0 $
- $Var\left[ X(t_n) \right] = n $

The process is not ergodic.

## Assignment 1 - Series Expansion of Stochastic Processes
The assignment consists of two parts.

1. A stochastic field $E(x)$ is given that is dependent on a zero-mean stationary Gaussian field $f(x)$ with unit variance. The autocorrelation function $R_f(\tau)$ for $f$ is known and the following are requested:
    - Usage of the *Karhunen-Loeve* (KL) series expansion method to generate a number of realizations of the field $E(x)$.
    - Justification of the number of terms retained in the KL-expansion.
    - Esemble average and variance calculation from the realization. Convergence of ensemble average and variance as $N$ increases.
2. A zero-mean Gausian process $X(t)$ is given along with its one-sided power spectrum $G(\omega)$.
    - Using the *Spectral Representation* method, a number of time-histories (realizations) of the process $X(t)$ is generated.
    - The ensembe average and variance is calculated from the realizations and convergence is studied as $N number of realizations increases.
    - Calculation of temporal average and variance from a single realization and commentary of observations.

## Assignment 2 - Monte Carlo Simulation and Stochastic Finite Element Method
A rectangular plate that is heated in a single position by a candle is given along with the steady state equation that describes the temperature field $T(x,y)$ along the plate at thermal equilibrium. 

1. The plate gets discretized to a grid and the finite difference scheme is found. Then a linear system of equations $K \cdot t = b$ is derived.
2. A Monte Carlo simulation is performed to obtain the probability density function of the temperature at the midpoint of the plate.
3. A smaller number of deterministic simulations is performed initially to derive an initial dataset. Then the PCA/POD method is used for dimensionality reduction of the linear system that describes the problem. Finally, a Monte Carlo simulation is performed on the reduced system and the pdf derived is compared with the previous question.

## Assignment 3 - Outliers Detection
Extreme turning movements for a car are identified based on data of a driver's smartphone (accelerometer, gyroscope and GPS) for a number of trips. Feature engineering and a number of methods (statistical, distance-based, density-based, tree-based, time-series) are employed in order to detect outliers in the data and classify them as extreme turning movement events.