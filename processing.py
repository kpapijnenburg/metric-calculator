from data import SSH, Names
from helpers import calculate_values, get_absolute_relative_difference, initialize_dataframe
import pandas as pd
import numpy as np
from tqdm import tqdm
import math

client = SSH(Names.koen)
client.login()

df = client.load_clean_antropometrie_data()

metrics = ['Length (cm)',
           'Sitting Length (cm)', 'Weight (kg)', 'Triceps', 'Biceps',
           'Subscapulair (mm)', 'Supra-iliacaal (mm)', 'Total (mm)',
           'Body Fat (%)', 'Body Density', 'Length Upper Body (cm)']

# # metrics = [
# #     'Length (cm)',
# #     'Sitting Length (cm)',
# #     'Weight (kg)',
# #     'Triceps',
# #     'Biceps',
# #     'Subscapulair (mm)',
# #     'Supra-iliacaal (mm)',
# #     'Total (mm)',
# #     'Body Fat (%)',
# #     'Body Density',
# #     'Length Upper Body (cm)',
# #     'TIME_Sprint 0-10m',
# #     'TIME_Sprint 10-20m',
# #     'TIME_Sprint 20-30m',
# #     'TIME_Sprint 0-30m',
# #     'TIME_COD-L',
# #     'TIME_COD-R',
# #     'force_velocity',
# #     'power_max',
# #     'RF'
# # ]

other = ['PLR_ID', 'Date']

subset = df[metrics + other]

# Convert ids from float to int.
ids = df.PLR_ID.unique()

range_ = range(int(df.Date.dt.year.min()), int(df.Date.dt.year.max()) + 1)

for metric in tqdm(metrics):
    # init dataframe
    data_frame = initialize_dataframe(metric, ids, range_)
    print(data_frame.head())
    break
        # # Create temporary dataframe containing the data measured in the current year.
        # temp = subset[subset.Date.dt.year == year]
        # # Sorting the values by date so the first and last occurrences of measurements can be extracted.
        # temp.sort_values(by='Date')

    #     for plr_id in ids:
    #         # Add date of first and last measurement
    #         dates = temp.loc[temp['PLR_ID'] == plr_id]['Date']

    #         # It is only relevant to check differences when there are more than two dates
    #         # where measurements took place.
    #         if len(dates) > 1:
    #             # When the only two measurments in a year were made on the same day
    #             # it will result in a days value of zero.
    #             data_frame.loc[index, 'first_measurement'] = dates.iloc[0]
    #             data_frame.loc[index, 'last_measurement'] = dates.iloc[-1]

    #             measurements = temp.loc[temp['PLR_ID']
    #                                     == plr_id][metric].dropna()

    #             if len(measurements) > 1:
    #                 # Calculate all values
    #                 minimal, maximum, mean, slope = calculate_values(
    #                     measurements, dates)
    #                 abs_rel_difference = get_absolute_relative_difference(
    #                     measurements, dates)
    #                 data_frame.loc[index, 'year'] = year
    #                 data_frame.loc[index, 'nr_of_measurements'] = len(
    #                     measurements)
    #                 data_frame.loc[index, 'min'] = minimal
    #                 data_frame.loc[index, 'max'] = maximum
    #                 data_frame.loc[index, 'mean'] = mean
    #                 data_frame.loc[index, 'slope'] = slope
    #                 data_frame.loc[index,
    #                                'absolute_relative_difference'] = abs_rel_difference

    #         # Only keep the rows were a player had more than two measurments
    #         data_frame.dropna(
    #             subset=['first_measurement', 'last_measurement'], inplace=True)
    #         data_frame.reset_index(drop=True, inplace=True)

    # # Save the dataframe when there is at least 1 row of data
    # if data_frame.shape[0] > 0:
    #     data_frame.to_csv(f'./exports/{data_frame.name}.csv')
