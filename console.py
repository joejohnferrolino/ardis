from config import connect
from utils import is_valid_email

# User creation
def create_user(connection, name, email):
    try:
        with connection.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
                (name, email)
            )
            user_id = cur.fetchone()[0]
            connection.commit()
            print(f"User created with ID: {user_id}")
    except Exception as e:
        print(f"Error creating user: {e}")

# List of users
def read_users(connection):
    try:
        with connection.cursor() as cur:
            cur.execute("SELECT id, name, email FROM users;")
            rows = cur.fetchall()
            if not rows:
                print("No user records found.")
            else:
                for row in rows:
                    print(row)
    except Exception as e:
        print(f"Error reading users: {e}")

# Update user
def update_user(connection, user_id, name, email):
    try:
        with connection.cursor() as cur:
            # Check if the user exists
            cur.execute("SELECT 1 FROM users WHERE id = %s;", (user_id,))
            if cur.fetchone() is None:
                print(f"No user found with ID {user_id}.")
                return

            # Perform the update
            cur.execute(
                "UPDATE users SET name = %s, email = %s WHERE id = %s;",
                (name, email, user_id)
            )
            rows_affected = cur.rowcount
            connection.commit()

            if rows_affected > 0:
                print(f"User with ID {user_id} updated.")
            else:
                print(f"Failed to update user with ID {user_id}.")
    except Exception as e:
        print(f"Error updating user: {e}")

# Delete user
def delete_user(connection, user_id):
    try:
        with connection.cursor() as cur:
            # Check if the user exists
            cur.execute("SELECT 1 FROM users WHERE id = %s;", (user_id,))
            if cur.fetchone() is None:
                print(f"No user found with ID {user_id}.")
                return

            # Perform the delete
            cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            rows_deleted = cur.rowcount
            connection.commit()
            if rows_deleted > 0:
                print(f"User with ID {user_id} deleted.")
            else:
                print(f"Failed to delete user with ID {user_id}.")
    except Exception as e:
        print(f"Error deleting user: {e}")

# Main function
def main():
    connection = connect()
    if connection is None:
        return

    while True:
        print("\nSelect an operation:")
        print("1: Create User")
        print("2: Read Users")
        print("3: Update User")
        print("4: Delete User")
        print("5: Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            while True:
                email = input("Enter email: ")
                if is_valid_email(email):
                    break
                else:
                    print("Invalid email address. Please enter a valid email.")

            create_user(connection, name, email)
        elif choice == '2':
            read_users(connection)
        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to update: "))
                name = input("Enter new name: ")

                while True:
                    email = input("Enter new email: ")
                    if is_valid_email(email):
                        break
                    else:
                        print("Invalid email address. Please enter a valid email.")

                update_user(connection, user_id, name, email)
            except ValueError:
                print("Invalid input. Please enter a valid number for the user ID.")
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(connection, user_id)
            except ValueError:
                print("Invalid input. Please enter a valid number for the user ID.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()

if __name__ == "__main__":
    main()
