import pyperclip
from user import User, Credential


def create_user(user_name,password):
	'''
	Function to create a new user account
	'''
	new_user = User(user_name,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	confirm_user = Credential.check_user(first_name,password)
	return confirm_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	random_pass = Credential.generate_password()
	return random_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)




def main():
    
    #landing page
    while True:
        print("Welcome to Siri, your password locker \n")
        print("If you are new to Siri, press 'a' : If you are already a Siri member, press 'b' : to exit Siri, press 'x' \nb")
        short_code = input().lower()
        print('\n')

        if short_code == 'a':
            print("Create Username")
            created_user_name = input()

            print("Create a Password")
            created_user_password = input()

            print("Confirm Password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Passwords DO NOT match \n")
                print("Recreate your Password")
                created_user_password = input()
                print("Confirm Password")
                confirm_password = input()
            
            else:
                print(f"Hoooray! {created_user_name}! You're account has been successfully created:) \n")
                print("Proceed to login to your account \n")
                print("Username")
                entered_username = input()
                print("Password")
                entered_password = input()


                while entered_username != created_user_name or entered_password != created_user_password:
                    print("Invalid login credentials. Try again.\n")
                    print("Username")
                    entered_username = input()
                    print("Password")
                    entered_password = input()
                
                else:
                    print(f"Welcome {entered_username} to your Siri account\n")

        elif short_code == 'b':
            print("Welcome back Siri Member")
            print("Enter your username")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print("\n")

            while default_user_name != created_user_name or default_user_password != created_user_password:
                print("Invalid login credentials. Try again. \n")

                print("Enter your username")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
                print("\n")
            
            else:
                print("Login Successful \n\n")

        elif short_code == 'x':
            break
        else:
            print("Enter valid code to continue")

if __name__ == '__main__':
    main()
