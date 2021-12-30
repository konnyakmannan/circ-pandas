import circpandas

from numpy import testing as npt
import pandas as pd

def test_mean():
    s = pd.Series([160.0, -170.0])

    desired = 175.0
    actual = s.circ.mean()
    npt.assert_allclose(actual, desired)
