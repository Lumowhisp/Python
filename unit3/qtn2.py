#Taking Input From User
def digits(sentence):
    count=0
    for i in sentence:
        if i.isdigit():
            count=count+1
    return count
def upper(sentence):
    count=0
    for i in sentence:
        if i.isupper():
            count=count+1
    return count
def lower(sentence):
    count=0
    for i in sentence:
        if i.islower():
            count=count+1
    return count
sentence=input("Enter Sentence :")
print("Digits in Sentence :",digits(sentence))
print("UpperCase in Sentence:",upper(sentence))
print("LowerCase in Sentence:",lower(sentence))