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
        [0,0    ,0,0],
        [0,0    ,0,0],
        [0,20/99,0,0],
        [0,0    ,0,0],
        [0,0    ,0,0],
    ]), rel=1e-3, abs=1e-6)
