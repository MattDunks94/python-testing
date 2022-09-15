from datetime import date, timedelta


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