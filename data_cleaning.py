import pandas as pd
import numpy as np

# Reading original data file
df = pd.read_csv('height.csv')

# Calculating average height in Cm (male and female)
col_cm = df.loc[: , "Male Height in Cm":"Female Height in Cm"]
df['Average height in Cm'] = col_cm.mean(axis=1)

# Dropping rank and columns with ft
df = df.drop(['Rank', 'Female Height in Ft', 'Male Height in Ft'], axis=1)

# Reorder columns
df = df[['Country Name', 'Average height in Cm', 'Male Height in Cm', 'Female Height in Cm']]

# Replacing any NaN values with 0 if they exist
df = df.fillna(0)

# Ensuring all data is rounded to two decimal places
df = df.round(decimals=2)

# Sorting data from largest to smallest
df = df.sort_values(by='Average height in Cm', ascending=False)

# Writing cleaned data to new CSV file
df.to_csv('height_cleaned.csv', index=False)