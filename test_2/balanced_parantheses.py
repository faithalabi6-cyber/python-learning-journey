text = input("Enter text: ").strip().lower()

count = 0

balanced = True
for char in text:
    for ch in char:

     if ch == "(":

        count += 1
     elif ch == ")":

        count -=1
     if count < 0:
        print("Not balanced")
        break
else:
    if count == 0 :
        print("Balanced")
    elif count > 0:
        print("Not balanced")


