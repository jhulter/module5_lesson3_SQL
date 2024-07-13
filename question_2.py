import mysql.connector
from mysql.connector import Error

db_name = "gym"
user = "root"
password = "Theezfoot7!"
host = "127.0.0.1"

try:
    conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host
    )

    if conn.is_connected():
        print("Connected to MySQL Database successful.")
    cursor = conn.cursor()
    def get_members_in_age_range(start_age, end_age):
        start_age = 25
        end_age = 50
        query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
        print(f"Members aged between {start_age} and {end_age}:")
        for member in cursor.fetchall():
            print(member)
    get_members_in_age_range(25, 50)
except Error as e:
    print(f"Error: {e}")

