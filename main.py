from user import User

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
