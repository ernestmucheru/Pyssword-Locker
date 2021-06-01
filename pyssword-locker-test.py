import unittest
from unittest.case import TestCase
from user import User,Credential

class TestUSer(unittest.TestCase):
    '''
    Defines test cases for the user class behaviours
     Agrs: 
     unittest.TestCase: helps in creating test cases
    '''

    def setUp(self):
        '''
        function to create a user account before each Test
        '''
        self.new_user = User('Ernest','254','254')

    def test_init(self):
        '''
        Test to if check the initialization/creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.user_name,'Ernest')
        self.assertEqual(self.new_user.password,'254')
        self.assertEqual(self.new_user.password,'254')
    
    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)