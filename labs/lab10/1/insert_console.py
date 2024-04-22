import psycopg2

def insert_all(name, surname, phone_number, home_number):

    sql = """INSERT INTO phone_book(name, surname, phone_number, home_number)
             VALUES(%s, %s, %s, %s) RETURNING id;"""  
    
    id = None

    try:
        with psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, surname, phone_number, home_number,))

                row = cur.fetchone()  
                if row:
                    id = row[0]  

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return id

def insert_many(phoneBook_list):

    sql = "INSERT INTO phone_book(name, surname, phone_number, home_number) VALUES(%s, %s, %s, %s)"
    
    try:
        with psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                for obj in phoneBook_list:
                    cur.execute(sql, obj)  

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':

    name = input("Name: ")
    surname = input("Surname: ")
    phone_number = input("Phone number: ")
    home_number = input("Home number:")

    storage = [
        (name, surname, phone_number, home_number), 
    ]

    insert_many(storage) 
