import numpy as np
import pandas as pd

allfiles = ['b_should_be_easy.in', 'c_no_hurry.in', 'd_metropolis.in', 'e_high_bonus.in']
alldfs = []

for file in allfiles:
    f = open(file, 'r')
    df = pd.DataFrame([ride.split(" ") for ride in f.readlines()],
                  dtype=float,
                  columns=['start_row', 'start_col', 'end_row', 'end_col', 'time_earliest', 'time_latest'])
    alldfs.append(df)

b_df, c_df, d_df, e_df = alldfs

"""
LET'S WORK WITH THE FIRST DATASET: b_should_be_easy.in
"""
# sort by earliest time
b_df.sort_values(by='time_earliest', inplace=True)

# save useful variables
b_NUM_ROWS, b_NUM_COLS, b_NUM_VEHICLES, b_NUM_RIDES, b_NUM_BONUS, b_NUM_STEPS = b_df.loc[0, :]

# remove first row
b_df = b_df[1:]

print(b_df.head())
