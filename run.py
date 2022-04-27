#!/usr/bin/env python3.8
from user import User


#create account function
def create_user(user_name, password, phone_number, email):
      '''
      Function to create a new user
      '''
      new_user = User (user_name, password, phone_number, email)
      return new_user


