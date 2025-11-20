import students
from quiz import quiz_portal
from admin import admin_portal
import sys

def main_menu():
    while True:
        print("            LNCT STUDENT QUIZ            ")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Attempt Quiz")
        print("6. Logout")
        print("7. Admin Login")
        print("8. Quit")
        ch = input("enter the choice (1-8): ")

        if ch == '1':
            students.register()
        elif ch == '2':
            students.login()
        elif ch== '3':
            students.show_profile()
        elif ch == '4':
            students.update_profile()
        elif ch == '5':
            if students.logged:
                quiz_portal()
            else:
                print("You have to login first.\n")
        elif ch == '6':
            students.logout()

        elif ch == '7':
            admin_portal()
        elif ch == '8':
            print("    Thankyou    ")
            sys.exit()
        else:
            print(" Invalid choice \n")

if __name__ == "__main__":
    main_menu()
