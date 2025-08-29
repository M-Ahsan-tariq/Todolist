import random
while True:
    ch = [1,2,3]
    choices = random.choice(ch)
    dict={1:"Rock",2:"Paper",3:"Siccors"}
    option = input(":==<(Chose one)>==:\n1.Rock\n2.Paper\n3.Siccor\n____________\n")
    compchoice =dict[choices]
    print(">The computer choses",compchoice)
    if option == "1" and compchoice == "Rock":
        print("--The game is draw!--")
    elif option == "2" and compchoice == "Paper":
        print("--The game is draw!--")
    elif option == "3" and compchoice == "Siccors":
        print("--The game is draw!--")
    else:
        if option == "1" and compchoice == "Paper":
            print("--Computer win!!--")
        elif option == "1" and compchoice == "Siccors":
            print("--You win!!--")
        elif option == "2" and compchoice == "Rock":
            print("--You win!!--")
        elif option == "2" and compchoice == "Siccors":
            print("--Computer win!!--")
        elif option == "3" and compchoice == "Rock":
            print("--Computer win!!--")
        elif option == "3" and compchoice == "Paper":
            print("--You win!!--")
        else:
            print("Invalid please chose from the given choices!")
