total = 0
running = True
while running:
    print("\n ====== SHOPPING MENU ======")
    print("1. Add Item")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")
    choice = int(input("Enter the your choice: "))
    if choice == 1:
        price = int(input("Enter price: "))
        total = total + price
        print("Item added")
    elif choice == 2:
        print("Current total:", total)
    elif choice == 3:
        print("Your total is:",total)
        print("Thank you for shopping!")
        running = False
    elif choice == 4:
        print("Have a great day!")
        running = False

    else:
        print("Invalid choice")
