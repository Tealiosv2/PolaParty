import psycopg2
from PIL import Image
from io import BytesIO
import base64


def connect():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="parade",
            port=5432)

        # Create a cursor object to interact with the database

        return connection


    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


def read_image_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


def db_read():
    connection = connect()
    cursor = connection.cursor()
    # Execute a SELECT query to retrieve data from the "images" table
    select_query = "SELECT * FROM polaroids"
    cursor.execute(select_query)

    # Fetch all the rows returned by the query
    records = []

    for row in cursor.fetchall():
        image64 = base64.b64encode(row[5]).decode('utf-8')

        record = {
            'id': row[0],
            'userid': row[1],
            'name': row[2],
            'description': row[3],
            'date': row[4],
            'image': image64
        }
        records.append(record)

    connection.close()

    return records


def db_write(userid, name, description, date, image_path, R, G, B):
    connection = connect()

    cursor = connection.cursor()

    insert_query = "INSERT INTO polaroids (user_id, name, description, date, image, R, G, B) " \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    values = (userid, name, description, date, read_image_file(image_path), R, G, B)

    cursor.execute(insert_query, values)

    # Commit the transaction
    connection.commit()

    connection.close()
