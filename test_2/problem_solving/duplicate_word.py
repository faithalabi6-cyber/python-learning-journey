#text = "greedy algo   j"
#seen = ""

# for n in range(len(text)):
#     if text[n] not in seen:
#         seen += text[n]

# print(seen)


#for n in range(len(text)):
  #  for j in range(len(seen)):
       ## if text[n] == seen[j]:
           # break
    #else:
       # seen += text[n]


# print(seen)


# range(1, 20, 2) looks for 7, if found return "found" else return not found. 




#text = "learning lab   "
#seen = ""
#for n in range(len(text)):
# for j in range (len(seen)):
      #  if text[n] == seen[j]:
            #seen +
         #   break
   # else:
      #  seen += text[n]
#print(seen)





text = "youareagoodgirl"
seen = ""
for n in range(len(text)):
    for j in range(len(seen)):
        if text[n] == seen[j]:
            break
    else:
        seen += text[n]
        print(seen)

   

