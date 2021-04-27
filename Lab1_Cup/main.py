import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def main():
    n = 10000
    d = int(input("Введите колличество траекторий: "))
    T = 1
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n-1, d))
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)
    P = stats.poisson.rvs(mu = 0.9, loc = 0, size=(n-1,d))
    plt.plot(times, B)
    plt.show()
    plt.figure()
    plt.hist( P, T, density=True)
    plt.show()


if __name__ == '__main__':
    main()

