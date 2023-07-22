import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def lambda_handler(event, context):
    # TODO implement
    connection = mysql.connector.connect(
        host="tuxpas-database.csmaoylldox7.us-east-1.rds.amazonaws.com",
        database="tuxpas",
        user="admin",
        password="perrocurry123",
    )
    mysql_empsql_insert_query = "INSERT INTO courses (id, course) VALUES (%s, %s)"
    rows = [["3000", "Algorithms"], ["3001", "Data Structures"]]
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query, rows)
    connection.commit()
    print(cursor.rowcount, "Record inserted sucessfully into courses table")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
