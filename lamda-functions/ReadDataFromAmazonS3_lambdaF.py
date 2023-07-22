import json
import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    # TODO implement
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    csv_file = event["Records"][0]["s3"]["object"]["key"]
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    lines = csv_file_obj["Body"].read().decode("utf-8").split("\n")
    results = []

    # Process the data rows using csv.DictReader (header assumed)
    # for row in csv.DictReader(lines):
    #    results.append(row.values())

    # Process the data rows using csv.reader (no header assumed)
    for row in csv.reader(lines):
        results.append(row)

    # print(results)

    connection = mysql.connector.connect(
        host="tuxpas-database.csmaoylldox7.us-east-1.rds.amazonaws.com",
        database="tuxpas",
        user="admin",
        password="perrocurry123",
    )
    mysql_empsql_insert_query = "INSERT INTO courses (id, course) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query, results)
    connection.commit()
    print(cursor.rowcount, "Record inserted sucessfully into courses table")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
