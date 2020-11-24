from data import SSH, Names
from helpers import initialize_dataframe, get_row_values
import pandas as pd
import numpy as np
from tqdm import tqdm

client = SSH(Names.koen)
client.login()

df = client.load_clean_antropometrie_data()

metrics = ['Length (cm)',
           'Sitting Length (cm)', 'Weight (kg)', 'Triceps', 'Biceps',
           'Subscapulair (mm)', 'Supra-iliacaal (mm)', 'Total (mm)',
           'Body Fat (%)', 'Body Density', 'Length Upper Body (cm)']

other = ['PLR_ID', 'Date']

subset = df[metrics + other]

ids = df.PLR_ID.unique()

range_ = range(int(df.Date.dt.year.min()), int(df.Date.dt.year.max()) + 1)

for metric in tqdm(metrics):
    # init dataframe
    data_frame = initialize_dataframe(metric, ids, range_)
    data_frame.name = metric.replace(' ', '_').lower()
    
    for index, row in data_frame.iterrows():
        data_frame.loc[index] = get_row_values(row, df[['PLR_ID', 'Date', metric]], metric)

    data_frame.to_csv(f'exports/{data_frame.name}.csv', index=False)