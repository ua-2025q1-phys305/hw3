import pytest
import numpy as np

from phys305_hw3 import trapezoid2, runexpr

def test_runexpr():
    """Test the `runexpr()` function to verify that the final
    posterior distribution on the parameter grid is computed as
    expected.

    The function `runexpr()` updates the posterior sequentially using
    synthetic data.  With a fixed random seed and a small grid
    (n_n0=4, n_lmbda=5), we compare the final posterior against a
    pre-computed expected array.

    """
    np.random.seed(42)

    posts, params = runexpr(
        n_n0    = 4,
        n_lmbda = 5,
    )

    assert posts[-1] == pytest.approx(np.array([
        [0,0    ,0,0],
        [0,0    ,0,0],
        [0,20/99,0,0],
        [0,0    ,0,0],
        [0,0    ,0,0],
    ]), rel=1e-3, abs=1e-6)

def test_lmbda():
    """Test the estimation of the decay constant (lmbda) from the
    posterior distribution.

    This test uses the final posterior distribution from `runexpr()`
    and computes the expected value of lmbda by integrating (using
    trapezoidal integration) over the parameter grid.  The result is
    then compared with a known approximate value.

    """
    np.random.seed(42)

    posts, params = runexpr(n_expr=10)

    n0ss, lmbdass = params
    post = posts[-1]

    lmbda = trapezoid2(post * lmbdass, params)

    assert lmbda == pytest.approx(0.0088, rel=1e-1)
