from user import User

def main():
    while True:
        print("Welcome to Siri, your password locker/n")
        print("If you are new to siri, press '1' : If you are already a Siri member, press '2' : to exit siri, press '0'")
        short_code = input().str()

    if short_code == '1':
        print("Create Username")
        created_user_name = input()

        print("Create a Password")
        created_user_password = input()

        print("Confirm Password")
        confirm_password = input()