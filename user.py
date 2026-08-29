from abc import ABC, abstractmethod
from event import Event


class User(ABC):
    total_users = 0

    def __init__(self, name, email):
        self.name = name

        # Keep the email private so it cannot be changed directly.
        self.__email = email

        User.total_users += 1

    @property
    def email(self):
        return self.__email

    @abstractmethod
    def get_role(self):
        pass

    def show_profile(self):
        print("Name:", self.name)
        print("Email:", self.email)


class Participant(User):

    def __init__(self, name, email):
        super().__init__(name, email)

        # A participant can have more than one registration.
        self.registrations = []

    def get_role(self):
        return "Participant"

    def register_for_event(self, event):
        registration = event.add_participant(self)

        if registration:
            self.registrations.append(registration)

        return registration

    def cancel_registration(self, registration):
        if registration in self.registrations:
            registration.cancel()


class Organizer(User):

    def __init__(self, name, email):
        super().__init__(name, email)

        # The organizer keeps track of the events they created.
        self.events = []

    def get_role(self):
        return "Organizer"

    def create_event(
        self,
        name,
        date,
        category,
        venue,
        capacity
    ):
        event = Event.create_event(
            name,
            date,
            category,
            venue,
            capacity
        )

        self.events.append(event)

        return event

    def delete_event(self, event):
        if event in self.events:
            self.events.remove(event)
            return True

        return False

    def show_events(self):
        if not self.events:
            print("No events available.")
            return

        for event in self.events:
            event.show_event()