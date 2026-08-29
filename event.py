from datetime import datetime

class Event:
    total_events = 0

    def __init__(
        self,
        name,
        date,
        category,
        venue,
        capacity
    ):
        self.name = name
        self.date = date
        self.category = category
        self.venue = venue
        self.capacity = capacity
        # Stores the participants registered for this event.
        self.participants = []
        Event.total_events += 1
    @classmethod
    def create_event(
        cls,
        name,
        date,
        category,
        venue,
        capacity
    ):
        return cls(
            name,
            date,
            category,
            venue,
            capacity
        )

    @staticmethod
    def valid_date(date):
        # Check whether the entered date follows YYYY-MM-DD.
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    def add_participant(self, participant):
        # Imported here to avoid a circular import between the classes.
        from registration import Registration
        if participant in self.participants:
            print("You are already registered.")
            return None
        if self.available_seats() <= 0:
            print("The event is full.")
            return None

        self.participants.append(participant)

        return Registration(participant, self)

    def remove_participant(self, participant):
        if participant in self.participants:
            self.participants.remove(participant)

    def available_seats(self):
        return self.capacity - len(self.participants)

    def show_event(self):
        print()
        print("Event:", self.name)
        print("Date:", self.date)
        print("Category:", self.category)
        print("Venue:", self.venue)
        print("Capacity:", self.capacity)
        print("Available seats:", self.available_seats())