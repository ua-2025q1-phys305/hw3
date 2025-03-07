import pytest
import numpy as np
from numpy import exp, pi

from phys305_hw3 import count, prior0_n0, prior0_lmbda, trapezoid2, posterior


# Ground truth parameters for the radioactive decay model
n0          = 100
lmbda       = 0.01
groundtruth = (n0, lmbda)

# Create time points and compute expected counts for the experiment
ts  = np.linspace(0, 100, 11)
dt  = 10
Cts = count(ts, dt, groundtruth)

# Create a discretized grid for n0 and lmbda parameters
n0s,    ps_n0    = prior0_n0(n=4)
lmbdas, ps_lmbda = prior0_lmbda(n=5)

# Combine the 1D parameter grids into 2D grid
params = np.meshgrid(n0s, lmbdas)

# Compute the combined prior on the 2D grid as an outer product of the
# individual priors
prior  = ps_n0[None, :] * ps_lmbda[:, None]


def test_trapezoid2():
    """Test the 2D trapezoidal integration function `trapezoid2()`.

    This test constructs a normalized 2D Gaussian function (which
    integrates to 1) on a mesh grid and then uses `trapezoid2()` to
    compute its integral. The result should be 1.

    """
    x = np.linspace(-10, 10, 101)
    y = np.linspace(-10, 10, 201)

    X, Y = np.meshgrid(x, y)
    G    = exp(-0.5 * (X*X + Y*Y)) / (2 * pi)
    I    = trapezoid2(G, (X, Y))

    assert I == pytest.approx(1)


def test_posterior():
    """Test the `posterior()` function.

    This test computes the posterior probability distribution on the
    parameter grid after observing the counts data from the
    experiment. The expected posterior is provided as a pre-computed
    array for this specific synthetic dataset and grid configuration.

    """
    obs  = Cts, ts, dt
    post = posterior(obs, prior, params)

    assert post == pytest.approx(np.array([
        [0,0    ,0,0],
        [0,0    ,0,0],
        [0,20/99,0,0],
        [0,0    ,0,0],
        [0,0    ,0,0],
    ]), rel=1e-3, abs=1e-6)
