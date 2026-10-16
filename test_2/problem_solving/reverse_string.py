text = "ydeerg"
# print(len(text))
c = ""
for n in range(len(text)-1,-1,-1):
    # print(text[n])
    c += "*"
    # print(c)

c = ""
for n in range(1, 10):
    c += str(n) + " "
    # print(c)


c = ""
text = "god"
for n in range(len(text)-1,-1,-1):
    c += text[n]
    print(c)

