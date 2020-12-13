import mysql.connector

HOST = "localhost"
USER = "tejesh"
PASSWORD = "sivaganga21"
DATABASE = "library"


def get_database():
    try:
        database = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = database.cursor(dictionary=True)
        return database, cursor
    except mysql.connector.Error:
        return None, None
