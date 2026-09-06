from Ticket import Ticket
#object
# ticket1 = Ticket("login Problem" , "cannot login")

# ticket2 =Ticket("Network Problem","Internet is not working")

# ticket3 =Ticket("Software Problem","Program keeps crashing")

#ticket1.change_status("Open")
# print(ticket1.title)
# print(ticket1.description)
# print(ticket1.status)
#
# Create a list for all tickets
tickets = []

while True:
    title = input("Enter ticket title: ")
    description = input("Enter ticket description: ")

    TK = Ticket(title, description)
    tickets.append(TK)

    choice = input("Do you want to add another ticket? (yes/no): ")
    choice = choice.lower()

    if choice == "no":
        break
#

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

#نرجع نطبع باستخدام الفور

for tk in tickets:
    print(tk.title)
    print(tk.description)
    print(tk.status)

