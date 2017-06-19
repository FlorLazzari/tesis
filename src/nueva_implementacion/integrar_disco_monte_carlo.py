from __future__ import division
import numpy as np

# integral de montecarlo
# https://en.wikipedia.org/wiki/Monte_Carlo_integration                ==> Monte Carlo (wiki)
# https://people.duke.edu/~ccc14/sta-663/MonteCarlo.html               ==> Monte Carlo + python
#
#
# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html   ==> numerical integration (quadrature)


# coment/arios:

# I certainly did not write this code for any practical purpose. Monte Carlo is probably
# the most inefficient solution method for almost any problem. I only put it here thinking
# some people may find it interesting, that's all.
#
# For higher-dimensional integrals, Monte Carlo is often the tool of choice. Yes, it's inefficient
# for single integrals, but it's a great thing for students to look at because a) it's simple
# to understand (no need of calculus) and b) it's easy to code.
#
# The convergence of Monte Carlo integration is 0(n1/2) and independent of the dimensionality.
# Hence Monte Carlo integration gnereally beats numerical intergration for moderate- and high-dimensional
# integration since numerical integration (quadrature) converges as 0(nd). Even for low dimensional problems,
# Monte Carlo integration may have an advantage when the volume to be integrated is concentrated in a very
# small region and we can use information from the distribution to draw samples more often in the region of importance.

# Monte Carlo approximation


def integrar_disco_monte_carlo(n,f,d_0):
    count = 0
    for i in range(n):
        rand_y = np.random.uniform(0, d_0/2)
        rand_z = np.random.uniform(0, d_0/2)
        if (rand_y**2 + rand_z**2 < d_0/2):
            count = count + f(rand_y, rand_z)
    volume = (d_0/2)**2
    return (volume * count)/n

# ejemplo:
n = 10**6                             # como elijo el n apropiadamente?
def f(y,z):
    return 1
d_0 = 2

sol = integrar_disco_monte_carlo(n,f,d_0)
print sol
print "pi =", sol*4
