from datetime import datetime
from ticket import Ticket


class Registration:
    total_registrations = 0

    def __init__(self, participant, event):
        self.participant = participant
        self.event = event
        self.registration_date = datetime.now()
        self.status = "Registered"

        Registration.total_registrations += 1

        # A ticket is created when the registration is made.
        self.ticket = Ticket(self)

    def cancel(self):
        if self.status == "Cancelled":
            print("Registration is already cancelled.")
            return

        self.event.remove_participant(self.participant)
        self.status = "Cancelled"

        print("Registration cancelled.")

    def show_registration(self):
        print()
        print("Participant:", self.participant.name)
        print("Event:", self.event.name)
        print("Status:", self.status)
        print(
            "Registered on:",
            self.registration_date.strftime("%Y-%m-%d")
        )