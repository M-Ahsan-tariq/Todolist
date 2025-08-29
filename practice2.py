import threading
import time
import datetime
import random


h = 0
m = 0
s = 5
total_seconds = h * 3600 + m * 60 + s

def countdown():
    global total_seconds
    while total_seconds > 0:
        time.sleep(1)
        total_seconds -= 1
    print("\nTime is up!")

timer_thread = threading.Thread(target=countdown)
timer_thread.daemon = True
timer_thread.start()

questions = [
    {
        "question": "What is the capital of Saudi Arabia?",
        "options": ["A. Makkah", "B. Madina", "C. Riadh", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A. Python", "B. C++", "C. JavaScript", "D. Java"],
        "answer": "C"
    },
    {
        "question": "What is 5 x 6?",
        "options": ["A. 30", "B. 11", "C. 56", "D. 20"],
        "answer": "A"
    },
    {
        "question": "Who is not in our group?",
        "options": ["A. Ahsan", "B. Shehzil", "C. Ahmed", "D. Muhammad"],
        "answer": "C"
    }
]

random.shuffle(questions)
score = 0

for q in questions:
    if total_seconds <= 0:
        break
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if total_seconds <= 0:
        break
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {q['answer']}.")

print(f"\nYour final score is: {score} out of {len(questions)}")