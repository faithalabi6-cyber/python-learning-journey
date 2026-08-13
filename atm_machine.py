def atm_machine():

    balance = 50000
    running = True

    while running:

        print("\n====== ATM MENU ======")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        user_choice = input("Enter a choice: ")

        if user_choice == "1":
            print(f"Your balance is: ${balance}")

        elif user_choice == "2":
            deposit = int(input("Enter deposit amount: "))
            balance += deposit
            print(f"Deposit successful!")
            print(f"Your balance is: ${balance}")

        elif user_choice == "3":
            withdraw = int(input("Enter withdrawal amount: "))

            if withdraw <= balance:
                balance -= withdraw
                print("Withdrawal successful!")
                print(f"Your balance is: ${balance}")
            else:
                print("Insufficient funds!")

        elif user_choice == "4":
            print("Thank you for using our ATM.")
            running = False

        else:
            print("Invalid selection! Choose 1, 2, 3 or 4.")


atm_machine()