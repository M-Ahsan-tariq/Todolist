import random

# Simple file reading without strip() or next()
def load_questions():
    questions = []
    try:
        with open("questions.txt", "r") as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                if lines[i].startswith("Q:"):
                    question = lines[i][2:-1]  # Remove "Q:" and newline
                    options = [
                        lines[i+1][:-1],  # Remove newline
                        lines[i+2][:-1],
                        lines[i+3][:-1],
                        lines[i+4][:-1]
                    ]
                    answer = lines[i+5][0]  # Just get the first character (A/B/C/D)
                    questions.append({
                        "question": question,
                        "options": options,
                        "answer": answer
                    })
                    i += 6
                else:
                    i += 1
    except FileNotFoundError:
        print("Error: questions.txt not found")
        return []
    return questions

questions = load_questions()
score = 0

def q():
    global score
    random.shuffle(questions)
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("->Correct!")
            score += 1
        else:
            print(f"->Incorrect. The correct answer was {q['answer']}.")
    
    print("YOUR EXAM IS COMPLETED!!!")

def get_score():
    return score