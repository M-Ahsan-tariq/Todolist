print("\n:=========<(TO DO LIST)>==========:")
tasks = []
while True:
 to_do = str(input('''\n1. Add Tasks:\n2. Show Tasks\n3. Mark  Task as done\n4. Exit\nselect the choice: '''))
 if (to_do == "1"):
   choice = int(input("How many tasks you want to add? "))
   for i in range(choice):
    task = str(input("Enter the tasks: "))
    tasks.append(task)

#Show the tasks
 elif(to_do == "2"):
  if len(tasks)>0:
   print("\nYour tasks are:")
   count = 1
   for i in tasks:
    print(str(count)+".",i)
    count+=1
  else:
   print("no choice")

#Mark as done:
 elif (to_do == "3"):
  print("\nMARK THE TASKS AS DONE:"+"(Enter\"done\"if taskes has done if not Enter\"not done\")")
  for i in tasks:
     f = "tasks:"   
     f = input(f"{f}{i}: ")
     if (f == "done"):
      print("MARKED AS DONE!")
     elif(f == "not done"):
      print("PENDING! MARK WHEN DONE!")
      
     else:
      print("Invalid text! please read the instruction carefully")
      
   

     
    