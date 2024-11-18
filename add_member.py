from connect_mysql import connect_database
from mysql.connector import Error
conn = connect_database()


def add_member(name, age):
    try:

        if conn.is_connected():
            cursor = conn.cursor()

            query_check = "SELECT id FROM Members WHERE name = %s AND age = %s"
            cursor.execute(query_check, (name, age))
            result = cursor.fetchone()

            if result:
                print(f"Member '{name}' with age {age} already exists. Skipping insertion.")
            else:
                query_insert = "INSERT INTO Members (name, age) VALUES (%s, %s)"
                cursor.execute(query_insert, (name, age))
                
                print(f"New member '{name}' added successfully with age {age}.")
            
            cursor.close()

    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
try:  
    add_member('John Doe', 32)
    add_member('Jane Doe', 25)
    add_member('Bob Smith', 45)
    add_member('Alice Johnson', 28)
    add_member('Mike Brown', 35)
    add_member('Emma Davis', 22)
    add_member('John Doe', 32)

    conn.commit()

finally:
    
    if conn.is_connected():
        conn.close()
        print("Connection closed.")



