from numpy import mean, nan
from datetime import datetime
from scipy.stats import linregress
import pandas as pd


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
