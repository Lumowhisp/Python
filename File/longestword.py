def longestWord():
    with open("text.txt","r")as f:
        content=f.read()
        word=content.split()
        print(word)
        longest=word[0]
        size=len(word)
        for i in range(1,size):
            if len(word[i])>len(longest):
                longest=word[i]
        return longest


print(f"Longest Word is : {longestWord()}")