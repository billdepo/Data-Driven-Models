import random

import numpy as np
import matplotlib.pyplot as plt

# Constants
X_t0 = 0
N = 1000
SAMPLE_SIZE = 10000


def coin_flip() -> float:
    prob = random.uniform(0, 1)  # between 0 and 1 uniformly
    return prob


def X_tn_range(n: int) -> np.array:
    coin_flips = [coin_flip() for i in range(n)]  # perform n coin flips
    Y_values = [1 if prob <= 0.5 else -1 for prob in coin_flips]

    current_sum = X_t0
    X_cum_values = np.array(current_sum)  # first element is X_t0
    for y in Y_values:
        current_sum += y
        X_cum_values = np.append(X_cum_values, current_sum + y)

    return X_cum_values


def sample_of_X_tn(n: int, sample_size: int) -> np.array:
    all_series = X_tn_range(n)  # first random walk instance
    for i in range(sample_size-1):
        X_tn_series = X_tn_range(n)
        all_series = np.vstack((all_series, X_tn_series))
    return all_series


def get_sample_mean(A: np.array) -> np.array:
    return A.mean(axis=0)  # mean for each timestep across the different sample instances


def get_sample_var(A: np.array) -> np.array:
    return A.var(axis=0)  # variance


def plot_random_walks(x: int, n_range: int, A: np.array) -> None:
    plt.figure()

    for i in range(x):
        X_tn_series = A[i]
        plt.plot(n_range, X_tn_series, label=f'n={i}', linewidth=1)

    plt.title('First three random walks values vs n')
    plt.xlabel('n')
    plt.ylabel('$X(t_n)$')
    plt.legend()
    plt.savefig('First-three-random-walks.png')


def plot_single_line(n_range: int, A: np.array, title: str, ylabel: str, filename: str) -> None:
    plt.figure()
    plt.plot(n_range, A, linewidth=1)
    plt.title(f'{title}')
    plt.xlabel('n')
    plt.ylabel(ylabel)
    plt.savefig(f'{filename}.png')


if __name__ == '__main__':
    n_range = np.arange(0, N+1)  # all 0 to 1000 number in a numpy array

    sample: np.array = sample_of_X_tn(N, SAMPLE_SIZE)
    sample_mean: np.array = get_sample_mean(sample)
    sample_var: np.array = get_sample_var(sample)

    plot_random_walks(3, n_range, sample)
    plot_single_line(n_range,
                     sample_mean,
                     title=f'Mean of {int(SAMPLE_SIZE):.0e} $X(t_n)$ random walks',
                     ylabel='$E[X(t_n)]$',
                     filename='Mean')
    plot_single_line(n_range,
                     sample_var,
                     title=f'Variance of {int(SAMPLE_SIZE):.0e} $X(t_n)$ random walks',
                     ylabel='$Var[X(t_n)]$',
                     filename='Variance')
