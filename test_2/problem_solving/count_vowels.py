# text = input("Enter sentence: ").lower()
text = "Remember Red, HOpe is a good thing, and no good thing ever dies." # 20 vowels

vowels = "aeiouAEIOU"
count = 0
# for char in text:
#     if char not in vowels:
#         count += 1

# print(count)

for n in range(len(text)):
    for j in range(len(vowels)):
        if  text[n] != vowels[j]:
            count += 1
            break

print(count)

    