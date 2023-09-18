import psycopg2
from PIL import Image
from io import BytesIO


try:
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="parade",
        port=5432)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a SELECT query to retrieve data from the "images" table
    select_query = "SELECT * FROM polaroids"
    cursor.execute(select_query)

    # Fetch all the rows returned by the query
    records = cursor.fetchall()

    print(records[0][2])
    print(records)

    image_data = records[0][5]

    image = Image.open(BytesIO(image_data))

    # saves the image to directory
    # output_dir = "../static/saved"
    # img_name = f"{records[0][2]}{records[0][0]}.jpg"
    # image.save(f"{output_dir}/{img_name}")

    # image will open
    # image.show()

    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
