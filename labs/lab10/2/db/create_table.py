import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            level INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_scores (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(user_id),
            level INTEGER NOT NULL,
            score INTEGER NOT NULL
        )
        """)
    try:
        with psycopg2.connect(host="localhost", database="snake", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                # Add ALTER TABLE command to add 'level' column to 'users' table
                cur.execute("""
                    ALTER TABLE users
                    ADD COLUMN IF NOT EXISTS level INTEGER;
                """)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
