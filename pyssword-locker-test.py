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

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentila class behaviours
    Args:
        unittest.TestCase: helps in creating cases
    '''
    def test_check_user(self):
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User('Ernest','254')
        self.new_user.save_user()
        user2 = User('Mwangi','245')
        user2.save_user()
        
        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
		return current_user
        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
       
            self.new_credential = Credential('Ernest','Facebook','estmuch','dpefe100')

    def test__init__(self):
        '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.user_name,'Ernest')
        self.assertEqual(self.new_credential.site_name,'Facebook')
        self.assertEqual(self.new_credential.account_name,'estmuch')
        self.assertEqual(self.new_credential.password,'dpefe100')

	def test_save_credentials(self):
        
            self.new_credential.save_credentials()
            twitter = Credential('Ernest','Twitter','nesto','pswd100')
            twitter.save_credentials()
            self.assertEqual(len(Credential.credentials_list),2)
    
    def tearDown(self):
        Credential.credentials_list = []
        User.users_list = []
        
    def test_display_credentials(self):
        '''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
        self.new_credential.save_credentials()
        twitter = Credential('Lee','Twitter','stan','pswd100')
        twitter.save_credentials()
        gmail = Credential('Tim','Gmail','pssbo','pswd200')
        gmail.save_credentials()
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
        
            self.new_credential.save_credentials()
            twitter = Credential('Doe','Twitter','Djoe','pswd100')
            twitter.save_credentials()
            credential_exists = Credential.find_by_site_name('Twitter')
            self.assertEqual(credential_exists,twitter)

	

if __name__ == '__main__':
    unittest.main()