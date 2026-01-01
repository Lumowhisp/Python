with open("text.txt","r") as f:
    text=""
    for line in f:
        text+=line
    print(text)
        