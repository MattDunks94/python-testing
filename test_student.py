# Built in testing tool
import unittest
# Importing the class 'Student' from student.py
from student import Student

from datetime import timedelta


# Tests for our 'Student' class
class TestStudent(unittest.TestCase):

    # @classmethod is a method that is bound to a class rather than its object. 
    # Is always attached to the class when passed 'cls'.
    # This runs before anything else.
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # This runs at the end of testing
    @classmethod    
    def tearDownClass(cls):
        print('tearDownClass')

    # setUp runs before each test method
    """
    Creating the instance variable 'student'
    This reduces code repetition, DRY(Don't Repeat Youself)
    """
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    # setUp runs after each test method
    def tearDown(self):
        print('tearDown')

    # Testing to see if full_name is equal to 'John Doe'
    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    
    # Testing to see if our student is on the naughty_list
    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self):
        print('test_apply_extension')
        # Defining variable to 'student.end_date' from our class Student
        # from student.py
        old_end_date = self.student.end_date
        self.assertEqual(self.student.end_date, old_end_date + timedelta(
            days=5))


if __name__ == '__main__':
    unittest.main()