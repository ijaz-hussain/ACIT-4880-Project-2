import pandas as pd
import numpy as np

# Reading original data file
df = pd.read_csv('no_shows.csv')

# Setting all column names to lowercase
df = df.columns.str.lower()

# Dropping not needed columns
df.drop(['patientid', 'appointmentid', 'scheduledday', 'appointmentday', 'neighbourhood'])

print(df)

#df.rename(index={3: 'hypertension', 6: 'handicap', 8: 'no_show'}, inplace=True)

# Drop ages that are less than 0
#df = df.drop[df.age >= 0]

# Writing cleaned data to new CSV file
#df.to_csv('no_shows_cleaned.csv')