import pandas as pd
import numpy as np

# Reading original data file
df = pd.read_csv('no_shows.csv')

# Dropping not needed columns
df = df.drop(['PatientId'])

#setting all column names to lowercase
df = df.columns.str.lower()

# Drop ages that are less than 0
df = df[df.age >= 0]

# Writing cleaned data to new CSV file
df.to_csv('no_shows_cleaned.csv', index=False)