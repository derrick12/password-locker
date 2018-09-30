#!/usr/bin/env python3.6
from locker import User
from locker import Credentials

from os import urandom
from random import choice
import math
import sys

# Defining User and Credentials functions

def create_user(fname,lname,phone,email):
    '''
    Function to create a new user with an account 
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

def create_account(account_name,account_password):
    '''
    Function to create a new account 
    '''
    new_account = Credentials(account_name,account_password)
    return new_account



def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()



def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()



def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)


def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)



def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()


# Password Generator

def user_input() :
    """
    Asks user what length of password to create.
    """

    userLength=0

    try : 
        userLength = int(input('How many characters would you like in your password? '))

    except :
        print('\nSorry there was an error')
        print('Please try again...')

        try : 
            userLength = int(input('\nHow many characters would you like in your password? '))
        except : 

            print('Sorry, there was an error')
            input('Press any key to exit')
            sys.exit()
                       
    return(userLength)


def generate_password() : 
    """
    Generate random characters to form the password.
    """

    charSets = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
        ]

    length = user_input()
    pwd = []
    charset = choice(charSets)

    while len(pwd) < length :

        pwd.append(choice(charset))
        charset = choice(list(set(charSets) - set([charset])))

    return outputPassword("".join(pwd))
        

def outputPassword(passwordString) :
    """
    Output password to user.
    """
    print('This is your generated password: {0}\n'.format(passwordString))


# Main Function
def main():
    print("Hello! Welcome to The Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user , ca - create a new account, dc - display users, da - display accounts, fc - find a user, rm - remove a user, For choices use: y - yes, n - no, ex - exit the password locker.")

        short_code = input().lower()

        if short_code == 'cc':
            
            
            print("New User")
            print("-"*10)
            print('\n')

            print("First name ....")
            f_name = input()

            print("Last name....")
            l_name = input()

            print("Phone number....")
            p_number = input()

            print("Email address....")
            e_address = input()

            save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
            print('\n')

            print("New Account")
            print("-"*13)
            print('\n')

            print("Account name ....")
            account_name = input()

            print("Generate a password for your account....")
            generate_password() # generates the password

            print("Input your new account password...")
            account_password = input()
    
            save_accounts(create_account(account_name, account_password)) # create and save new account.
            print('\n')
            print(f"New {account_name} account created by {f_name} {l_name} ")
            print('\n')


        elif short_code == 'ca':

            print("New Account")
            print("-"*13)
            print('\n')

            print("Account name ....")
            account_name = input()

            print("Generate a password for your account....")
            generate_password() # generates the password

            print("Input your new account password...")
            account_password = input()
    
            save_accounts(create_account(account_name, account_password)) # create and save new account.
            print('\n')
            print(f"New {account_name} account created by {f_name} {l_name} ")
            print('\n')
             
        
        elif short_code == 'dc':
            
            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} ......{user.phone_number}")

                print('\n')
            
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'da':
            
            if display_accounts():
                print("Here is a list of all your accounts")
                print('\n')

                for account in display_accounts():
                    print(f"{account.account_name}")

                print('\n')
            
            else:
                print('\n')
                print("You dont seem to have any accounts saved yet")
                print('\n')

        
        elif short_code == 'fc':
            
            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_users(search_number):
                search_user = find_user(search_number)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-'*20)

                print(f"Phone number .....{search_user.phone_number}")
                print(f"Email address.....{search_user.email}")
            else:
                print("That user does not exist")

        
        elif short_code == 'rm':
            
            
            print("Enter the number you want to delete")

            delete_number = input()
            if check_existing_users(delete_number):

                search_user = find_user(delete_number)
                print(f"Do you want to delete {search_user.first_name} {search_user.last_name} ?")
                print('\n')
                print(f"If yes input y. If no input n")

                choice = input().lower()
                if choice == 'y':
                    del_user(search_user)
                    del_account(account)
                    print(f"User has been deleted")

                elif choice == 'n':
                    print(f"{search_user.first_name} {search_user.last_name} is safe and soouuund.")

                else:
                    print("I really didn't get that. Please use the short codes")

            else:
                print("That user does not exist") 
                
        
        elif short_code == "ex":
            print("Thank you for using Password Locker. Bye!")
            break

        
        else:
            print("I really didn't get that. Please use the short codes")
            

if __name__ == '__main__':
    main()

