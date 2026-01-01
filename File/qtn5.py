def commaseperated():
    with open("text.txt","r+") as f:
        content=f.read()
        print(type(content))
        print(",".join(content))
commaseperated()