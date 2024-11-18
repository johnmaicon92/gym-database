from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()

def get_members_in_age_range(start_age, end_age):
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            query = """
                SELECT id, name, age
                FROM Members
                WHERE age BETWEEN %s AND %s
                ORDER BY age
            """
            cursor.execute(query, (start_age, end_age))

            members = cursor.fetchall()

            if members:
                print(f"Members between ages {start_age} and {end_age}:")
                for member in members:
                    print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
            else:
                print(f"No members found in the age range {start_age} to {end_age}.")
          
            cursor.close()

    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
       
        if conn.is_connected():
            conn.close()
            print("Connection closed.")


try:
    get_members_in_age_range(1, 50)  
finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")