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

