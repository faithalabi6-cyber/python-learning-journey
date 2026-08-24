running = True
while running:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
      print("Even number")

    else:
      print("Odd number")

    answer = input("Continue? (yes/no): ")
    if answer == "no":
     running = False
     print("Goodbye.")

