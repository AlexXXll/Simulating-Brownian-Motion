import matplotlib.pyplot as plt
import scipy.stats as stats
# лямбда = 0.9
data = stats.poisson.rvs(mu = 0.9, loc = 0, size = 1000)
plt.figure()
plt.hist(data, T, density = True)
plt.show()