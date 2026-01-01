import math
def count_PerfectSquare(num):
    count=0
    for i in range(1,num+1):
        if(math.sqrt(i)**2)==i:
            count=count+1
    return count
        
print(count_PerfectSquare(9))
        