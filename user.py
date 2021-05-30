import pyperclip
import string
import random

class User:
    '''
    This is a class that will generate a new instance of the user
    '''
    user_list = []
    
    def __init__(self,user_name,password):
    
        self.user_name = user_name
        self.password = password

    '''
    __init__ method will help us define properties for our user
    Arguments:
        user_name: The user's username.
        password: The user's login pass to the locker.
    '''

    def save_user (self):
        '''
        Saves a new user object to our user_list
        '''
        User.user_list.append(self)

class Credential:
        '''
        Class to create account credentials, generate password and save account Credentials
        '''
        #Class Varibales
        credentials_list = []
        user_credentials_list = []

        @classmethod
        def confirm_user(cls,user_name,password):
                 '''
                 checks that the name and password match the one on the list
                 '''
                 confirm_user = ''
                 for user in User.users_list:
                     if (user.user_name == user_name and user.password == password):
                                current_user = user.user_name
                 return confirm_user 
                
        def __init__(self, user_name,site_name,account_name,password):
                '''
                Method to define the properties for each user object will hold
                '''

                #instance variables
                self.user_name = user_name
                self.site_name = site_name
                self.account_name = account_name
                self.password = password
        def save_credentials(self):
                '''
                Function to save a newly created user instance
                '''
                #global_user_list
                Credential.credentials_list.append(self)
        
        def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
                Function to generate an 8 character password for a credential
                '''
                random_pass=''.join(random.choice(char) for _ in range(size))
                return random_pass
