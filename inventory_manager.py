import json
inventory = []
sales = []

def add_perfume():
    name = input("Enter perfume name: ")
    brand = input("Enter brand's name: ")
    while True:
        try:
            price = int(input("Enter amount: "))
            if price >0 :
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number.")
    while True:

        try:
            size = int(input("Enter your preferred size: "))
            if size > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Enter a valid number.")
    while True:
        try:
            stock = int(input("Enter many is available in stock: "))
            if stock >= 0:
                break
            else:
                print("Please enter 0 a positive number")
        except ValueError:
            print("Please enter a valid number")
           
    perfume = {
    "name"  : name,
    "brand" : brand,
    "price" : price,
    "size"  :  size,
    "stock" : stock
    }
    inventory.append(perfume)
    save_inventory()
    print("perfume added!")

def view_perfume():
    for perfume in inventory:
         print(
         f"{perfume['name']}  |"
         f"{perfume['brand']} |"
         f"{perfume['price']} | "
         f"{perfume['size']} | "
         f"{perfume['stock']} | "

    )

def search_perfume():
    user_choice = input("Enter perfume of your choice: ")
    found = False
    for perfume in inventory:
        if user_choice.lower() == perfume["name"].lower():
            print(perfume["name"])
            print(perfume["brand"])
            print(perfume["price"])
            print(perfume["size"])
            print(perfume["stock"])
            found = True
    if not found:
        print("perfume not found")


def update_stock():
    user_choice = input("Enter perfume you want to update: ")
    found = False
    for perfume in inventory:
        if user_choice.lower() == perfume["name"].lower():
             while True:
                 try:
                     new_stock = int(input("Enter new stock: "))
                     if new_stock >= 0:
                         break
                     else:
                         print("Please enter 0 or a positive number")
                 except ValueError:
                     print("Please enter a valid number")
             perfume["stock"] = new_stock
             save_inventory()
           
             print("Perfume has been updated.")
             found = True
    if not found:
        print("perfume not found")

def remove_perfume():
    user_choice = input("Enter perfume to remove: ")
    found = False
    for perfume in inventory:
        if user_choice.lower() == perfume["name"].lower():
            inventory.remove(perfume)
            print("perfume has been removed.")
            save_inventory()
            found = True
            break
    if not found:
            print("perfume not found")

def main():
    while True:
     
     print("=========SCENTSBYLARAH INVENTORY=======")
     print("1. Add perfume")
     print("2. View perfume")
     print("3. Search perfume")
     print("4. Update stock")
     print("5. Remove perfume")
     print("6. Record a sale")
     print("7. Total sales")
     print("8. Save inventory")
     print("9. Exit")




     user_choice = input("Enter your choice: ")
    
     if user_choice  =="1":
        add_perfume()
     elif user_choice == "2":
         view_perfume()
     elif user_choice == "3":
         search_perfume()
     elif user_choice == "4":
         update_stock()
     elif user_choice == "5":
         remove_perfume()
     elif user_choice == "6":
         record_sales()
     elif user_choice == "7":
        total_sales()
     elif user_choice == "8":
         save_inventory()
     elif user_choice == "9":
         print("Goodbye!")
         break
     else:
         print("Invalid choice. Please choose fom 1-9")








def record_sales():
    user_choice = input("Enter the perfume that was sold: ")
    found = False
    for perfume in inventory:
        if user_choice == perfume["name"]:
            found = True
            if perfume["stock"] > 0:
                sale_amount = perfume["price"]
                perfume["stock"] = perfume["stock"] -1
                print(f"Sale amount: {sale_amount}")
                sales.append(sale_amount)
                save_inventory()
                print (f" Total sum : {sum(sales)}")
                print("Perfume sale recorded successfully!")
                print(f"Remaining stock: {perfume['stock']}")
            else:
                print("Out of stock!")
    if not found:
        print("Perfume not found!")



def total_sales():
    total = sum(sales)
    print(f"Total sales:{total}")


def save_inventory():
    with open("inventory.json","w") as file:
        data = {
            "inventory": inventory,
            "sales": sales
        }
        json.dump(data, file, indent=4)


def load_inventory():
    global inventory, sales
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            inventory = data["inventory"] 
            sales = data["sales"]

    except FileNotFoundError:
      print("No saved inventory found")
      
      
load_inventory()
main()

     

    




    