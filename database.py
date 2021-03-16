import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "0_Bietjes_",
    database = "testdatabase",
    )

my_cursor = mydb.cursor() # cursor maken

# # database maken, hoeft maar één keer, daarom nu uitgegrijsd
# my_cursor.execute("CREATE DATABASE testdatabase")

# # laat de databases zien die zijn gemaakt
# my_cursor.execute("SHOW DATABASES")
# for dbase in my_cursor:
#   print(dbase[0])

# # tabel maken
# my_cursor.execute('CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(3), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#   print(table[0])

# # één record (rij) toevoegen
# basis = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Robbie Williams", "rowi@randomsite.co.uk", 51)
# my_cursor.execute(basis, record1)
# mydb.commit()

# # nog een om te oefenen
# basis = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record = ("John Travolta", "pulpfiction@comebacks.com", 67)
# my_cursor.execute(basis, record)
# mydb.commit()

# # meerdere records toevoegen
# basis = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# records = [("Tim Timson", "timmyboy.timmymail.com", 16),
#     ("Heather Forest", "info@heathersweather.com", 44),
#     ("Ed Lemon", "grandpa_ed@grandpasunite.co.uk", 91),]
# my_cursor.executemany(basis, records)
# mydb.commit()

# # data uit een tabel selecteren: alle kolommen
# my_cursor.execute("SELECT * FROM users")
# opgehaald = my_cursor.fetchall()
# print("NAME\t\tEMAIL\t\tAGE\t\tUSER_ID")
# for record in opgehaald:
#     print(record[0] + "\t\t%s" %record[1] + "\t\t%s" %record[2] + "\t\t%s" %record[3])

# # alternatieve schrijfwijze
# my_cursor.execute("SELECT * FROM users")
# opgehaald = my_cursor.fetchall()
# for record in opgehaald:
#     print(f"{record[0]}, {record[1]}, {record[2]}")

# # data uit een tabel selecteren: 2 kolommen
# my_cursor.execute("SELECT name, age FROM users")
# opgehaald = my_cursor.fetchall()
# for record in opgehaald:
#     print(record)

# # deel van de records ophalen dat voldoet aan een voorwaarde
# my_cursor.execute("SELECT * FROM users WHERE age >= 18")
# boven18 = my_cursor.fetchall()
# for user in boven18:
#     print(user)

# # deel van de records ophalen dat voldoet aan een voorwaarde, in dit geval om het e-mailadres te vinden.
# my_cursor.execute("SELECT * FROM users WHERE name = 'Heather Forest'")
# Heather = my_cursor.fetchall()
# for user in Heather:
#     print(user[1])

# # records ophalen via LIKE en wildcards
# my_cursor.execute("SELECT * FROM users WHERE email LIKE '%uk' AND age >= 18")
# result = my_cursor.fetchall()
# for record in result:
#     print(record)

# # records updaten, eerste twee regels kunnen ook op één regel zonder 'bijwerken'
# bijwerken = "UPDATE users SET age = 66 WHERE user_id = 5"
# my_cursor.execute(bijwerken)
# mydb.commit()

# # resultaten beperken
# my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 2")
# my_cursor.execute("SELECT * FROM users ORDER BY age DESC")
# result = my_cursor.fetchall()
# for record in result:
#     print(record)

# # records verwijderen
# te_verwijderen = "DELETE FROM users WHERE user_id = 5"
# my_cursor.execute(te_verwijderen)
# mydb.commit()

# hele tabel weergeven
my_cursor.execute("SELECT * FROM users")
alle_items = my_cursor.fetchall()
for item in alle_items:
    print(item)

# # hele tabel verwijderen (drop genaamd in MySQL)
# te_verwijderen = "DROP TABLE IF EXISTS users"
# my_cursor.execute(te_verwijderen)