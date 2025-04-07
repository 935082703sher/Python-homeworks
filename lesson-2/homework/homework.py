import random
import string
letters=random.choice(string.ascii_letters)
digits=random.choice(string.digits)
characters=random.choice(string.punctuation)
password=letters+digits+characters
p=''.join(random.choice(password) for _ in range(12))
print(p)
a=4
print(4*a)
import math
b=24
print(b*math.pi)
c=7
n=16
print((c+n)/2)
print(c+n)
print(c*c,n*n)
from datetime import datetime
a=input('Enter your name: ')
b=input('Enter yyyy-mm-dd: ')
c=datetime.strptime(b,"%Y-%m-%d")
today=datetime.today()
age=today.year-c.year-((today.month,today.day)<(c.month,c.day))
print(f'Name { a } age {age}')
