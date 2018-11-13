import psycopg2
import xlrd

conn_string = "host='localhost' dbname='testdb' user='gumer' password='aidar'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()


dataXls = xlrd.open_workbook('data.xls',formatting_info=True)
sheet = dataXls.sheet_by_index(0)
colnames = []
for colnum in range (sheet.ncols):
    colnames.append(sheet.cell(0, colnum).value)

cursor.execute("CREATE TABLE tableForData(VARCHAR(255));".format(colnames[0])
