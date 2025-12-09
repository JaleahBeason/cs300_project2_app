import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Opens and returns a connection to your cs300_project2 database.
    Change user/password to match your MySQL setup.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Catelaya1211!",
            database="cs300_project2"
        )
        return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None

