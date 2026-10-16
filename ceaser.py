def ceaserF(text, shift):

    result = ""

    for char in text:
        if char.isalpha():

            start = ord("A") if char.isupper() else ord("a")
            result += chr(((ord(char) - start) + shift)%26 + start)
        else:
            result += char
    return result

def ceaserB(text, shift):

    result = ""

    for char in text:
        if char.isalpha():

            start = ord("A") if char.isupper() else ord("a")

            result += chr(((ord(char) - start) - shift)%26 + start)
        else:
            result += char
    return result

def zipString(text):

    result = ""
    count = 1
    # for i, char in enumerate(text):

    #     if i+1 <len(text) and char == text[i+1]:
    #         count +=1
    #     else:
    #         result += f"{char}{count}"
    #         count =1
    for i in range(0, len(text)):
            
    
            if i+1 <len(text) and text[i] == text[i+1]:
                count +=1
            else:
                result += f"{text[i]}{count}"
                count = 1
    return result
print(zipString("A-BAAABBAA                    "))

def twoSum(nums, targ):

    res = [] 
    seen = {}
    for i in range(0, len(nums)):
        needed = targ - nums[i]

        if needed in seen:
            res.append([seen[needed],i])

        seen[nums[i]] = i

    return res

print(twoSum([1,2,3,4],5))


# print(ceaserF("XYZ", 3))
# print(ceaserB("ABC", 3))