import pytest

from phys305_hw3 import prior0_n0, prior0_lmbda


def test_prior0_n0():

    n0s, ps_n0 = prior0_n0(n=4)

    assert n0s   == pytest.approx([0,100,200,300])
    assert ps_n0 == pytest.approx(1/300)

def test_prior0_lmbda():

    lmbdas, ps_lmbda = prior0_lmbda(n=5)

    assert lmbdas   == pytest.approx([1e-4,1e-3,1e-2,1e-1,1])
    assert ps_lmbda == pytest.approx([
        5.0474369195669805e-09,
        7.795871698888053e-02,
        1.941463711450083e+01,
        7.795871698888053e-02,
        5.0474369195669805e-09,
    ])
