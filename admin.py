import os
score_file= "data/scores.txt"

def admin_portal():
    uname = input("enter the username: ")
    passw = input("enter the password: ")

    if uname == "lnct" and passw == "lnct009":
        print("\n Admin Portal - ")
        while True:
            print("\n   1. View All Scores of the Quiz")
            print("   2. Search Scores by Username")
            print("   3. Logout Admin")
            ch = input("Enter choice: \n ")

            if ch == '1':
                if os.path.exists(score_file):
                    with open(score_file, "r") as f:
                        print("Quiz All Scores: \n")
                        for line in f:
                            print(line.strip())
                else:
                    print("No scores yet.")
            
            elif ch == '2':
                user = input("Enter username to search: \n ")
                if os.path.exists(score_file):
                    found = False
                    with open(score_file, "r") as f:
                        for line in f:
                            if user in line:
                                print(line.strip())
                                found = True
                    if not found:
                        print("No entries found")
                else:
                    print(" file not found.")
            
            elif ch == '3':
                print("Admin logged out successfully.")
                break
            
            else:
                print("Invalid choice.")
    else:
        print("Admin details  are invalid.")
