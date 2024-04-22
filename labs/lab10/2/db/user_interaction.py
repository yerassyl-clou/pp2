import psycopg2

def get_user_level(username):
    try:
        # Connect to the database
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            # Create a cursor object to execute SQL queries
            with conn.cursor() as cur:
                # Execute the SQL query to retrieve the user's level
                cur.execute("SELECT level FROM users WHERE username = %s ORDER BY level DESC LIMIT 1", (username,))
                # Fetch the result (level) from the query
                level = cur.fetchone()
                # If a level is found, return it; otherwise, return None
                if level:
                    return level[0]
                else:
                    return None
    except (psycopg2.DatabaseError, Exception) as error:
        # Print any errors that occur during the database operation
        print(error)
        return None

def create_new_user(username):
    try:
        # Connect to the database
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            # Create a cursor object to execute SQL queries
            with conn.cursor() as cur:
                # Execute the SQL query to insert a new user
                cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
                # Commit the transaction to save the changes to the database
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        # Print any errors that occur during the database operation
        print(error)
