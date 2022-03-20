import csv

with open('output-files\weather.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data, None)
    print(csv_data)