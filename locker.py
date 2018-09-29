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