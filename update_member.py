from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()


def update_member_age(member_id, new_age):
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            query_check_member = "SELECT id FROM Members WHERE id = %s"
            cursor.execute(query_check_member, (member_id,))
            result = cursor.fetchone()

            if not result:
                print(f"Member with id {member_id} does not exist. Skipping update.")
            else:
                query_update_age = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query_update_age, (new_age, member_id))

                conn.commit()

                print(f"Age of member with id {member_id} updated to {new_age}.")
            
            cursor.close()

    except Error as error:
        print(f"Error: {error}")

    except Exception as e:
        print(f"Error: {e}")

try:
    
    update_member_age(1, 27) 
    

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")