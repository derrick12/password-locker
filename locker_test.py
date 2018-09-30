import unittest # Importing the unittest module
from locker import User # Importing the user class
from locker import Credentials # Importing the credentials

class TestUser(unittest.TestCase,User,Credentials):
    
    '''
    This is test class that defines test cases for the user and credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''
    def setUp(self):
        '''
        Set Up method to run before each test cases.
        '''
        self.new_user = User("Derrick","Kariuki","0718016066","derrickwaweru@gmail.com") # creates user object
        self.new_account = Credentials("Instagram","dero1234") # creates credentials object

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run
        '''
        User.user_list = []
        Credentials.account_list = []


    def test_init(self):
        '''
        test init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Derrick")
        self.assertEqual(self.new_user.last_name,"Kariuki")
        self.assertEqual(self.new_user.phone_number,"0718016066")
        self.assertEqual(self.new_user.email,"derrickwaweru@gmail.com")

        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.account_password,"dero1234")





    def test_save_user(self):
        '''
        test_save_user test case tests whether the user object is saved in the user list
        '''

        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_account(self):
        '''
        test_save_account test case tests whether the account object is saved in the account list
        '''

        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Credentials.account_list),1)





    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list 
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com") # the new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple account objects to our account_list 
        '''

        self.new_account.save_account()
        test_account = Credentials("Test","account12") # the new account
        test_account.save_account()
        self.assertEqual(len(Credentials.account_list),2)





    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list 
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove an account from our account list 
        '''

        self.new_account.save_account()
        test_account = Credentials("Test","account12") # new account
        test_account.save_account()

        self.new_account.delete_account()# Deleting a account object
        self.assertEqual(len(Credentials.account_list),1)




    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_number("0711223344")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user") #new user
        test_user.save_user()

        user_exists = User.user_exist("0711223344")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        test to check that a list of all users saved is returned.
        '''
        self.assertEqual(User.display_users(), User.user_list)


if __name__ == '__main__':
    unittest.main()