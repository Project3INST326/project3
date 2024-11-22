# project 3 program code
# Doing 1 and 2 
class Person:
    """ Represents a generic person with basic details. """
    def __init__(self, name, phone, email):
        """
        Initialize a person with their basic details.

        :param name: Name of the person
        :param phone: Phone number
        :param email: Email address
        """
        self.name = name
        self.phone = phone
        self.email = email

    def update_contact(self, phone=None, email=None):
        """
        Update the contact details of the person.

        :param phone: New phone number (optional)
        :param email: New email address (optional)
        """
        if phone:
            self.phone = phone
            print(f"Phone updated to: {self.phone}")
        if email:
            self.email = email
            print(f"Email updated to: {self.email}")
            
class Caregiver(Person):
    """
    Represents a caregiver with pay rate, hours, and availability schedule
    """

    def __init__(self, name, phone, email, pay_rate, availability=None):
        """
        Initialize a caregiver with their details and availability.

        :param name: Name of the caregiver
        :param phone: Phone number
        :param email: Email address
        :param pay_rate: Hourly pay rate for the caregiver
        :param availability: Dictionary of availability for each day and shift
        """
        super().__init__(name, phone, email)
        self.pay_rate = pay_rate
        self.hours = 0  # Total hours worked
        # Default availability if none provided
        self.availability = availability or {
            "Monday": {"AM": "available", "PM": "available"},
            "Tuesday": {"AM": "available", "PM": "available"},
            "Wednesday": {"AM": "available", "PM": "available"},
            "Thursday": {"AM": "available", "PM": "available"},
            "Friday": {"AM": "available", "PM": "available"},
            "Saturday": {"AM": "available", "PM": "available"},
            "Sunday": {"AM": "available", "PM": "available"},
        }

    def update_availability(self, day, shift, status):
        """
        Update the caregiver's availability for a specific day and shift.

        :param day: Day of the week (e.g., "Monday")
        :param shift: Shift type ("AM" or "PM")
        :param status: New status ("preferred", "available", "unavailable")
        """
        if day in self.availability and shift in self.availability[day]:
            self.availability[day][shift] = status
            print(f"Availability updated: {day} {shift} set to {status}.")
        else:
            print(f"Invalid day or shift. No changes made.")

    def display_details(self):
        """
        Display the caregiver's details and availability schedule.
        """
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Pay Rate: ${self.pay_rate}/hour")
        print(f"Hours Worked: {self.hours}")
        print("Availability:")
        for day, shifts in self.availability.items():
            print(f"  {day}: AM: {shifts['AM']}, PM: {shifts['PM']}")

if __name__ == "__main__":
    caregiver1 = Caregiver(
        name="Michael Teka",
        phone="301-312-2470",
        email="michael.teka04@gmail.com",
        pay_rate=20,
        availability={
            "Monday": {"AM": "preferred", "PM": "available"},
            "Tuesday": {"AM": "available", "PM": "preferred"},
            "Wednesday": {"AM": "unavailable", "PM": "available"},
            "Thursday": {"AM": "preferred", "PM": "unavailable"},
            "Friday": {"AM": "available", "PM": "preferred"},
            "Saturday": {"AM": "available", "PM": "available"},
            "Sunday": {"AM": "preferred", "PM": "available"},
        },
    )

    caregiver2 = Caregiver(
        name="Mikias Zenebe",
        phone="301-555-1234",
        email="mikias.zenebe@gmail.com",
        pay_rate=18,
    )


    caregiver1.display_details()
    print("\n")
    caregiver2.display_details()
    caregiver1.update_availability("Monday", "AM", "available")
    caregiver1.update_contact(phone="555-555-5555")
    caregiver1.display_details()