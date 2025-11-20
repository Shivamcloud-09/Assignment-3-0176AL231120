import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.txt")

students = {}
logged_user = ''
logged = False

def load_students():
    global students
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 11:
                username, password, name, email, phone, dob, gender, address, course, branch, year = parts
                students[username] = {
                    "username": username, "password": password,
                    "name": name, "email": email, "phone": phone,
                    "dob": dob, "gender": gender, "address": address,
                    "course": course, "branch": branch, "year": year
                }

def save_students():
    with open(DATA_FILE, "w") as f:
        for s in students.values():
            f.write('|'.join([
                s["username"], s["password"], s["name"], s["email"],
                s["phone"], s["dob"], s["gender"], s["address"],
                s["course"], s["branch"], s["year"]
            ]) + "\n")

load_students()

def register():
    global students
    print("        Student Registration -        ")
    username = input("Enter username (unique): ")
    if username in students:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    name = input("Enter full name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    dob = input("Enter date of birth (dd-mm-yyyy): ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")
    course = input("Enter course: ")
    branch = input("Enter branch: ")
    year = input("Enter year: ")

    students[username] = {
        "username": username, "password": password, "name": name,
        "email": email, "phone": phone, "dob": dob, "gender": gender,
        "address": address, "course": course, "branch": branch, "year": year
    }
    save_students()
    print("Registration successful")

def login():
    global logged_user, logged
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in students and students[username]["password"] == password:
        logged_user = username
        logged = True
        print(f"Welcome {students[username]['name']}!\n")
    else:
        print("Invalid credentials.\n")

def show_profile():
    global logged_user, logged
    if not logged:
        print("Please login first.")
        return
    print("        Student Profile -        ")
    for k, v in students[logged_user].items():
        if k != "password":
            print(f"{k.capitalize()}: {v}")

def update_profile():
    global logged_user, logged
    if not logged:
        print("You Need To Login First.\n")
        return
    print("        Update Profile -        ")
    profile = students[logged_user]
    for field in profile:
        if field not in ["username", "password"]:
            new_value = input(f"Update {field} (current: {profile[field]}) or press Enter to keep: ")
            if new_value.strip() != "":
                profile[field] = new_value
    students[logged_user] = profile
    save_students()
    print("User Profile updated successfully.")

def logout():
    global logged_user, logged
    if logged:
        print(f"{students[logged_user]['name']} logged out successfully.")
        logged_user = ''
        logged = False
    else:
        print("user not logged in.")
