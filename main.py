from user import User

def main():
    while True:
        print("Welcome to Siri, your password locker \n")
        print("If you are new to siri, press '1' : If you are already a Siri member, press '2' : to exit siri, press '0'")
        short_code = input().str()

    if short_code == '1':
        print("Create Username")
        created_user_name = input()

        print("Create a Password")
        created_user_password = input()

        print("Confirm Password")
        confirm_password = input()

        while confirm_password != created_new_password:
            print("Passwords DO NOT match")
            print("Recreate your Password")
            created_user_password = input()
            print("Confirm Password")
            confirm_password = input()
        
        else:
            print(f"Hoooray! {created_user_name}. You have account has been successfully created! \n")
            print("Proceed to login to your account")
            print("Username")
            entered_username = input()
            print("Password")
            entered_password = input()


            while entered_username != created_user_name or entered_password != created_user_password:
                print("Invalid login credentials\n")
                print("Username")
                entered_username = input()
                print("Password")
                entered_password = input()
            
            else:
                print(f"Welcome {entered_username} to your Siri account\n")

    