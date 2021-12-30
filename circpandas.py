import numpy as np
import pandas as pd

@pd.api.extensions.register_series_accessor('circ')
class CircAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def mean(self, radian: bool = True) -> float:
        angles = self._obj
        if not radian:
            angles = np.deg2rad(angles)
        mean_cosine = np.mean(np.cos(angles))
        mean_sine = np.mean(np.sin(angles))
        mean_angle = np.arctan2(mean_sine, mean_cosine)
        if not radian:
            mean_angle = np.rad2deg(mean_angle)
        return mean_angle

