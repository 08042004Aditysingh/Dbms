import mysql.connector
from mysql.connector import Error

# Function to create a connection to the MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',            # Your MySQL server host
            user='root',                 # Replace with your MySQL username
            password='ankur033',         # Replace with your MySQL password
            database='ankur__'             # Your database name
        )
        if connection.is_connected():
            print("Connected to MySQL database.")
    except Error as e:
        print(f"Error: {e}")
    return connection

# Function to execute an SQL query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to read all users from the database
def read_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()

# Function to edit (update) a user's details
def edit_user(connection, user_id, new_name, new_email):
    update_query = f"""
    UPDATE users
    SET name = '{new_name}', email = '{new_email}'
    WHERE id = {user_id};
    """
    execute_query(connection, update_query)

# Function to delete a user from the database
def delete_user(connection, user_id):
    delete_query = f"DELETE FROM users WHERE id = {user_id};"
    execute_query(connection, delete_query)
# Main block to execute the script
if __name__ == "__main__":
    conn = create_connection()

    if conn:
        # Clear existing users (optional)
        execute_query(conn, "DELETE FROM users;")

        # Add new users
        execute_query(conn, "INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');")
        execute_query(conn, "INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');")

        # Edit an existing user (ID 1)
        print("\nUpdating user with id 1...")
        edit_user(conn, 1, "Updated Alice", "updated_alice@example.com")

        # Delete a user (ID 2)
        print("\nDeleting user with id 2...")
        delete_user(conn, 2)

        # Read all users
        print("\nUsers in the database:")
        users = read_users(conn)
        for user in users:
            print(user)

        # Close the connection
        conn.close()
        
        
        
        
        
# sql code
        
# -- Create the database
# CREATE DATABASE IF NOT EXISTS ankur;

# -- Switch to the new database
# USE ankur;

# -- Create the users table
# CREATE TABLE IF NOT EXISTS user (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# );


# SELECT * FROM users;
