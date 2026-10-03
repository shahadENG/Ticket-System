import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alra143DSAzz",
    database="ticket_system"
)

print("Connected successfully!")

cursor = connection.cursor()

sql = """
INSERT INTO tickets (title, description, status)
VALUES (%s, %s, %s)
"""

values = ("Computer problem", "The computer is not working", "Pending")

cursor.execute(sql, values)

connection.commit()
cursor.execute("SELECT * FROM tickets") 
tickets = cursor.fetchall() 
for ticket in tickets: print(ticket)

connection.close()