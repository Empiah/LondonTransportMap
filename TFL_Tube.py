import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

tube_df = pd.read_csv('/Users/oliverphipps/Dropbox/6. Python/Python Projects/TFL Tube Project/2015_Data_TFL.csv')

tube_df.head()

data_by_location = tube_df.groupby(['latitude', 'longitude'],as_index=False).mean()

data_by_location.head()['latitude']
scaled_entries = (data_by_location['EntriesHr'] / data_by_location['EntriesHr'].std())

plt.scatter(data_by_location['latitude'], data_by_location['longitude'], s=scaled_entries)

plt.savefig('/Users/phipp/Dropbox/6. Python/TFL Tube Project/TFLScatter.png', dpi=600)
