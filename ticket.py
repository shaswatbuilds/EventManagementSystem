class Ticket:
    # Each new ticket gets the next available number.
    next_number = 1000

    def __init__(self, registration):
        self.registration = registration
        self.number = Ticket.next_number

        Ticket.next_number += 1

    def show_ticket(self):
        participant = self.registration.participant
        event = self.registration.event

        print()
        print("========== TICKET ==========")
        print("Ticket:", self.number)
        print("Name:", participant.name)
        print("Email:", participant.email)
        print("Event:", event.name)
        print("Date:", event.date)
        print("Venue:", event.venue)
        print("============================")