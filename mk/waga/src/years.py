"""
Project: Daily weight analysis.
Class: YearlyDF containe df with one year measurements.


Copyright: Marek


Created: 2024.11.18
Modified: 2024.11.18
"""
import pandas as pd

class YearlyDF:
    def __init__(self, name, df):
        self.name = str(name)
        self._df = df.copy()

    def get_mean_by_monty(self, prec=2):
        return self._df.mean(skipna=True).round(prec)