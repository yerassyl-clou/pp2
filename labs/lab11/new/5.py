import psycopg2

def delete_data_by_phone(name):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book_2", user="postgres", password="123")
        cur = conn.cursor()

        query = "DELETE FROM phone_book_2 WHERE name = %s"
        
        cur.execute(query, (name,))

        conn.commit()
        
        print("Deleted")

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

name = input("Enter the username to delete: ")

delete_data_by_phone(name)
