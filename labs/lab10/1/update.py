import psycopg2

def update_name(id, name, old_name):
    """Update the name in the phone_book table."""
    updated_row_count = 0

    sql = """UPDATE phone_book 
             SET name = %s 
             WHERE id = %s AND name = %s"""

    try:
        with psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                # Execute the UPDATE statement
                cur.execute(sql, (name, id, old_name))
                updated_row_count = cur.rowcount

            # Commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def update_phone(id, phone_number, old_phone_number):
    """Update the phone number in the phone_book table."""
    updated_row_count = 0

    sql = """UPDATE phone_book 
             SET phone_number = %s 
             WHERE id = %s AND phone_number = %s"""

    try:
        with psycopg2.connect(host="localhost", database="phone_book", user="postgres", password="123") as conn:
            with conn.cursor() as cur:
                # Execute the UPDATE statement
                cur.execute(sql, (phone_number, id, old_phone_number))
                updated_row_count = cur.rowcount

            # Commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    num = int(input("Change of: 1-name, 2-phone number: "))

    if num == 1:
        update_name(12, "Walter", "Frank")
    elif num == 2:
        update_phone(12, "+78889990011", "+77018340909")
    else:
        print("error")
