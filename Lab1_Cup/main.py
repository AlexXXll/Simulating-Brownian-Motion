import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def main():
    n = 1000
    d = int(input("Введите колличество траекторий: "))
    T = 1
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n-1, d))
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)
    mu = np.random.normal(size=(0, n))
    distr = stats.poisson(mu=mu)
    x = np.arange(d)
    plt.plot(times, B)
    plt.show()
    plt.figure()
    plt.vlines(x,0,distr.pmf(x))
    plt.show()


if __name__ == '__main__':
    main()

