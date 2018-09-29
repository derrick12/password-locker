class User:
    """
    Class that generates new instances of users
    """
    user_list = []  # Class variable

    def __init__(self, first_name, last_name, number, email):        
        """
        __init__ method that helps us define properties for our objects.abs

        Args:
        first_name: New user first name.
        last_name : New user last name.
        number: New user phone number.
        email : New user email address.
        
        """

        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


    @classmethod
    def find_by_number(cls,number):
        '''
        This is a method that takes in a number and returns a user that matches that number.
        
        Args:
            number: Phone number to search for 
        Returns:
            User that matches the number. 
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns:
            Boolean: True or Flase depending if the user exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return True
            return False


