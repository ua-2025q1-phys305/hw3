import pytest
import numpy as np
from   numpy import log

from phys305_hw3 import logpoisson, count, likelihood


# Ground truth parameters for testing
n0    = 100
lmbda = 0.01
groundtruth = (n0, lmbda)

# Create a set of time points and a measurement interval
ts = np.linspace(0, 100, 11)
dt = 10


def test_logpoisson():
    """Test the `logpoisson()` function to verify that it correctly
    computes the logarithm of the Poisson probability mass function.

    The tests check for a variety of k and lmbda values to ensure that
    the function behaves as expected.

    """
    assert logpoisson(0, 1) == pytest.approx(-1)
    assert logpoisson(1, 1) == pytest.approx(-1)
    assert logpoisson(2, 1) == pytest.approx(-1-log(2))
    assert logpoisson(3, 1) == pytest.approx(-1-log(2*3))
    assert logpoisson(4, 1) == pytest.approx(-1-log(2*3*4))

    assert logpoisson(0, 2) == pytest.approx(-2)
    assert logpoisson(1, 2) == pytest.approx(-2 +   log(2))
    assert logpoisson(2, 2) == pytest.approx(-2 + 2*log(2) - log(2))
    assert logpoisson(3, 2) == pytest.approx(-2 + 3*log(2) - log(2*3))
    assert logpoisson(4, 2) == pytest.approx(-2 + 4*log(2) - log(2*3*4))


def test_likelihood():
    """Test the `likelihood()` function to verify that it correctly
    computes the combined likelihood over a series of measurements.

    This test first computes the expected counts using the count
    function, then calculates the likelihood incrementally over
    subsets of the data, and finally compares the computed likelihood
    values to pre-computed expected values.

    """
    Cts = count(ts, dt, groundtruth)

    likes = []
    for u in range(len(ts)):
        obs = Cts[:u+1], ts[:u+1], dt
        likes.append(likelihood(obs, groundtruth))

    assert likes == pytest.approx([
        0.12204558897970384,
        0.015645784650976338,
        0.002106627966482018,
        0.0002978870904208763,
        4.423261327490666e-05,
        6.896194804218761e-06,
        1.1287456275679916e-06,
        1.9392780394508465e-07,
        3.496817027668932e-08,
        6.616356842093209e-09,
        1.3133931511273722e-09
    ])
