import psycopg2

def delete_data_by_phone(phone_number):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123")
        cur = conn.cursor()

        query = "DELETE FROM phone_book WHERE phone_number = %s"
        
        cur.execute(query, (phone_number,))

        conn.commit()
        
        print("Deleted")

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

phone_number = input("Enter the number to delete: ")

delete_data_by_phone(phone_number)
