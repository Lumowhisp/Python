def creating_inputfile():
    with open("input.txt","w")as f:
        f.write("1 2 3 4 5 6 7 8 90")
def even_file(n):
    with open("even_file.txt","a+")as f:
        f.write(n+"\n")
def odd_file(n):
    with open("odd_file.txt","a+")as f:
        f.write(n+"\n")
def odd_even():
    with open("input.txt","r")as f:
        content=f.read().split()
        print(content)
        size=len(content)
        for i in range(size):
            if(int(content[i])%2==0):
                even_file(content[i])
            else:
                odd_file(content[i])
    

# creating_inputfile()
odd_even()
