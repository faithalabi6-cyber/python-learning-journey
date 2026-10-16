def is_letter(ch) -> bool:  #-> bool later
    #if ch in .lower() "a" - "z"
    return  (ch >= "a" and ch  <= "z") or (ch >= "A" and ch  <= "Z")

        
def is_palindrome(text) -> bool:
    
    left, right = 0, len(text) -1

    while left < right:
        
        if not is_letter(text[left]):
            left +=1
            continue

        if not is_letter(text[right]):
            right -= 1
            continue
        
        if text[left].lower() != text[right].lower():
            return False
        
        left+=1
        right-=1

    return True

def rec_palindrome(text, left, right):

    if left >= right:
        return True
    
    if not is_letter(text[left]):
        return rec_palindrome(text, left+1, right)

    if not is_letter(text[right]):
            return rec_palindrome(text, left, right-1)

    if text[left].lower() != text[right].lower():
        return False

    return rec_palindrome( text, left+1, right-1)
            
    
        

text = "Was it a car or a cat I aw?"

print(rec_palindrome(text, 0, len(text)-1))




