# import pyperclip
import string
from user import User, Credential


def create_user(user_name, password):
    '''
    Function to create a new user account
    '''
    new_user = User(user_name, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    confirm_user = Credential.check_user(first_name, password)
    return confirm_user

def user_exists(user_name):
    return User.user_exists(user_name)

def generate_password():
    '''
    Function to generate a password automatically
    '''
    random_pass = Credential.generate_password()
    return random_pass


def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(user_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)


def display_credentials(user_name):
    '''
    Function to display credentials saved by a user
    '''
    return Credential.display_credentials(user_name)

# @classmethod
def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credential.copy_credential(site_name)

# def copy_password(cls, account):
#         found_credentials = Credentials.find_credentials(account)
#         pyperclip.copy(found_credentials.password)


def main():

    # landing page
    while True:
        print("Welcome to Siri, your password locker \n")
        print("What do you want to do next?")

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
                save_user(create_user(created_user_name, created_user_password))
                print(
                    f"Hoooray! {created_user_name}! You're account has been successfully created:) \n")
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

                # Credential.save_credentials(default_user_name)
                save_user(create_user(entered_username))

                print(f"Welcome {entered_username} to your Siri account\n")

               
            # else:
                # user_exists = user_exists(
                # entered_username, entered_password)
                # print(f"Welcome {entered_username} to your Siri account\n")
                # print("Invalid Credentials")

        elif short_code == 'b':
            print("Welcome back Siri Member")
            print("Enter your username")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print("\n")

            while default_user_name != default_user_name or default_user_password != default_user_password:
                print("Invalid login credentials. Try again. \n")

                print("Enter your username")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
                print("\n")

            else:
                print("Login Successful \n\n")
                
                print("Select an option to Proceed\n\n")
                while True:
                    print("-"*60)
                    print(
                        'Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {default_user_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        site_name = input('Enter the site\'s name- ').strip()
                        account_name = input(
                            'Enter your account\'s name - ').strip()
                while True:
                    print("-"*60)
                    print(
                        'Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                    psw_choice = input('Enter an option: ').lower().strip()
                    print("-"*60)

                    if psw_choice == 'ep':
                        print(" ")
                        password = input('Enter your password: ').strip()
                        break
                    elif psw_choice == 'gp':
                        password = generate_password()
                        break
                    elif psw_choice == 'ex':
                        break
                    else:
                        print('Oops! Wrong option entered. Try again.')
                        save_credential(create_credential(
                            default_user_name, site_name, account_name, password))
                        print(' ')
                        print(
                            f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')

        elif short_code == 'dc':
            print(' ')
            if display_credentials(default_user_name):
                print('Here is a list of all your credentials')
                print(' ')
                for credential in display_credentials(default_user_name):
                    print(
                        f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                    print(' ')
                else:
                    print(' ')
                    print("You don't seem to have any credentials saved yet")
                    print(' ')
        elif short_code == 'copy':
            print(' ')
            chosen_site = input('Enter the site name for the credential password to copy: ')
            copy_credential(chosen_site)
            print('')
        else:
            print('Oops! Wrong option entered. Try again.')
    else:
        print(' ')
        print('Oops! Wrong details entered. Try again or Create an Account.')


# else:
# print("-"*60)
# print(' ')
# print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
    main()
