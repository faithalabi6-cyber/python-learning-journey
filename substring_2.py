s = "abcabcbb"
longest = 0
current = ""

for i in range(0, len(s)):
    current_charcter = s[i]


    while current_charcter in current:

        current = current[1:]

    current = current + current_charcter

    if len(current) > longest:

        longest = len(current)
print(longest)



