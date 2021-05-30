import pyperclip

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

        credential_list = []
        user_credential_list = []

        @classmethod
        def confirm_user (cls, user_name, password):
            '''
            checks that the name and password match the one on the list
            '''
        