#!/usr/bin/env python3.8
from email.policy import default
import random
from lib2to3.pgen2.tokenize import generate_tokens
from user import User
# from user_test import pyperclip



# create account function
def create_new_user(user_name, password, phone_number, email):
    '''
    Function to create a new user
    '''
    new_user = User(user_name, password, phone_number, email)
    return new_user

# save account function


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


# delete credential function
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

# Finding a user through number


def find_user(number):
    '''
    Function that finds a user by number and returns
    '''
    return User.find_by_number(number)

# check if a contact exists


def check_existing_user(number):
    '''
    function that check if a contact exists with that number and return a boolean.
    '''
    return User.user_exist(number)

# displaying all users


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()





def main():
    print("hello! Welcome to Password Manager")
    print('\n')
    print("use these short code : creating a new user- nu, da-display accounts, fa -find accounts, ip -input password, gp-generate password, ex -exit the account list")
    short_code = input().lower()
    print('\n')

    if short_code == "nu":
        print("create username")
        created_user_name = input()

        print("create password")
        created_user_password = input()

        print("confirm password")
        confirm_password = input()

        while confirm_password != created_user_password:
            print("invalid! Password did not match!")
            print("enter your password")
            created_user_password = input()
            print("confirm your password")
            confirm_password = input()

        else:
            print(f"congratulations {created_user_name}! account creation successful")
            print('\n')
            print("Enter username")
            print("Username")
            entered_username = input()
            print("Enter password")
            entered_password = input()

        while entered_password != created_user_name or entered_password != created_user_password:
            print("invalid username or password")
            print("username")
            entered_username = input()
            print("Enter password")
            entered_password = input()

        else:
            print(
                f"welcome: {entered_username} to your password manager account")
            print('\n')

    elif short_code == 'lg':
        print("Welcome")
        print("please enter your username")
        default_user_name = input()

        print("Enter your password")
        default_user_password = input()
        print('\n')

        while default_user_name != 'testuser' or default_user_password != '09876':
            print(
                "invalid username or password. Username 'testuser' and password '09876'")
            print("Enter username")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print("\n")

        else:
            print("login was successful")
            print('\n')
            print('\n')

    elif short_code == 'ex':
       
    
        print("Enter valid code to continue")


if __name__ == '__main__':
    main()
