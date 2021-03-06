# password manager

##### Password Manager
### By Zipporah Mukami

## Table of Content

- [password manager](#password)
        - [password manager](#password-manager)
    - [By Zipporah Mukami](#by-zipporah-mukami)
  - [Table of Content](#table-of-content)
  - [Description](#description)
  - [Installation / Setup instruction](#installation--setup-instruction)
      - [The application requires the following installations to operate](#the-application-requires-the-following-installations-to-operate)
      - [Cloning](#cloning)
  - [Site Screenshot](#site-screenshot)
  - [User Stories](#user-stories)
  - [Behaviour Driven Development](#behaviour-driven-development)
    - [Running the Application](#running-the-application)
  - [Technology Used](#technology-used)
  - [Reference](#reference)
  - [Licence](#licence)
  - [Known Bugs](#known-bugs)
  - [Contact Information](#contact-information)
  - [Authors Info](#authors-info)


## Description
<p> Password Manager is an amazing terminal-based python program where a user can store credentials of different applications or services and generate passwords. </p>




## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.8
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/ZippMukami/password-manager/.git```

* cd password-manager

* code . or atom . based on the text editor you have.


## User Stories

1. Given : A user wants to log into her password-manager account
   when : creating an account
   Then : The user must fill in his/her details

2.  Given : A user wants to store other accounts passwords and usernames
    when : having passwords to store
    Then : The user can store other existing paswords in their password manager account

3. Given : A user wants to create a new account
    when : The user needs a random password
    Then : The user is able to generate random password for account

4. Given : A user wants to delete credentials
   when : The user nolonger needs the password to be saved
   Then : The user can delete credentials

5. Given : A user wants to view their various saved passwords
   when : The user wants to access them
   Then : The user can acces their various saved passwords

6. Given : A user wants to come up with their own password
   when : creating a credential account
   Then : The user is able to.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to password manager <br>* ```CA``` ---  Sign Up * ```LI``` ---  Log in, Have An Account |
|input username and password| Select  ```CA```| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
| Enter your password and username you signed up with  |Select ```LI```| Abbreviations menu to help you navigate through the application|
|New credential | Enter ```CC```|Enter Account, username, password<br>choose ```IP``` to enter your password or ```GP``` for the application to generate a password for you |
|Display all credentials | Enter ```VC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find stored credential based on Application name|Enter ```EC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential |Enter ```Del```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|




## Technology Used

*Python3.8



## Reference
* Google

[Go Back to the top](#password-manager)


## Licence

MIT License

Copyright (c) [2021] [Zipporah Mukami]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, but not to sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#password-manager)

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot one

## Contact Information 

If you have any question or contributions, please email me at [zimukami@gmail.com]

## Authors Info

I am self-driven and passionate about Software development and all types of art. I take each day as a learning opportunity and seek to develop new skills .


[Go Back to the top](#password-manager)
