values = [14, 7, 22, 9, 7, 31]
#(input("Enter values: ")).split(",")

target = int(input("Enter target: "))
found = False   # i dont know if this is correct but i think so because i am looking for a number .i have a target

for i, num in enumerate (values):  # to track the counter index and also the values

    #followed by an if statement that checks if values is equal to target
    if target == num:

        print(f"found at the index of{i}")

        found = True
        break

    if not found:
    #else:
        print("Target not found")
