import mysql.connector
import random

# Database connection parameters
config = {
    'user': 'root',
    'password': 'mysql@64',
    'host': 'localhost',
    'database': 'Food'
}

try:
    # Establish a database connection
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        cursor = connection.cursor()

        # Sample SQL query to create the "Donor" table (if not already created)
        create_table_query = """
        CREATE TABLE if not exists surplus
        (Food_id INT AUTO_INCREMENT PRIMARY KEY,food_type VARCHAR(255),
        donor_id INT,food_name VARCHAR(255),quantity varchar(200),
        Expiry_Date date,Packaging_Date date,ingredients varchar(50),ingredient_count int,
        Allergen_Info varchar(200),Dietary_Info varchar(200),
        storage_remarks varchar(200),status varchar(200),waste varchar(200));
        """
        cursor.execute(create_table_query)
        insert_query="INSERT INTO surplus (Food_id,donor_id,food_type,food_name,quantity,Expiry_Date,Packaging_Date,ingredients,ingredient_count,Allergen_Info,Dietary_Info,storage_remarks,status,waste) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print("Hi Donor, Kindly enter your details below:")
        while(True):
            food_id=input("Enter the food_id: ")
            donor_id=input("Enter the donor id: ")
            food_type=input("Enter the food type: ")
            food_name=input("Enter the food name: ")
            quantity=input("Enter the quantity: ")
            expiry_date=input("Enter the expiry date: ")
            packaging_date=input("Enter the packaging date: ")
            ingredients=input("Enter the ingredients used: ")
            ingredient_count=input("Enter the ingredients count: ")
            allergen_info=input("Enter the allergen information: ")
            dietary_info =input("Enter dietary information:")
            storage_remarks=input("Enter storage remarks:")
            status=input("Enter status:")
            waste=input("Enter waste:")
            surplus_data=(food_id,donor_id,food_type,food_name,quantity,expiry_date,packaging_date,ingredients,ingredient_count,allergen_info,dietary_info,storage_remarks,status,waste)
            
            cursor.execute(insert_query,surplus_data)
            connection.commit()
            ch=input("Is that all? [y/n]: ")
            if(ch=='y'):
                break
            connection.commit()
except mysql.connector.Error as error:
    print("Error: ", error)

finally:
    if 'connection' in locals():
        if cursor:
            cursor.close()
        connection.close()

