import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql@64',
    'database': 'Food',  # Replace with your credentials
}


connection = mysql.connector.connect(**db_config)
if connection.is_connected():
    print("Connected to MySQL database")

cursor = connection.cursor()


insert_query = """
    INSERT INTO Recipient(
        Email_ID,
        Recipient_ID,
        NGO_name,
        Phone_number,
        Address,
        City,
        State,
        Pincode,
        quantity_required_inGrams,
        redistribution_time_span_inHours
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

val = [
    ('abc@gmail.com', 1, 'Goonj', '9398165342', 'ramapuram', 'chennai', 'tamilnadu', 654654, 4, 2),
('bcd@gmail.com', 2, 'pratham', '9398165342', 'vani_nagar', 'mumbai', 'maharashtra', 213416, 20, 3),
    ('efg@gmail.com', 3, 'actionaid', '9398165342', 'prasanth_nagar', 'kanyakumari', 'tamilnadu', 897764, 50, 5),
    ('hij@gmail.com', 4, 'BARC', '9398165342', 'tdp_area', 'jammu', 'kashmir', 564534, 80, 6),
    ('lmn@gmail.com', 5, 'catholic relief services', '9398165342', 'wee_place', 'mumbai', 'madhya pradesh', 645466, 90, 7),
    ('kml@gmail.com', 6, 'deepalaya', '9398165342', 'telugu_place', 'delhi', 'uttar pradesh', 544352, 53, 4),
    ('one@gmail.com', 7, 'give foundation', '9398165342', 'ysrcp_area', 'shimla', 'uttar pradesh', 545361, 45, 3),
    ('two@gmail.com', 8, 'sammaan', '9398165342', 'prabhas_nagar', 'nellore', 'andhra pradesh', 209870, 89, 9),
    ('ten@gmail.com', 9, 'action against hunger', '9398165342', 'koyembedu', 'tirupati', 'andhra pradesh', 786754, 85, 4),
    ('red@gmail.com', 10, 'world now', '9398165342', 'kilpauk', '', 'tamilnadu', 284534, 45, 7),
    ('mno@gmail.com', 11, 'who', '9398165342', 'hell', 'hyderabad', 'telangana', 203425, 76, 8),
    ('uno@gmail.com', 12, 'caring hearts', '9398165342', 'heavenly_area', 'west bengal', 'bengal', 406234, 43, 7),
    ('ino@gmail.com', 13, 'uniting our world', '9398165342', 'valluvari_salai', 'kolkata', 'bengal', 457892, 45, 4),
    ('bal@gmail.com', 14, 'novo', '9398165342', 'embassy_nagar', 'kanpur', 'karnataka', 434456, 55, 4)

]

try:

    cursor.executemany(insert_query, val)


    connection.commit()
    print(f"Inserted {len(val)} rows successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    # Rollback the transaction if an error occurs
    connection.rollback()
finally:
    cursor.close()
    connection.close()
