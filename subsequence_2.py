s = "abc"
t = "ahbgdc"

def subsequence(s,t):

    i = 0
    for character in t:
     if character == s[i]:
         i += 1
     if i == len(s):
      return True
    return False
print(subsequence("abc", "ahbgdc"))
print(subsequence("axc", "abgdc"))
