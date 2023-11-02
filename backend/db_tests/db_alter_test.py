import psycopg2

# Define your PostgreSQL connection parameters
conn_params = {
    'host': "localhost",
    'database': "postgres",
    'user': "postgres",
    'password': "parade",
    'port': 5432
}

# Connect to the database
conn = psycopg2.connect(**conn_params)

# Create a cursor object
cursor = conn.cursor()

# Define the ALTER TABLE statement to add a new column
alter_table_query = "ALTER TABLE polaroids ADD COLUMN R integer;"
alter_table_query_g = "ALTER TABLE polaroids ADD COLUMN G integer;"
alter_table_query_b = "ALTER TABLE polaroids ADD COLUMN B integer;"

# Execute the ALTER TABLE statement
cursor.execute(alter_table_query)
cursor.execute(alter_table_query_g)
cursor.execute(alter_table_query_b)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
