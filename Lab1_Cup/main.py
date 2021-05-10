import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import poisson

class main():
        n = 1000
        Bd = int(input("Введите колличество траекторий Винеровского процесса: "))
        Pd = int(input("Введите колличество траекторий Пуассоновского процесса: "))
        T = 1
        times = np.linspace(0., T, n)
        dt = times[1] - times[0]

        dB = np.sqrt(dt) * np.random.normal(size=(n-1, Bd))
        B0 = np.zeros(shape=(1, Bd))
        B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)

        mu = 0.08
        dP = poisson.rvs(mu, loc=0, size=(n-1, Pd), random_state=None)
        P0 = np.zeros(shape=(1, Pd))
        P = np.concatenate((P0, np.cumsum(dP, axis=0)), axis=0)

        plt.figure(1)
        plt.plot(times, B)
        plt.figure(2)
        plt.step(times, P)
        plt.show()


if __name__ == '__main__':
    main()

