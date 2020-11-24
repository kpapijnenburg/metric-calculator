from numpy import mean, nan
from datetime import datetime
from scipy.stats import linregress
import pandas as pd
import numpy as np


def calculate_values(values: list, dates: list) -> tuple:
    """Calculates the minimal, maximum, mean and slope of the given values."""
    # Convert all dates to timestamps
    dates = [date.timestamp() for date in dates]

    # If the length of values does is not the same as the length of dates linear regession can not be done.
    if len(values) != len(dates):
        slope = nan
    else:
        slope, _, _, _, _ = linregress(dates, values)

    min_ = min(values)
    max_ = max(values)
    mean_ = mean(values)

    return min_, max_, mean_, slope


def get_absolute_relative_difference(values: list, dates: list) -> float:
    """ Calculated the absolute relative difference between a list of values """
    difference = dates.iloc[-1] - dates.iloc[0]
    nr_of_days = round(difference.days + (difference.seconds / 3600 / 24))

    return (values.iloc[-1] - values.iloc[0]) / nr_of_days


def initialize_dataframe(metric: str, ids: list, year_range: range) -> pd.DataFrame:
    data = []

    for id_ in ids:
        for year in year_range:
            try:
                data.append([int(id_), year, None, None, np.nan,
                             np.nan, np.nan, np.nan, np.nan, np.nan])
            except ValueError as e:
                pass

    return pd.DataFrame(data, columns=['player_id', 'year', 'first', 'last', 'nr_of_measurements', 'min', 'max', 'mean', 'slope', 'abs_relative_difference'])


def get_row_values(row, df, metric):
    subset = df[df['PLR_ID'] == row.player_id]
    subset = filter_on_year(row.year, subset)

    values = subset[metric].dropna()
    dates = subset.Date

    first, last = (None,) * 2
    nr_of_measurements, min_, max_, mean_, slope, abs_relative_difference = (
        np.nan,) * 6

    if len(dates) > 1 and len(values) > 1:
        min_, max_, mean_, slope = calculate_values(values, dates)
        abs_relative_difference = get_absolute_relative_difference(
            values, dates)
        last = dates.iloc[-1]
        first = dates.iloc[0]

    return row.player_id, row.year, first, last, len(values), min_, max_, mean_, slope, abs_relative_difference
    # Return order
    #player_id, year, first, last, nr_of_measurements, min,  max, mean, slope, abs_relative_difference


def filter_on_year(year: int, df: pd.DataFrame) -> pd.DataFrame:
    # Create subset from the dataframe containing the data measured in the given year.
    subset = df[df.Date.dt.year == year]
    subset.sort_values(by="Date")
    return subset
