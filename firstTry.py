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

# save useful variables
NUM_ROWS, NUM_COLS, NUM_VEHICLES, NUM_RIDES, NUM_BONUS, NUM_STEPS = rides_df.loc[0, :]

# remove first row
rides_df = rides_df[1:]

print(rides_df.head())
