import random
import datetime
import os
from students import logged_user

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCORE_FILE = os.path.join(DATA_DIR, "scores.txt")

def load_questions(category):
    filename = os.path.join(DATA_DIR, "questions_" + category.lower() + ".txt")
    if not os.path.exists(filename):
        print("No question file found for", category)
        return []
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    questions = []
    for i in range(0, len(lines), 6):
        if i + 5 < len(lines):
            q = {
                "question": lines[i],
                "a": lines[i+1],
                "b": lines[i+2],
                "c": lines[i+3],
                "d": lines[i+4],
                "answer": lines[i+5].lower().strip()
            }
            questions.append(q)
    return questions   

def attempt_quiz(category):
    questions = load_questions(category)
    if not questions:
        return
    random.shuffle(questions)
    score = 0
    total = min(10, len(questions))
    for i in range(total):
        q = questions[i]
        print("Q" + str(i+1) + ": " + q["question"])
        print("a) " + q["a"])
        print("b) " + q["b"])
        print("c) " + q["c"])
        print("d) " + q["d"])
        ans = input("Your answer (a/b/c/d): ").lower()
        if ans == q["answer"]:
            score += 1
    print("You scored " + str(score) + "/" + str(total))
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        record = logged_user + "|" + category + "|" + str(score) + "/" + str(total) + "|" + str(datetime.datetime.now()) + "\n"
        f.write(record)

def view_result():
    if not os.path.exists(SCORE_FILE):
        print("No quiz attempts found.")
        return
    print("Your Quiz Attempts:")
    with open(SCORE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) != 4:
                continue
            user, cat, marks, dt = parts
            if user == logged_user:
                print(cat + " -> " + marks + " (" + dt + ")")

def quiz_portal():
    while True:
        print("Quiz Portal")
        print("1. Attempt DSA Quiz")
        print("2. Attempt DBMS Quiz")
        print("3. Attempt PYTHON Quiz")
        print("4. View My Scores")
        print("5. Back to Main Menu")
        ch = input("Choose (1-5): ")

        if ch == '1':
            attempt_quiz("dsa")
        elif ch == '2':
            attempt_quiz("dbms")
        elif ch == '3':
            attempt_quiz("python")
        elif ch == '4':
            view_result()
        elif ch == '5':
            break
        else:
            print("Invalid choice.")
