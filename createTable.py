import psycopg2 

import moduleForConnection

conn =  moduleForConnection.connectToDB()

#conn_string = "host='localhost' dbname='testdb' user='gumer' password='aidar'" #connection parameters

#conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

tableName = raw_input("Please enter tible name:")

firstColumnName = raw_input("please enter first column name:")

secondColumnName = raw_input("Please enter second column name:")

param = [tableName, firstColumnName, secondColumnName]

query = """    
    CREATE TABLE {0}(
    {1} VARCHAR(255),
    {2} INT NOT NULL)
    """.format(param[0], param[1], param[2])
cursor.execute(query)
conn.commit()

conn.close()
