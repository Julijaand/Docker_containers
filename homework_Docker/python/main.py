import mysql.connector
from decouple import config

# When connecting to already existing database:
connection = mysql.connector.connect(
    host='mysql',
    user=config('username'),
    password=config('password'),
    database='db',
    port='3306'
)
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM employees')
employees = cursor.fetchall()
connection.close()

print(employees)

