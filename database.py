import psycopg2

import credentials

# Render PostgreSQL connection details
db_params = {
    "dbname": credentials.DB_NAME,
    "user": credentials.DB_USERNAME,
    "password": credentials.DB_PASSWORD,
    "host": credentials.DB_HOST_NAME_EXTERNAL,
    "port": credentials.DB_PORT
}

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    print("Connected to the database successfully!")

    # Create a cursor object
    cur = conn.cursor()

    # Execute a sample query
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("Database version:", db_version)

    # Example: Create a table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
    """)
    print("Table 'users' created or already exists.")

    # Example: Insert a record
    cur.execute("""
        INSERT INTO users (name, email) VALUES (%s, %s)
    """, ("John Doe", "john.doe@example.com"))
    print("Record inserted successfully.")

    # Commit the transaction
    conn.commit()

    # Example: Query the table
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    print("\nRecords in the table:")
    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()