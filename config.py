from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql

# Load environment variables from .env file
load_dotenv()

# Connect to PostgreSQL database
def connect():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Check the connection
def check(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        print("Database connection is working.")
        cursor.close()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    check(connect())
