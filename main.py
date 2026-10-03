
import mysql.connector
from Ticket import Ticket

# object
# ticket1 = Ticket("login Problem", "cannot login")

# ticket2 = Ticket("Network Problem", "Internet is not working")

# ticket3 = Ticket("Software Problem", "Program keeps crashing")

# ticket1.change_status("Open")
# print(ticket1.title)
# print(ticket1.description)
# print(ticket1.status)

#
# Create a list for all tickets
tickets = []

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alra143DSAzz",
    database="ticket_system"
)

cursor = connection.cursor()

print("Database connected!")

while True:

    print("----IT Ticket System-----")
    print("1.Add Ticket")
    print("2. View Ticket")
    print("3. Change Ticket Status")
    print("4. Exit")

    choice = input("Choose an Option :")
    
    if choice == "1":
        title = input("Enter ticket title :")
        description = input("Enter ticket description :")
        TK = Ticket(title, description)

        tickets.append(TK)
        print("Ticket added successfully")

        sql = """
        INSERT INTO tickets (title, description, status)
        VALUES (%s, %s, %s)
        """

        values = (title, description, TK.status)

        cursor.execute(sql, values)
        connection.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM tickets")
        tickets_from_db = cursor.fetchall()

        if len(tickets_from_db) == 0:
            print("No tickets found")
        else:
            for ticket in tickets_from_db:
                print("ID:", ticket[0])
                print("Title:", ticket[1])
                print("Description:", ticket[2])
                print("Status:", ticket[3])

        # len == length
        # enumerate == تعطي رقم العنصر + العنصر نفسه
        # i رقم العنصر
        # tk التذكره نفسها

    elif choice == "3":
        cursor.execute("SELECT * FROM tickets")
        tickets_from_db = cursor.fetchall()

        if len(tickets_from_db) == 0:
            print("No ticket found")
        else:
            for ticket in tickets_from_db:
                print(ticket[0], "-", ticket[1])

            ticket_number = int(input("choose ticket number : "))

            new_status = input(
                "Enter new status (Open/In Progress/Closed): "
            )

            sql = """
            UPDATE tickets
            SET status = %s
            WHERE id = %s
            """

            values = (new_status, ticket_number)
            cursor.execute(sql, values)
            connection.commit()

            print("Status updated successfully!")

    elif choice == "4":
        print("bye")
        connection.close()
        break


# while True:
#     title = input("Enter ticket title: ")
#     description = input("Enter ticket description: ")

#     TK = Ticket(title, description)
#     tickets.append(TK)

#     choice = input("Do you want to add another ticket? (yes/no): ")
#     choice = choice.lower()

#     if choice == "no":
#         break


# Print tickets
# print(ticket1.status)
# print(ticket2.status)
# print(ticket3.status)


# u can rename ticket in loop

# for ticket in tickets:
#     print(ticket.status)


# title = input("Enter ticket title: ")
# description = input("Enter ticket description: ")

# for tk in tickets:
#     print(tk.title)
#     print(tk.description)
#     print(tk.status)


# TK = Ticket(title, description)
# tickets.append(TK)
# print(tickets)


# نرجع نطبع باستخدام الفور

# for tk in tickets:
#     print(tk.title)
#     print(tk.description)
#     print(tk.status)

