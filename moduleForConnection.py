import psycopg2
import getpass

def connectToDB():
    hostname = raw_input("Please enter hostname:") or 'localhost'
    dbname = raw_input("Please enter DB name:") or 'testdb'
    username = raw_input("Please enter Username:") or 'gumer'
    password = getpass.getpass("Please enter Password:")

    conn_string = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format(hostname, dbname, username, password) 
    connectionName = psycopg2.connect(conn_string)
    cursor = connectionName.cursor()
    print(conn_string)
    cursor.execute('SELECT * from testtable')    
    infoFromDB = cursor.fetchall() 
    print(infoFromDB) 
connectToDB()
