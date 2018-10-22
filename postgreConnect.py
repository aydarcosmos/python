import psycopg2
import pprint

conn_string = "host='localhost' dbname='testdb' user='gumer' password='aidar'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
cursor.execute("DELETE FROM testtable WHERE number = 28")
conn.commit()
cursor.execute("SELECT * from testtable")
infoFromDB = cursor.fetchall()
conn.close()

for line in infoFromDB:
    print(line)


