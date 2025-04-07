def prime(n):
  for i in range(2,int(n**0.5) + 1):
    if  n%i==0:
      return f'it is not {n} prime '
    
  return "wrong"
def digit_sum(k) :
    d=str(k)
    f=0
    for i in d:
        f+=int(i)
    return f     
def square(n):
    for i in range(1,n):
        for j in range(n):
             if i**j<=10:
                print(f"{i}^{j} = {i**j}")
