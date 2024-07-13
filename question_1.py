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

    try:
        def add_member():
            new_member = (9, "Jeff Hulter", 36)
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, new_member)
            conn.commit()
            print("New Member Added!")
        add_member()
        def add_workout_session():
            new_session = (1, 9, "2021-2-22", 120, 1000)
            query = "INSERT INTO WorkoutSessions (session_id, member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, new_session)
            conn.commit()
            print("New Session Added!")
        add_workout_session()
        def update_member_age():
            update = (9, 37)
            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, update)
            conn.commit()
            print("Age updated!")
        update_member_age()
        def delete_workout_session():
            session = (1, )
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, session)
            conn.commit()
            print("Session removed!")
        delete_workout_session()
    except Error as e:
            print(f"Error: {e}")



except Error as e:
    print(f"Error: {e}")

