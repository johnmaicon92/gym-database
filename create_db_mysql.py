# import mysql.connector
# from mysql.connector import Error

# def create_database():

#     user = "root"
#     password = "1Johnjohn"
#     host = "localhost"
#     db_name = "gym_db"

#     conn = None
    
#     try:
#         conn = mysql.connector.connect(
#             user = user,
#             password = password,
#             host = host
#         )

#         cursor = conn.cursor()
#         cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{db_name}'")
#         result = cursor.fetchone()

#         if not result:
#             cursor.execute(f"CREATE DATABASE {db_name}")
#             print(f"Database '{db_name}' created successfully.")
#         conn.database = db_name
        
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS Members (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(100),
#                 age INT
#             )
#             """)
#         print("Table 'Members' created successfully.")

#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS WorkoutSessions (
#                 session_id INT AUTO_INCREMENT PRIMARY KEY,
#                 member_id INT,
#                 date DATE,
#                 duration_minutes INT,
#                 calories_burned INT,
#                 FOREIGN KEY (member_id) REFERENCES Members(id)
#             )
#             """)

#         print("Table 'WorkoutSessions' created successfully.")
       
       
#         cursor.execute("SHOW TABLES")
#         tables = cursor.fetchall()
#         print("Tables in the database:")
#         for table in tables:
#             print(table)
#         cursor.close()
        

#         if conn.is_connected():
#             print("Connected to MySQL database successfully")
#             return conn
        

#     except Error as e:
#         print(f"Error: {e}")
#         return None
    
#     finally:
#         if conn and conn.is_connected():
#             conn.close()


# create_database()

