import psycopg2

def select_data(columns, conditions):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123")
        cur = conn.cursor()

        query = f"SELECT {columns} FROM phone_book"
        if conditions:
            query += f" WHERE {conditions}"

        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


columns = str(input("choose what to select (In format, name, surname): "))
conditions = str(input("give conditions (In format, name = 'John' AND surname = 'Doe'): "))

select_data(columns, conditions)