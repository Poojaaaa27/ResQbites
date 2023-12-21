import mysql.connector
mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql@64",
  database="food",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists food")
mycursor.execute("CREATE table if not exists donor(donor_id int AUTO_INCREMENT primary key)")
mycursor.execute("CREATE TABLE if not exists recipient(email_id varchar(200),recipient_id INT AUTO_INCREMENT PRIMARY KEY,ngo_name VARCHAR(255),phone_number BIGINT,address VARCHAR(255),city VARCHAR(255),state VARCHAR(255),pincode INT,quantity_required_inGrams INT,redistribution_time_span_inHours INT)")
sql="INSERT INTO recipient(email_id,recipient_id,ngo_name,phone_number,address,city,state,pincode,quantity_required_inGrams,redistribution_time_span_inHours)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

val=[
    ('abc@gmail.com','1','Goonj',' 9398165342','ramapuram','chennai','tamilnadu','654654','4','2'),
    ('bcd@gmail.com','2','pratham','9398165342','vani_nagar',' mumbai',' maharastra','213416','20','3'),
    ('efg@gamil.com','4','actionaid','9398165342','prasanth_nagar',' kanyakumari','tamilnadu','897764','50','5'),
    ('hij@gmail.com','5','BARC','9398165342','tdp_area','jammu ', 'kashmir','564534','80','6'),
    ('lmn@gmail.com','6','catholic relife services','9398165342','wee_place',' mumbai', 'madyapradesh','645466','90','7'),
    ('kml@gmail.com','7','deepalaya','9398165342','telugu_place','delhi ','uttarpradesh','544352','53','4'),
    ('one@gmail.com','8','give foundation','9398165342','ysrcp_area','shimla ','uttarpradesh','545361','45','3'),
    ('two@gmail.com','9','sammaan','9398165342','prabhas_nagar','nellore ','andhrapradesh','209870','89','9'),
    ('ten@gmail.com','10','action against hunger','9398165342','koyembedu',' tirupati','andhrapradesh','786754','85','4'),
    ('red@gmail.com','11','world now','9398165342','kilpauk',' ','tamilnadu','284534','45','7'),
    ('mno@gmail.com','12','who','9398165342','hell','hyderabad','telangana','203425','76','8'),
    ('uno@gmail.com','13','caring hearts','9398165342','hevenly_area','west_bengal ','2023-01-03','bengal','406234','43','7'),
    ('ino@gmail.com','14','uniting our world','9398165342','valluvari_salai','kolkata ','bengal','457892','45','4'),
    ('bal@gmail.com','15','novo','9398165342','embacy_nagar',' kanpur','karnataka','434456','55','4' )
]  
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
