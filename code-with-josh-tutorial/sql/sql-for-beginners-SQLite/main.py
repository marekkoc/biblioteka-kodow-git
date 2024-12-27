"""
Code with Josh
YT: SQL in Python for Beginners | Python Tutorial (https://www.youtube.com/watch?v=tXJtY51xHq8&t=5s)

Created: 2024.12.25
Modified: 2024.12.26
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
        
# Step 3: Add user to database
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User {name} was added to your database!")
    except Exception as e:
        print(f"Exception with: insert user: {e}")

# Step 4: Query all users in database 
def fetch_users(connection, condition="") -> list[tuple]: #(mk,47, mk@gmail.com)
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    try:
        with connection:
            rows = connection.execute(query).fetchall()           
        return rows
    except Exception as e:
        print(f"Exception in fetch_users: {e}")

# Step 5: Delete a user from the database
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try:
        with connection:
            connection.execute(query, (user_id,))
        print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(f"delete_user: {e}")

# Step 6: Update an existing user
def update_user(connection, user_id:int, email:str):
    query = "UPDATE users SET email = ? WHERE id = ?"
    try:
        with connection:
            connection.execute(query, (email, user_id))
        print(f"User ID {user_id} has a new email of {email}")
    except Exception as e:
        print(f"update_user: {e}")

# Bonus: Ability to add Multiple users
def add_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} were added to the database!")
    except Exception as e:
        print(f"add_users: {e}")


# Main function wrapper
def main():
    connection = get_connection("subscribe.db")
    try:
        # create a table
        create_table(connection)

        x = int(input("1-activate, 2-freeze: "))
        while x != 2:

            start = input("Enter Option (Add, Delet, Update, Search, Add Many):").lower()
            if start == "add":
                name = input("Enter name: ")
                age:int = int(input("Enter age: "))
                email:str = input("Enter email: ")
                insert_user(connection, name, age, email)
            elif start == "search":
                print("All users:")
                for user in fetch_users(connection, "age < 55"):
                    print(user)
            elif start == "delete":
                user_id = int(input("Enter USER ID: "))
                delete_user(connection, user_id)
            elif start == "update":
                new_email = input("Enter a new email: ")
                user_id = int(input("Enter USER ID: "))
                update_user(connection, user_id, new_email)
            elif start == "add many":
                users_nubmer:int = int(input("Enter number of users: "))
                users_list:list[tuple[str, int, str]] = []
                for i in range(users_nubmer):
                    print(f"User: {i}/{users_nubmer}")
                    name: str = input(f"]tEnter name: ")
                    age:int = int(input("Enter age: "))
                    email:str = input("Enter email:")
                    users_list.append((name, age, email))
                add_users(connection, users_list) 
            x = int(input("1-activate, 2-freeze: "))

    finally:
        connection.close()


if __name__ == "__main__":
    main()
