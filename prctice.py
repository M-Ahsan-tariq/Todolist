# def s_l(list1, list2):
#     list3 = list1 + list2
#     list3.sort()
#     return list3

# list0 = [78,64,22,43]
# list4=[10,28,69,20]

# result = s_l(list0, list4)
# print(result)

# def s_l(list1,list2):
#     list3 = list1 + list2
#     list3.sort()
#     return list3
# list0 = [78,64,22,43]
# list4=[10,28,69,80]
# result = s_l(list0,list4)
# print(result)
# ------------------------------------------
print("\n:=========<( TO DO LIST )>==========:")

# Variable to store tasks (list)
tasks = []

# Function to add tasks
def add_tasks():
    how_many = int(input("How many tasks do you want to add? "))
    for i in range(how_many):        # loop
        task = input("Enter task: ")
        tasks.append(task)

# Function to show tasks
def show_tasks():
    if len(tasks) == 0:              # conditional
        print("No tasks added yet.")
    else:
        print("\nYour tasks:")
        count = 1
        for task in tasks:           # loop
            print(str(count) + ". " + task)
            count = count + 1

# Function to mark task as done
def mark_done():
    if len(tasks) == 0:
        print("No tasks to mark as done.")
    else:
        show_tasks()
        print("\nMark the task as done")
        for i in tasks:
            t = "tasks:"   
            f = input(f"{t}{i}: ")
            if f == "done":
                print("MARKED AS DONE!")
            elif f == "not done":
                print("PENDING!. MARK WHEN DONE")
            else:
                print("Invalid task number.")
# Main loop to keep showing menu
while True:
    print("\n1. Add Tasks")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = input("Select your choice: ")    # variable + input
    
    if choice == "1":
        add_tasks()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Goodbye!...")
        break                                 # loop ends here
    else:
        print("Please enter a valid choice (1–4).")



        



