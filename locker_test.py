import unittest # Importing the unittest module
from locker import User # Importing the user class

class TestUser(unittest.TestCase,User):
    
    '''
    This is test class that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''
    def setUp(self):
        '''
        Set Up method to run before each test cases.
        '''
        self.new_user = User("Derrick","Kariuki","0718016066","derrickwaweru@gmail.com") # creates user object

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run
        '''
        User.user_list = []


    def test_init(self):
        '''
        test init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Derrick")
        self.assertEqual(self.new_user.last_name,"Kariuki")
        self.assertEqual(self.new_user.phone_number,"0718016066")
        self.assertEqual(self.new_user.email,"derrickwaweru@gmail.com")


if __name__ == '__main__':
    unittest.main()