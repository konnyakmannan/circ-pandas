import circpandas

from numpy import testing as npt
import pandas as pd

def test_mean():
    ss = [
        pd.Series([160.0, -170.0]),
        pd.Series([45.0, -45.0, 0.0]),
    ]

    desired = [175.0, 0.0]
    actual = [s.circ.mean(radian=False) for s in ss]
    npt.assert_allclose(actual, desired)
