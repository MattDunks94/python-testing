# Built in testing tool
import unittest
# Importing the class 'Student' from student.py
from student import Student


# Tests for our 'Student' class
class TestStudent(unittest.TestCase):

    # @classmethod is a method that is bound to a class rather than its object. 
    # Is always attached to the class when passed 'cls'.
    # This runs before anything else.
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # This runs at the end of testing.
    @classmethod    
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

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


if __name__ == '__main__':
    unittest.main()