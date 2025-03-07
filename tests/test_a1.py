import pytest
import numpy as np

from phys305_hw3 import count, sample


# Ground truth parameters for testing
n0    = 100
lmbda = 0.01
groundtruth = (n0, lmbda)

# Time parameters for the measurement
t  = 0
dt = 10


def test_count():
    """Test the `count` function to verify that it returns the
    correct expected number of counts for given time parameters and
    ground truth.

    The expected value is computed from the radioactive decay formula.

    """
    c = count(t, dt, groundtruth)

    # Use pytest.approx() to handle floating point comparisons.
    assert c == pytest.approx(10.517091807564771)


def test_sample():
    """Test the `sample` function by generating multiple samples and
    verifying that the average of these samples approximates the
    expected count value.

    A fixed random seed is used to ensure reproducibility.

    """
    np.random.seed(42)

    cs = [sample(t, dt, groundtruth) for _ in range(1000)]
    c  = np.mean(cs)

    assert c == pytest.approx(10.517091807564771, rel=0.1)
