s = "abc"
current = ""
i = 0
subsequences = []

def subsequence(s, i, current):
    
    if i == len(s):
     subsequences.append(current)
subsequence(s, i +1 , current + s[i])