# EventManagementSystem
Python OOP based Event Management and Registration System

# Event Management & Registration System

## Introduction

The Event Management & Registration System is a Python-based project that allows an organizer to create and manage events while participants can view events, register for them, cancel registrations, and view their tickets.

The main purpose of this project is to demonstrate the practical use of Object-Oriented Programming concepts in Python.

## Features

* Organizer can create events.
* Organizer can view created events.
* Organizer can delete events.
* Participant can view available events.
* Participant can register for an event.
* Participant can cancel a registration.
* Participant can view registration details.
* Participant can view their ticket.
* Event capacity is checked before registration.
* Duplicate registration is prevented.
* Basic input validation is included.

## OOP Concepts Used

The project contains six classes:

1. `User`
2. `Participant`
3. `Organizer`
4. `Event`
5. `Registration`
6. `Ticket`

### Classes and Objects

The system uses classes to represent users, events, registrations, and tickets. Objects are created from these classes during program execution.

### Constructors

The `__init__()` method is used to initialize objects with their required information.

### Instance Attributes and Methods

Each object stores its own information such as:

* User name
* Email
* Event name
* Event date
* Event capacity
* Registration status

Methods are used to perform actions such as registering, cancelling, creating events, and displaying information.

### Class Attributes

Class attributes are used for values shared by all objects of a class.

Examples:

```python
User.total_users
Event.total_events
Registration.total_registrations
Ticket.next_number
```

### Class Method

The `Event.create_event()` method is used as an alternative way to create an event object.

### Static Method

The `Event.valid_date()` method checks whether an entered date follows the required format.

### Encapsulation

The user's email is stored using a private attribute:

```python
self.__email
```

A property is used to access it.

### Inheritance

`Participant` and `Organizer` inherit from the `User` class.

```text
User
├── Participant
└── Organizer
```

This allows both classes to reuse common user information and behavior.

### Abstraction

`User` is an abstract class. It defines the `get_role()` method that its child classes must implement.

### Polymorphism and Method Overriding

Both `Participant` and `Organizer` provide their own implementation of:

```python
get_role()
```

The same method name therefore behaves differently depending on the object.

### Composition

A `Registration` creates and contains a `Ticket`. A ticket belongs to its registration.

### Aggregation

An `Organizer` maintains a collection of event objects. The events can exist independently of the organizer.

### Association

A `Registration` connects a `Participant` with an `Event`.

## Project Structure

```text
EventManagementSystem/
│
├── main.py
├── user.py
├── event.py
├── registration.py
└── ticket.py
```

### `user.py`

Contains:

* `User`
* `Participant`
* `Organizer`

### `event.py`

Contains:

* `Event`

### `registration.py`

Contains:

* `Registration`

### `ticket.py`

Contains:

* `Ticket`

### `main.py`

Contains the menus and handles interaction with the user.

## Requirements

* Python 3.x

No external Python libraries are required.

## How to Run

1. Create a folder named `EventManagementSystem`.
2. Create the five Python files inside the folder.
3. Copy the corresponding code into each file.
4. Open the project folder in VS Code or another Python editor.
5. Run:

```bash
python main.py
```

## Example Workflow

### Organizer

```text
1. Organizer
   ↓
Create Event
   ↓
Enter event details
   ↓
Event created
```

### Participant

```text
1. Participant
   ↓
View Events
   ↓
Select Event
   ↓
Register
   ↓
Registration Created
   ↓
Ticket Generated
```

## Limitations

This version stores data only while the program is running.

It does not use:

* File handling
* Database
* Login system
* Online payment
* Web interface

These features can be added in a larger version of the project.

## Conclusion

The Event Management & Registration System demonstrates how Object-Oriented Programming can be used to model a real-world system. Each class has a specific responsibility, and the classes interact with one another to manage events, participants, registrations, and tickets.
