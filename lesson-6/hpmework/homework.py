txtxt=input('enter:')
vowels = "aeiou"
t=[]
for i in txtxt:
    t.append(i)
i=3
while i<len(txtxt):
    if t[i-1]=='_' or t[i-1] in vowels :
        
       i+=1
    t.insert(i,'_')
    i+=4
f="".join(t)
print(f)
print(txtxt) 
#================================================================
def int_sqt(a:int):
  if 0<=a: 
    for i in range(a):
      print(i**2)
#============================================================
w=11
e=0
while w>e:
    print(e)
    e+=1
#==========================================================
sequence = [1, 2, 3, 4, 5]
new_list = []
for i in sequence:
    new_list.append(i)
    print(new_list)
#===================================================
num=int(input('enter: '))
r=[]
for i in range(num+1):
   r.append(i) 
print(sum(r)) 
#=====================================================
num=int(input('enter: '))
for i in range(1,11):
    print(i*num)
#====================================================
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    print(i)
#=====================================================
num=int(input('enter: '))
r=[]
for i in str(num):
    r.append(i)
print(len(r))
#==========================================================================
sequence = [1, 2, 3, 4, 5]
w=len(sequence)
while w>=0:
    print(sequence[w::-1])
    w-=1
#==========================================================================
list1 = [10, 20, 30, 40, 50]
for i in list1[-1::-1]:
    print(i)
#==============================================================================
for i in range(-10,0):
    print(i)

#============================================================================
for i in range(5):
    print(i)
print('done')
#===================================================================================
def is_prime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:
            return False
    return True

# Generate and print prime numbers between 25 and 50
for num in range(25, 51):
    if is_prime(num):
        print(num)

#=======================================================================
n=int(input('enter: '))
for i in range(n):
    if i<=1:
        print(i)
    elif i<0:
        print("false")
    else:
        f=(i-1)+(i-2)
        print(f)
#=======================================================================
n = int(input('Enter the number of Fibonacci terms to generate: '))

if n <= 0:
    print("False - Fibonacci sequence requires a positive number.")
else:
    a, b = 0, 1  
    for i in range(n):
        print(a, end=" ")  
        a, b = b, a + b

#============================================================================================
list1 = [1, 1, 2] 
list2 = [2, 3, 4]
f=[]
for i , j in zip(list1,list2):
    if i  not in list2 :
        f.append(i)
        print(f)
    if j not in list1:
     f.append(j)
    print(f)
f  
#=============================================================================================
list1 = [1, 2, 3]
list2 = [4, 5, 6]
f=[]
for i , j in zip(list1,list2):
    if i  not in list2 :
        if i in f:
           break
        else: 
           f.append(i)
        print(f)
    if j not in list1:
    
     if j in f:
       break 
     else:
        f.append(j)
    print(f)
h=sorted(f)  
print(h)
#================================================================================================
for i  in list1:
    if i  not in list2 :
        f.append(i)
        print(f)
        for j in list2:
            if j not in list1:
                if j not in f:
                 f.append(j)
                else:
                   break
        print(f)
#===========================================================================================
n=int(input('enter: '))
h=[]
a=1
for i in range(1,n+1):
  h.append(i)
  f=a*i
  a=f

print(a,h)
