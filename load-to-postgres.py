import psycopg2

# in postgres version 14, we need to use with syntax to do state
# login to default database and create database name "weatherdb"
conn = psycopg2.connect(dbname="postgres", user="postgres", password="soulfunkjazz88", host="localhost")

# make cursor auto commit (like confirm our command)
conn.autocommit = True


with conn.cursor() as cur: 
    cur.execute("DROP DATABASE weatherdb")
    
with conn.cursor() as cur: 
    cur.execute("CREATE DATABASE weatherdb")

conn.close()

# login to "weatherdb" database, create "weather" table and upload "weather.csv" to "weather" table
conn = psycopg2.connect(dbname="weatherdb", user="postgres", password="soulfunkjazz88", host="localhost")
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("CREATE TABLE weather (Country varchar, Province varchar, date date, temperatureMin double precision, temperatureMax double precision)")

with conn.cursor() as cur:
    file = open('output-files\weather.csv', 'r')
    next(file)
    cur.copy_from(file, 'weather', sep=',')

# confirm that data has loaded into "weather" table by querying
with conn.cursor() as cur:
    sql = "SELECT count(*) FROM weather;"
    cur.execute(sql)
    result = cur.fetchone()
    print("weather table has", result[0], "rows")
    
conn.close()