def factor(num):
    list=[]
    if num==0:
        return list
    if num>=1:
        for i in range(1,num+1):
            if num%i==0:
                list.append(i)
    return list

print(factor(9))