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

    update_query = """
        UPDATE polaroids
        SET name = %s, description = %s 
        WHERE id = %s;                
        """

    # Define the values for the update
    new_value1 = "dogs"  # Replace with the new value for column1
    new_value2 = "doggert"  # Replace with the new value for column2
    row_id_to_update = 1  # Replace with the specific row ID or condition

    # Execute the update query
    cursor.execute(update_query, (new_value1, new_value2, row_id_to_update))

    # Commit the transaction
    connection.commit()

    print(f"Row with ID {row_id_to_update} updated successfully!")

    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
