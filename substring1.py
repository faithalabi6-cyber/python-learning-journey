text = "banana"
substring = "ana"
count = 0
for i in range(4):
    piece = text[i: i+3]
    if piece == substring:
        count+= 1
print(count)






text = input("Enter text: ")
substring = input("Enter substring: ")


count = 0
for i in range(0,(len(text))):
    word = text[i: i + 2]
    if word == substring:
        count += 1
print(count)
        