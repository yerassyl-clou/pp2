import psycopg2

def selectData(name=None, surname=None, phone_number=None, home_number=None):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123")
        
        cur = conn.cursor()

        condition = ""
        values = []
        if name:
            condition += "name = %s"
            values.append(name)
        if surname:
            condition += " AND surname = %s"
            values.append(surname)
        if phone_number:
            condition += " AND phone_number = %s"
            values.append(phone_number)
        if home_number:
            condition += " AND home_number = %s"
            values.append(home_number)
        
        query = "SELECT * FROM phone_book"
        if condition:
            query += " WHERE " + condition
        cur.execute(query, values)
        
        rows = cur.fetchall()
        
        for row in rows:
            print(row)  
            
        cur.close()
        conn.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

name = str(input("name: "))
surname = str(input("surname: "))
phone_number = str(input("phone number: "))
home_number = str(input("home number: "))

selectData(name, surname, phone_number, home_number)