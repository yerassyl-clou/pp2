import psycopg2

def insert_or_update():

    name = input("Name: ")
    
    try:
        with psycopg2.connect(host="localhost", database="phone_book_2", user="postgres", password="123") as conn:

            with conn.cursor() as cur:                                                                
                cur.execute("SELECT id FROM phone_book_2 WHERE name = %s", (name,))
                row = cur.fetchone()

                if row:                                                                             #Check username for existance  
                    phone_number = input("Phone number: ")
                    user_id = row[0]
                    cur.execute("UPDATE phone_book_2 SET phone_number = %s WHERE id = %s",
                                (phone_number, user_id))  

                else:                                                                               #If not get new data     
                    surname = input("Surname: ")
                    phone_number = input("Phone number: ")
                    home_number = input("Home number:")
                    
                    cur.execute("INSERT INTO phone_book_2(name, surname, phone_number, home_number) VALUES(%s, %s, %s, %s) RETURNING id",
                                (name, surname, phone_number, home_number,))
                    row = cur.fetchone()
                    user_id = row[0]

                conn.commit()
                return user_id
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


user = insert_or_update()
if user:
    print("success, ID:", user)
else:
    print("Fail")
