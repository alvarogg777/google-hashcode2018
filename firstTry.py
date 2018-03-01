import numpy as np
import pandas as pd

f = open("b_should_be_easy.in", 'r')
rides = f.read().split("\n")
rides_df = pd.DataFrame([ride.split(" ") for ride in rides],
                  dtype=float,
                  columns=['start_row', 'start_col', 'end_row', 'end_col', 'time_earliest', 'time_latest'])

# remove last row
rides_df = rides_df[:-1]
rides_df['start_row'] = rides_df['start_row'].astype(float)

# sort by earliest time
rides_df.sort_values(by='time_earliest', inplace=True)
print(rides_df.head())
