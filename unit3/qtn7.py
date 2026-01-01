def return_small(lst):
    if not lst:
        return []

    minlength = len(lst[0])
    minlist = lst[0]

    for i in range(1, len(lst)):
        if len(lst[i]) < minlength:
            minlength = len(lst[i])
            minlist = lst[i]

    return minlist


lst = [[1], [2,2,3,4,5,6], [34,7]]
print(return_small(lst))