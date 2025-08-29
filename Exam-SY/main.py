import login
import result
import Question
choice = "yes"
while choice == "yes":
    print("\n===<WELCOME TO ONLINE EXAM PORTAL>==\n\n(prepare yourself for your dream college)")
    print("note: login for exam and get instant results\n")
    option = input("1)login\n2)Result\nEnter your choice: ")
    if option == "1":
        print("\n--<Login>--")
        user_data = login.log()
        print("login successfully!!\nYOUR EXAM STARTS NOW!!")
        # QUESTIONS:
        Question.q()
        # RESULT:
        result_check = input("\nDo you want to check your result: ")
        if result_check == "yes" or result_check == "YES":
                result.check_result(user_data)  

    elif option == "2":
        print("Error: Please log in first (select option 1).")
    else:
        print("Invalid option!")
    choice = input('\nDo you want to do it again?(yes/no)').lower()
    if choice == "no":
         break