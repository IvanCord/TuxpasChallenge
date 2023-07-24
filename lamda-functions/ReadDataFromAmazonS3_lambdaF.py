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
    results_not_inserted = []

    # Process the data rows using csv.DictReader (header assumed)
    # for row in csv.DictReader(lines):
    #    results.append(row.values())

    # Process the data rows using csv.reader (no header assumed)
    for row in csv.reader(lines):
        if all(cell != "" for cell in row) and (
            row != []
        ):  # Check if all cells in the row are not empty - data integrity
            results.append(row)
        else:
            results_not_inserted.append(row)

    print(
        "Transactions failing to comply with the rules are ... ", results_not_inserted
    )  # Load to Amazon CloudWatch

    connection = mysql.connector.connect(
        host="tuxpas-database.csmaoylldox7.us-east-1.rds.amazonaws.com",
        database="tuxpas",
        user="admin",
        password="perrocurry123",
    )

    tabletype = csv_file.split("/")[-1][:6]
    mysql_empsql_insert_query = ""
    if tabletype == "course":
        mysql_empsql_insert_query = "INSERT INTO courses (id, course) VALUES (%s, %s)"
    elif tabletype == "career":
        mysql_empsql_insert_query = "INSERT INTO careers (id, career) VALUES (%s, %s)"
    elif tabletype == "studen":
        mysql_empsql_insert_query = "INSERT INTO students (id, name, enrolment, career_id, course_id) VALUES (%s, %s, %s, %s, %s)"

    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query, results)
    connection.commit()
    print(cursor.rowcount, "Record inserted sucessfully into courses table")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
