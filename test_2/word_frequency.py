word = input("Enter word: ")

ch = ""
def count_words(words:list[str])-> dict[str, int]:         #what is the work and use of this
    frequent = {}

    for word in words:
        clean_word = ""
        for ch in word:
            if ch not in (
            ".", ",", "!"," ", "-", "_" "?"
              ):
                clean_word+= ch.lower()

        else:
            if clean_word:
                frequent(clean_word) = frequent.get(clean_word)
                return frequent


def most_frequent(frequent: dict[str, int]) ->str:
    top_word = ""
    
    








        #return "Not "

    
       # count += 1
       #for 
