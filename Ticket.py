class Ticket:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Pending"

    def change_status(self, new_status):
        self.status = new_status