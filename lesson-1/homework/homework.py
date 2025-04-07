import re
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])
txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[-1::-2])
txt = "I'am John. I am from London"
j=txt.split(" ")
print(j[-1])
print(txt[::-1])
print()
l="".join(txt)
print(l)
vowels="".join(re.findall(r"[aeouiAOIUE]",txt))
print(len(vowels))
k=input('Enter list of numbers :')
u=k.split(',')
print(k)
max_value=int(u[0])
for num in u:
    if int(num)>int(max_value):
       max_value=num
       print(max_value)
txt=input(' enter :')
if txt==txt[::-1]:
    print('palindrome')
else :
    print('No')
w=txt.split('@')[-1]
print(w)
