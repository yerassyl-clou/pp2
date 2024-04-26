import psycopg2

def selectDataByName(name=None):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book_2", user="postgres", password="123")
        
        cur = conn.cursor()

        condition = ""
        values = []
        if name:
            condition += "name = %s"
            values.append(name)
        
        query = "SELECT * FROM phone_book_2"
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

def selectDataBySurname(surname=None):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book_2", user="postgres", password="123")
        
        cur = conn.cursor()

        condition = ""
        values = []
        if surname:
            condition += "surname = %s"
            values.append(surname)
        
        query = "SELECT * FROM phone_book_2"
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

def selectDataByNumber(number=None):
    try:
        conn = psycopg2.connect(host="localhost", database="phone_book_2", user="postgres", password="123")
        
        cur = conn.cursor()

        condition = ""
        values = []
        if number:
            condition += "phone_number = %s"
            values.append(number)
        
        query = "SELECT * FROM phone_book_2"
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


x = int(input("Choose a patern: 1.Name 2.Surname 3.Phone number    "))

if x == 1:
    name = str(input("name: "))
    selectDataByName(name)
elif x == 2:
    surname = str(input("surname: "))
    selectDataBySurname(surname)
elif x == 3:    
    phone_number = str(input("phone number: "))
    selectDataByNumber(phone_number)    
else:
    print("Selected wrong pattern")


