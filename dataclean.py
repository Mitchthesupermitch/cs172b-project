import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import time

print(torch.backends.mps.is_available())

# Load the dataset
file_path = 'household_power_consumption.txt'
data = pd.read_csv(file_path, sep=';', na_values='?', low_memory=False)

# Combine and convert the Date and Time into a single Datetime column and set as index
data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], dayfirst=True)
data.drop(['Date', 'Time'], axis=1, inplace=True)
data.set_index('Datetime', inplace=True)

# Impute missing values based on the mean of the same time slot across different years
time_mean = data.groupby(data.index.time).mean()
for col in ['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']:
    fill_values = data.index.map(lambda x: time_mean.at[x.time(), col])
    data[col] = data[col].fillna(pd.Series(fill_values, index=data.index))

# Calculate the new feature 'Active_Energy_Not_Measured'
data['Active_Energy_Not_Measured'] = (data['Global_active_power'] * 1000 / 60) - (data['Sub_metering_1'] + data['Sub_metering_2'] + data['Sub_metering_3'])

## Resample the dataset to every 15 minutes
data_resampled = data.resample('15min').mean()

# Display the first few rows of the resampled dataframe to verify
data_resampled.head()