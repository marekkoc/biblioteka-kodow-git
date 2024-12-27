"""
Code with Josh
YT: SQL in Python for Beginners | Python Tutorial (https://www.youtube.com/watch?v=tXJtY51xHq8&t=5s)

Test: próba dodania warunku przy określającego zakres wypiswanych danych z tabeliw funkcji: fetch_user()

Created: 2024.12.27
Modified: 2024.12.27
"""
# All of our imports
import sqlite3
from icecream import ic as print


# Step 1: Setup / initialize our database
def get_connection(db_name):
    try:
        return sqlite3.Connection(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise

# Step 2: Create a table in the database
def create_table(connection):
    # DataBase can be though of as a spreadsheet --> a spreadsheet can contain multiple tables
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("Table was created")
    except Exception as e:
        print(e)
        
# Step 4: Query all users in database 
def fetch_users(connection, condition="") -> list[tuple]: #(mk,47, mk@gmail.com)
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    
    print(f"\n {query} \n")
    
          
    try:
        with connection:
            rows = connection.execute(query).fetchall()           
        return rows
    except Exception as e:
        print(f"Exception in fetch_users: {e}")


# Main function wrapper
def main():
    connection = get_connection("subscribe.db")
    try:
        # create a table
        create_table(connection)

        print("All users:")
        for user in fetch_users(connection, 'age < 55 and age > 20'):
            print(user)        

    finally:
        connection.close()


if __name__ == "__main__":
    main()
