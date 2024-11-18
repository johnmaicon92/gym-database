from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()

def delete_workout_session(session_id):
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            query_check_session = "SELECT id FROM WorkoutSessions WHERE id = %s"
            cursor.execute(query_check_session, (session_id,))
            result = cursor.fetchone()

            if not result:
                print(f"Workout session with id {session_id} does not exist. Skipping deletion.")
            else:
                query_delete_session = "DELETE FROM WorkoutSessions WHERE id = %s"
                cursor.execute(query_delete_session, (session_id,))

                conn.commit()

                print(f"Workout session with id {session_id} deleted successfully.")
            
            cursor.close()

    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
try:
    delete_workout_session(0)

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")