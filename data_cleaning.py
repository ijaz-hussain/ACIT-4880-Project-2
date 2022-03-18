import pandas as pd

# Reading original data file
df = pd.read_csv('height.csv')

# Calculating average height in Cm (male and female)
col_cm = df.loc[: , "Male Height in Cm":"Female Height in Cm"]
df['Average height in Cm'] = col_cm.mean(axis=1)

# Calculating average height in Ft (male and female)
col_ft = df.loc[: , "Male Height in Ft":"Female Height in Ft"]
df['Average height in Ft'] = col_ft.mean(axis=1)

# Reorder columns
df = df[['Rank', 'Country Name', 'Average height in Cm', 'Male Height in Cm', 'Female Height in Cm', 'Average height in Ft', 'Male Height in Ft', 'Female Height in Ft']]

# Replacing any NaN values with 0 if they exist
df = df.fillna(0)

# Ensuring all data is rounded to two decimal places
df = df.round(decimals=2)

# Sorting data from largest to smallest
df = df.sort_values(by='Average height in Cm', ascending=False)

# Writing cleaned data to new CSV file
df.to_csv('height_cleaned.csv')