#to check pallindrom
def pallindrome(word):
    size=len(word)
    start=0
    end=size-1
    while start<end:
        if word[start]!=word[end]:
            return False
        start=start+1
        end=end-1
        
    return True

    
word=input("Enter a Word : ")
print(pallindrome(word))