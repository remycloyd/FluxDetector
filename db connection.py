import mysql.connector

cnx = mysql.connector.connect(user='root', password='Vihila1;',
                              host='127.0.0.1',
                              database='mydb')
cnx.close()
