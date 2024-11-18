from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()


def delete_member(member_id):
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            query_check_member = "SELECT id FROM Members WHERE id = %s"
            cursor.execute(query_check_member, (member_id,))
            result = cursor.fetchone()

            if not result:
                print(f"Member with id {member_id} does not exist. Skipping deletion.")
            else:
                query_delete_sessions = "DELETE FROM WorkoutSessions WHERE member_id = %s"
                cursor.execute(query_delete_sessions, (member_id,))
                print(f"Related workout sessions for member {member_id} deleted.")

                query_delete_member = "DELETE FROM Members WHERE id = %s"
                cursor.execute(query_delete_member, (member_id,))
                
                conn.commit()

                print(f"Member with id {member_id} deleted successfully.")
            
            cursor.close()

    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
try:
    
    delete_member(0) 

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")