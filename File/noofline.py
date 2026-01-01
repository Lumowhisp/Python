def no_of_line():
    with open ("text.txt","r")as f:
        countLine=0
        for line in f:
            countLine+=1
        return countLine
print(no_of_line())