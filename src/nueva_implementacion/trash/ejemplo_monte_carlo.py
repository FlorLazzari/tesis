from __future__ import division
import scipy.stats as stats
import seaborn as sns
import os
import sys
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# matplotlib inline
# precision 4
plt.style.use('ggplot')

x = np.linspace(0, 1, 100)
plt.plot(x, np.exp(x));
pts = np.random.uniform(0,1,(100, 2))
pts[:, 1] *= np.e
plt.scatter(pts[:, 0], pts[:, 1])
plt.xlim([0,1])
plt.ylim([0, np.e]);
plt.show()

# Check analytic solution
from sympy import symbols, integrate, exp

x = symbols('x')
expr = integrate(exp(x), (x,0,1))
expr.evalf()
print(expr.evalf())
# Using numerical quadrature
# You may recall elementary versions such as the
# trapezoidal and Simpson's rules
# Note that nuerical quadrature needs $n^p$ grid points
# in $p$ dimensions to maintain the same accuracy
# This is known as the curse of dimensionality and explains
# why quadrature is not used for high-dimensional integration

from scipy import integrate
integrate.quad(exp, 0, 1)

# Monte Carlo approximation
n in 10**np.array([1,2,3,4,5,6,7,8]):
        pts = np.random.uniform(0, 1, (n, 2))
        pts[:, 1] *= np.e
        count = np.sum(pts[:, 1] < np.exp(pts[:, 0]))
        volume = np.e * 1 # volume of region
        sol = (volume * count)/n
        print '%10d %.6f' % (n, sol)

# ejemplo en c:
# int i;
# long double throws = 99999, circleDarts = 0, randX, randY, pi;
# srand(time(NULL));
# for (i = 0; i < throws; ++i) {
#   randX = rand() / (double)RAND_MAX;
#   randY = rand() / (double)RAND_MAX;
#   if (1 > ((randX*randX) + (randY*randY))) ++circleDarts;
# }
# pi = 4 * (circleDarts/throws);
