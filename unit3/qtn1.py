def alternating(list):
    
    for i in range(len(list)):
        if i % 2 == 0:
            if list[i] % 2 != 0:
                return False
        else:
            if list[i] % 2 == 0:
                return False
    return True
print(alternating([1,2,3,4,5]))
print(alternating([2,3,4,5,6]))
print(alternating([1]))
print(alternating([1,2,4,5]))
print(alternating([12,5,6,7,8]))


