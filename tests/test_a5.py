import pytest
import numpy as np

from phys305_hw3 import trapezoid2, runexpr

def test_runexpr():

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

    np.random.seed(42)

    posts, params = runexpr(n_expr=10)

    n0ss, lmbdass = params
    post = posts[-1]

    lmbda = trapezoid2(post * lmbdass, params)

    assert lmbda == pytest.approx(0.009, rel=1e-1)
