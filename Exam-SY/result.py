import Question

def check_result(user_data):
    print("\nWelcome TO STUDENT RESULT PORTAL:")
    r_n = input("Enter your name: ").lower()
    r_r = input("Enter your roll number: ")
    
    if r_n == user_data["name"] and r_r == user_data["roll number"]:
        # Save result to file
        with open("results.txt", "a") as f:
            f.write(f"Name: {r_n}, Roll: {r_r}, Score: {Question.get_score()}/{len(Question.questions)}\n")
        
        print(f"\nYour final score is: {Question.get_score()} out of {len(Question.questions)}")
    else:
        print("Error: Invalid credentials!")