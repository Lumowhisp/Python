def leapyear(year):
    if((year%400==0)or(year%4==0 and year%100!=0)):
        return True
    else:
        return False
year=int(input("Enter Year :"))
if leapyear(year):
    print(f"{year} is Leap Year")
else:
    print(f"{year} is not Leap Year")
