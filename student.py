from datetime import date, timedelta
import requests


class Student:
    """ A student class as base for method testing """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # Creates Students full name
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    # Creates Students email
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    # alert_santa method, set to True
    def alert_santa(self):
        self.naughty_list = True

    # This extends students end date
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        # Gathering student's course schedule through a mock database
        # Collect data using the .get method, assigning it to our response var
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        # If statement, checking if data has been collected
        if response.ok:
            return response.text
        # Otherwise, returns error message
        else:
            return "Something went wrong!"

    def student_start_date(self):
        return self._start_date