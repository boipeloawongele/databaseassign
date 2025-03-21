import mysql.connector 

#Connect to MYSQL Server
conn =mysql.connector.connect(
    host ="localhost",
    user ="root",#Add User
    password = "Elizabethsekoena20!" #Add Password
)

#Create a cursor object
cursor = conn.cursor()

#Create new database
database_name = "sales.DB" #Add a unique Database name
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}if created successfully!")

#Close the connection
cursor.close()
conn.close()