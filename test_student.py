# Built in testing tool
import unittest
# Importing the class 'Student' from student.py
from student import Student


# Tests for our 'Student' class
class TestStudent(unittest.TestCase):

    # Testing to see if full_name is equal to 'John Doe'
    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')
    
    # Testing to see if our student is on the naughty_list
    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()