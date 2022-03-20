import pandas as pd

# read file
data = pd.read_csv('input-files/daily_weather_2020.csv')

# select important columns
data = data[['Country/Region', 'Province/State', 'time', 'temperatureMin', 'temperatureMax']]

# write data to "weather.csv" file
data.to_csv('output-files/weather.csv', index=False)
print(data.head())