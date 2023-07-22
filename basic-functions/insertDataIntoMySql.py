import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host="tuxpas-database.csmaoylldox7.us-east-1.rds.amazonaws.com",
        database="tuxpas",
        user="admin",
        password="perrocurry123",
    )
    mysql_empsql_insert_query = "INSERT INTO courses (id, course) VALUES (%s, %s)"

    rows = []
    with open("course.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # print(row)
            rows.append(row)

    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query, rows)
    connection.commit()
    print(cursor.rowcount, "Record inserted sucessfully into courses table")

    sql_select_query = "SELECT * from courses"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    print("Total number of rows in courses table is ", cursor.rowcount)

    print("\nPrinting each course record")
    for row in records:
        print("id = ", row[0])
        print("course = ", row[1])
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into courses table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
