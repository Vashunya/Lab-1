import psycopg2
import csv
import re

def number_cheking(number):
    return bool(re.match(r'^\+7\d{10}', number))

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="ccffgc",
    host="localhost",
    port="7777"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. Add contact by CSV")
    print("3. Redact contact")
    print("4. Find contact")
    print("5. Delete contact")
    print("6. Show all phonebook")
    print("7. Search by pattern")
    print("8. Bulk insert from list")
    print("9. Paginated contacts")
    print("0. Quit")

    choice = input("Chose the num: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Number: ")
        if number_cheking(phone):
            cur.execute("CALL insert_update(%s, %s)", (name, phone))
            conn.commit()
            print("Succesful!")
        else: print("Wrong number format")

    elif choice == "2":
        filename = input("CSV file name: ")
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if number_cheking(row[1]):
                        cur.execute("CALL insert_update(%s, %s)", (row[0], row[1]))
                conn.commit()
            print("Succesful!")
        except:
            print("Try again")

    elif choice == "3":
        name = input("Name to change: ")
        new_phone = input("New number: ")
        if number_cheking(new_phone):
            cur.execute("CALL insert_update(%s, %s)", (name, new_phone))
            conn.commit()
            print("Succesful!")
        else:
            print("Invalid number format")

    elif choice == "4":
        keyword = input("Name to find: ")
        cur.execute("SELECT * FROM search_with(%s)", (keyword,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"{row[1]}: {row[2]}")
        else:
            print("Try again")

    elif choice == "5":
        value = input("Name or number to delete: ")
        cur.execute("CALL del(%s)", (value, ))
        conn.commit()
        print("Deleted")

    elif choice == "6":
        cur.execute("SELECT * FROM phonebook")
        contacts = cur.fetchall()
        if contacts:
            for row in contacts:
                print(f"{row[1]}: {row[2]}")
        else:
            print("Enmpty")

    elif choice == "7":
        pattern = input("Enter search pattern: ")
        cur.execute("SELECT * FROM search_with(%s)", (pattern,))
        results = cur.fetchall()
        for row in results:
            print(f"{row[1]}: {row[2]}")
        if not results:
            print("No result")

    #elif choice == "8":    

    elif choice == "9":
        limit = 2
        page = int(input("Chose page number: "))
        offset = (page - 1) * limit
        cur.execute("SELECT * FROM paginate(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(f"{row[1]}: {row[2]}")
        if not rows:
            print("No data for this page")

    elif choice == "0":
        print("Quit")
        break

    else:
        print("Chose again")
        
cur.close()
conn.close()