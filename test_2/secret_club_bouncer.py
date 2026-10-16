banned_names = ["Larah", "Ayo", "Femi", "Precious"]
guest = ["Gbemi", "Ay", "Tee"]
#for i in guest:
accepted_guest = []
while True:
    user_input = input("Enter guest's name: ")
    if user_input == "quit":
        print("Exit, bye!")
        break
    if user_input in banned_names:
        print("Banned from entering")
    else:
        accepted_guest.append(user_input)
        print("You are welcomed to this party!")
        print(accepted_guest)


    


        