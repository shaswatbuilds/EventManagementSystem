from user import Participant, Organizer
from event import Event


def create_event(organizer):
    print("\nCreate Event")

    name = input("Event name: ")
    date = input("Event date (YYYY-MM-DD): ")

    if not Event.valid_date(date):
        print("Invalid date.")
        return

    category = input("Category: ")
    venue = input("Venue: ")
    capacity = input("Capacity: ")

    if not capacity.isdigit():
        print("Capacity must be a number.")
        return

    capacity = int(capacity)

    if capacity <= 0:
        print("Capacity must be greater than zero.")
        return

    organizer.create_event(
        name,
        date,
        category,
        venue,
        capacity
    )

    print("Event created.")


def show_events(organizer):
    if not organizer.events:
        print("\nNo events available.")
        return

    for number, event in enumerate(
        organizer.events,
        start=1
    ):
        print("\nEvent", number)
        event.show_event()


def register(participant, organizer):
    if not organizer.events:
        print("\nNo events available.")
        return

    show_events(organizer)

    choice = input("\nSelect event: ")

    if not choice.isdigit():
        print("Enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(organizer.events):
        print("Invalid event.")
        return

    event = organizer.events[choice - 1]

    registration = participant.register_for_event(event)

    if registration:
        print("Registration successful.")
        registration.ticket.show_ticket()


def show_registrations(participant):
    if not participant.registrations:
        print("\nNo registrations.")
        return

    for registration in participant.registrations:
        registration.show_registration()


def cancel_registration(participant):
    if not participant.registrations:
        print("\nNo registrations.")
        return

    for number, registration in enumerate(
        participant.registrations,
        start=1
    ):
        print(
            number,
            "-",
            registration.event.name,
            "-",
            registration.status
        )

    choice = input("\nSelect registration: ")

    if not choice.isdigit():
        print("Enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(
        participant.registrations
    ):
        print("Invalid registration.")
        return

    registration = participant.registrations[choice - 1]

    participant.cancel_registration(registration)


def show_ticket(participant):
    if not participant.registrations:
        print("\nNo registrations.")
        return

    for number, registration in enumerate(
        participant.registrations,
        start=1
    ):
        print(
            number,
            "-",
            registration.event.name,
            "-",
            registration.status
        )

    choice = input("\nSelect registration: ")

    if not choice.isdigit():
        print("Enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(
        participant.registrations
    ):
        print("Invalid registration.")
        return

    registration = participant.registrations[choice - 1]

    registration.ticket.show_ticket()


def participant_menu(participant, organizer):
    while True:
        print("\nParticipant Menu")
        print("1. View events")
        print("2. Register for event")
        print("3. View registrations")
        print("4. Cancel registration")
        print("5. View ticket")
        print("6. Back")

        choice = input("Choose: ")

        if choice == "1":
            show_events(organizer)

        elif choice == "2":
            register(
                participant,
                organizer
            )

        elif choice == "3":
            show_registrations(participant)

        elif choice == "4":
            cancel_registration(participant)

        elif choice == "5":
            show_ticket(participant)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def organizer_menu(organizer):
    while True:
        print("\nOrganizer Menu")
        print("1. Create event")
        print("2. View events")
        print("3. Delete event")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            create_event(organizer)

        elif choice == "2":
            organizer.show_events()

        elif choice == "3":
            if not organizer.events:
                print("No events available.")
                continue

            show_events(organizer)

            choice = input("\nSelect event: ")

            if not choice.isdigit():
                print("Enter a valid number.")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(organizer.events):
                print("Invalid event.")
                continue

            event = organizer.events[choice - 1]

            if organizer.delete_event(event):
                print("Event deleted.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def main():
    organizer = Organizer(
        "Shaswat",
        "organizer@gmail.com"
    )

    participant = Participant(
        "Ram",
        "ram@gmail.com"
    )

    while True:
        print("\n============================")
        print("EVENT MANAGEMENT SYSTEM")
        print("============================")
        print("1. Organizer")
        print("2. Participant")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            organizer_menu(organizer)

        elif choice == "2":
            participant_menu(
                participant,
                organizer
            )

        elif choice == "3":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()