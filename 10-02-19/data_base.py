import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db",
    pool_size=10
)

cursor = database.cursor()

cursor.execute("CREATE TABLE BOOKS "
               "(ID INT AUTO_INCREMENT PRIMARY KEY,"
               "NAME VARCHAR (255),"
               "AUTHOR VARCHAR (255))")

cursor.execute("INSERT INTO BOOKS "
               "(NAME, AUTHOR) VALUES "
               "('Matrix', 'Neo')")

database.commit()

cursor.execute("SELECT * FROM BOOKS WHERE NAME = 'Matrix'")
result = cursor.fetchone()
print(result)

cursor.execute("DELETE FROM BOOKS WHERE AUTHOR = 'Michal Barnea'")
database.commit()

name = 'Guitars for dummies'
author = 'King Crimson'
id = 5

cursor.execute(f"UPDATE BOOKS "
               f"SET "
               f"NAME = '{name}', "
               f"AUTHOR = '{author}' "
               f"WHERE ID = {id}")

database.commit()



