import pandas as pd


# Reading original data file
df = pd.read_csv('no_shows.csv')

# Setting all column names to lowercase
df = df.rename(columns=str.lower)

# Dropping not needed columns
df = df.drop(columns=['patientid', 'appointmentid', 'scheduledday', 'appointmentday', 'neighbourhood'])

# Rename misspelled columns
df.rename(columns={'hipertension': 'hypertension', 'handcap': 'handicap', 'no-show': 'no_show'}, inplace=True)

# Drop ages that are less than 0
df = df[df.age >= 0]

# Legal drinking age in most countries is at least 18 - dropping any rows with minors and alcoholism
#checking
print(df[(df.alcoholism) & (df.age < 18)].shape)

#dropping them by using their index with the drop method
df.drop(index= df[(df.alcoholism) & (df.age < 18)].index , inplace=True)

#checking the operation
print(df[(df.alcoholism) & (df.age < 18)].shape)

# Drop index column
df = df.set_index('gender')

# Change no_show column from Yes/No to 1/0
df.no_show = df.no_show.map(dict(Yes=1, No=0))

# Writing cleaned data to new CSV file
df.to_csv('no_shows_cleaned.csv')