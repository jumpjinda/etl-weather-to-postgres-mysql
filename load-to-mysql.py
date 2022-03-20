import mysql.connector
import csv


# login to default database and create database name "weatherdb"
conn = mysql.connector.connect(user='root', password='', host='localhost', database='mysql')

# make cursor auto commit (like confirm our command)
conn.autocommit = True

# create cursor for implement
cur = conn.cursor()

# make sure delete old database and create new one that we want
cur.execute("DROP DATABASE weatherdb")
cur.execute("CREATE DATABASE weatherdb")

conn.close()

# login to "weatherdb" database, create "weather" table
conn = mysql.connector.connect(user='root', password='', host='localhost', database='weatherdb')
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE weather (Country varchar(50), Province varchar(50), date varchar(15), \
    temperatureMin varchar(10), temperatureMax varchar(10))")

# load data into "weather" table
with open('output-files/weather.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data, None) # None mean skip header row
    for row in csv_data:
        cur.execute('INSERT INTO weather (Country, Province, date, temperatureMin, temperatureMax)' \
               'VALUES("%s", "%s", "%s", "%s", "%s")', row)

# confirm that data has loaded into "weather" table by querying
with conn.cursor() as cur:
    sql = "SELECT count(*) FROM weather;"
    cur.execute(sql)
    result = cur.fetchone()
    print("weather table has", result[0], "rows")
    
conn.close()