import csv
import psycopg2

def insert_from_csv(csv_file):
    """Insert data from a CSV file into the database."""
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists
            data = [tuple(row) for row in reader]  # Convert each row into a tuple
            print("Data read from CSV:", data)  # Debugging: print the data read from CSV
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return

    insert_many(data)  # Call insert_many function to insert the data into the database
 

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
    insert_from_csv("/Users/yerassyl/vscode/kbtu/pp2/labs/lab10/data.csv")
