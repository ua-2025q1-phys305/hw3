import pytest
import numpy as np
from numpy import log

from phys305_hw3 import count, prior0_n0, prior0_lmbda, trapezoid2, posterior


n0          = 100
lmbda       = 0.01
groundtruth = n0, lmbda

ts  = np.linspace(0, 100, 11)
dt  = 10
Cts = count(ts, dt, groundtruth)

n0s,    ps_n0    = prior0_n0(n=4)
lmbdas, ps_lmbda = prior0_lmbda(n=5)

params = np.meshgrid(n0s, lmbdas)
prior  = ps_n0[None,:] * ps_lmbda[:,None]


def test_trapezoid2():

    x = np.linspace(-10, 10, 101)
    y = np.linspace(-10, 10, 201)

    X, Y = np.meshgrid(x, y)
    G    = np.exp(-0.5 * (X*X + Y*Y)) / (2 * np.pi)
    I    = trapezoid2(G, (X, Y))

    assert I == pytest.approx(1)


def test_posterior():

    obs  = Cts, ts, dt
    post = posterior(obs, prior, params)

    assert post == pytest.approx(np.array([
        [0.00000000e+000, 8.93146071e-116, 4.67763254e-094, 1.50488443e-081],
        [0.00000000e+000, 5.76653448e-040, 2.43370687e-022, 6.30950198e-014],
        [0.00000000e+000, 2.02020202e-001, 3.01938027e-011, 2.77213427e-030],
        [0.00000000e+000, 3.04598307e-116, 4.23549674e-212, 0.00000000e+000],
        [0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
    ]))
