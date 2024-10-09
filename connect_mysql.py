import mysql.connector
from mysql.connector import Error





def connect_database():
    # Database connection parameters
    db_name = "library_management"
    user = "root"
    password = "Tekking58!"
    host = "localhost"
    # port = 3307  # Specify the port separately
    
    print("Attempting to connect to the database...")  # Debugging statement

    try:
        # Try establishing the connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
           # port=port,
           
        )
        
        # Check if the connection is successful
        if conn.is_connected():
            print("Connected to MySQL database successfully")  
            return conn
        else:
            print("Failed to connect to the database")  
            return None
    
    except Error as e:
        print(f"Error: {e}") 
        return None
connect_database()