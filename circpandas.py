import pandas as pd

@pd.api.extensions.register_series_accessor('circ')
class CircAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def mean(self) -> float:
        return self._obj.mean()

