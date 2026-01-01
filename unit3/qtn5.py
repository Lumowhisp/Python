import math
def is_PerfectSquare(number):
    if (math.sqrt(number)**2)==number:
        return number
    else:
        return -1

print(is_PerfectSquare(4))
print(is_PerfectSquare(40))
print(is_PerfectSquare(36))
print(is_PerfectSquare(49))
