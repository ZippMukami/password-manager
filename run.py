#!/usr/bin/env python3.8
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
def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

#Finding a user
def find_user(number):
    '''
    Function that finds a user by number and returns the contact
    '''
    return User.find_by_number(number)

#check if a contact exists
def check_existing_user(number):
    '''
    function that check if a contact exists with that number and return a boolean.
    '''
    return User.user_exist(number)
