import pandas as pd
import mysql.connector
import numpy as np
db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '@MYsql23!',
        'database': 'Food',
    }
connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
def add():
    cursor = connection.cursor()
    query = """
        INSERT INTO Recipient(
            Email_ID,
            Recipient_ID,
            NGO_name,
            Phone_number,
            Address,
            City,
            State,
            Pincode,
            Quantity_required_in_grams,
            Redistribution_time_span_in_hours
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    n=int(input("Enter number of rows of data to add: "))
    for i in range(n):
        val=input("Enter the details in this order:  Email_ID | Recipient_ID | NGO_name| Phone_number | Address| City | State | Pincode | Quantity_required_in_grams | Redistribution_time_span_in_hours:\n").split()
        cursor.execute(query, val)
        connection.commit()
        print("Data inserted successfully.")

def search():
    cursor = connection.cursor()
    state =input("Enter the State where your NGO is located: ")
    city=input("Enter the City where your NGO is located: ")
    query=f"SELECT * FROM Donor d Where d.city='{city}' || d.state='{state}'"
    data = pd.read_sql(query, con=connection)
    print("Your Results are...\n")
    print(data)


