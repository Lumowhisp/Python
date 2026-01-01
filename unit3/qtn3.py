def vowel_count(sentence):
    count=0
    vowel=["A","E","I","O","U","a","e","i","o","u"]
    for ch in sentence:
        if ch in vowel:
            count=count+1
    return count
sentence=input("Enter Sentence :")
print(vowel_count(sentence))