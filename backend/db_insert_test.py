import psycopg2

import psycopg2


def read_image_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="parade",
        port=5432)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Insert a record into the "polaroids" table
    insert_query = "INSERT INTO polaroids (user_id, name, description, date, image) VALUES (%s, %s, %s, %s, %s)"



    values = (1, "doggy", "Portuguese water dog", "2020-03-18", read_image_file("../static/uploads/waterdog.jpg"))

    cursor.execute(insert_query, values)

    # Commit the transaction
    connection.commit()

    # Query data from the "polaroids" table
    select_query = "SELECT * FROM polaroids"
    cursor.execute(select_query)

    # Fetch and print the results
    records = cursor.fetchall()
    records[0]

    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    print('0')
