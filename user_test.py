from cgi import test
import unittest
from user import User
# import pyperclip


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Jane")
        self.assertEqual(self.new_user.password, "123pass")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email,"jane@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")  # new user
        test_user.save_user()

        found_user = User.find_by_number("0712345678")

        self.assertEqual(found_user.email, test_user.email)


    def test_user_exists(self):
       '''
       test to check if we can return a Boolean  if we cannot find the user.
       '''

       self.new_user.save_user()
       test_user = User("Jane", "123pass", "0712345678", "jane@gmail.com")  # new user
       test_user.save_user()

       user_exists = User.user_exist("0712345678")

       self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)   

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''

        self.new_user.save_user()
        User.copy_email("0712345678")

        self.assertEqual(self.new_user.email,pyperclip.paste())         


if __name__ == '__main__':
    unittest.main()
