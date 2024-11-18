from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            query_check_member = "SELECT id FROM Members WHERE id = %s"
            cursor.execute(query_check_member, (member_id,))
            result = cursor.fetchone()

            if not result:
                print(f"Member with id {member_id} does not exist. Skipping workout session.")
            else:
                query_insert_session = """
                INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query_insert_session, (member_id, date, duration_minutes, calories_burned))
                
                conn.commit()

                print(f"Workout session added for member {member_id} on {date}.")
            
            cursor.close()

    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

try:
    add_workout_session(2, '2024-11-18', 45, 350)
   

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")