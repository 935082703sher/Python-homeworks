num=int(input("enter: "))
if num%2!=0 and  num >1 and num<=100:
    print(f'{num} is weird')
elif num%2==0 and num>=2 and num<5 :
    print(f"{num} is not weird")
elif num%2==0 and num>=6 and num<20:
    print(f"{num}is weird")
elif num%2==0 and num>=20:
    print(f"{num} is not weird")
else:
    print(f"{num} is weird ")  
def leap_year( year):
    
    if (year%4==0 and year%100!=0) or year%400==0 :
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year') 
leap_year(2020)
