#!/usr/bin/env python3.8
from lib2to3.pgen2.tokenize import generate_tokens
from user import User


#create account function
def create_new_user(user_name, password, phone_number, email):
      '''
      Function to create a new user
      '''
      new_user = User (user_name, password, phone_number, email)
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

#Finding a user through number
def find_user(number):
    '''
    Function that finds a user by number and returns
    '''
    return User.find_by_number(number)

#check if a contact exists
def check_existing_user(number):
    '''
    function that check if a contact exists with that number and return a boolean.
    '''
    return User.user_exist(number)

#displaying all users
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()




def main():
    print("Hello! Welcome to Password Manager. Kindly enter your name")
    user_name   = input()
    print(f"Hello {user_name}!")
    print('\n')

    while True:
        print("use these short code : ca -create new account, da-display accounts, fa -find accounts, ex -exit the account list")
        short_code = input(). lower()
        if short_code == 'ca':
            print("New Account")
            print("-"*10)

            print("User Name....")
            user_name = input()

            print("phone number...")
            p_number = input()

            print("Email address...")
            e_address = input()

            print("IP - To input own password:\n GP - To generate random Password")
            password_Choice = input ().lower().strip()

            if password_Choice == 'ip':
                password = input ("Enter Password\n")
                break

            elif password_Choice == 'gp':
                password = generate_password()
                break

            else:
                print("Wrong password, please try againg")


            

