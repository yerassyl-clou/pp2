import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE phone_book (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            home_number VARCHAR(7) NOT NULL
        )
        """,)
    try:
        with psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()

