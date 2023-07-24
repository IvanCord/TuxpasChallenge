
# Tuxpas Challenge

As a data engineer at Tuxpas, you're on the brink of undertaking a significant project
involving the migration of large amounts of data to a new database system. You are tasked
with developing a proof of concept that addresses the following requirements:

1. Transfer historical data from CSV files to the new database.
2. Develop a RESTful API service to handle incoming data, with the following considerations:
- Each incoming transaction must comply with data dictionary rules.
- Facilitate the insertion of batch transactions, from 1 to 1000 rows.
- Accept data for different tables through the same service.
- Remember to enforce specific data rules for each table.
3. An architectural diagram for the most optimal (not necessarily the one you will be
presenting) solution in an AWS environment using its cloud services.

## Solution: AWS API Rest Serverless Architecture

![What is this](TuxpasAPIRestArchitecture.png)
