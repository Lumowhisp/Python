def append_to_file(sent):
    with open("text.txt","a") as f:
        f.write(sent+'\n')
def read_file():
    with open("text.txt","r") as f:
        content=f.read()
        print(content)
append_to_file("Aditya is Looser")
append_to_file("Aditya is Bhadwa")
read_file()