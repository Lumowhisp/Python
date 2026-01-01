def read_last_n_lines(n):
    with open("text.txt","r") as f:
        listofLines=f.readlines()
        print(listofLines)
        for line in listofLines[-n:]:
            print(line,end="")
read_last_n_lines(3)