def rev(num):
    rev=0
    digits=0
    while num>0:
        digits=num%10
        rev=rev*10+digits
        num=num//10
    return rev
def pallindrome(num):
    if num==rev(num):
        return True
    else:
        return False
num=int(input("Enter Number : "))
if(pallindrome(num)):
    print(f"{num} is Pallindome")
else:
    print(f"{num} is not Pallindrome")