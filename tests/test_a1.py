import pytest
import numpy as np

from phys305_hw3 import count, sample


n0    = 100
lmbda = 0.01

t  = 0
dt = 10

groundtruth = n0, lmbda


def test_count():
    c = count(t, dt, groundtruth)
    assert c == pytest.approx(10.517091807564771)

def test_samplpe():
    np.random.seed(42)
    c = np.mean([sample(t, dt, groundtruth) for _ in range(1000)])
    assert c == pytest.approx(10.517091807564771, 0.1)
