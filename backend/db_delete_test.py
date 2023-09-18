import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="parade",
        port=5432)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # DELETE all rows from the "your_table_name" table
    delete_query = "DELETE FROM polaroids WHERE id = 2"
    cursor.execute(delete_query)

    # Commit the transaction
    connection.commit()

    print(f"All values deleted from 'your_table_name' table successfully!")

    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
