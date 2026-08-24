def login_system():
    username ="Omolara01"
    password = "Lara100"
    for attempt in range(5):
        user_input =input("Enter Username: ")
        pass_input =input("Enter Password: ")
        if attempt == 4:
            print("Account Locked")
            break
        if user_input == username and pass_input == password:
           print("Login Successful")
           print("Welcome Omolara01")
           print()
           print('View Profile')
           print('Change Password')
           print('Logout')
        choice = input("Select an option: ")  
        view_profile = "My Dashboard"
        Change_password = " Old password \n New Password"
        Logout = "Exit"
        if choice == "1":
             print(view_profile)
        elif choice == "2":
             print(Change_password)
        elif choice == "3":
         print(Logout)
    else:
          print("Invalid option")
    if user_input != username:
          print("Invalid username")
    elif pass_input != password:
            print("Invalid password")
    if user_input != username and pass_input != password:
             print("Invalid username and password")
        

login_system()