dicttt={i:i**3 for i in range(1,23)}
a=dicttt.values()
print(a)
h=list(u for u in a)
h[-1:0:-1]
l={0: 10, 1: 20}
l.update({2:30})
print(l)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
for d in(dic2,dic3):
    dic1.update(d)
print(dic1)
seqsquare={i:i**2 for i in range(1,6)}
print(seqsquare)
seqsquare={i:i**2 for i in range(1,16)}
print(seqsquare)
settt={1,4,5}
type(settt)
for i in settt:
    print(i)
settt.add(232)
print(settt)
settt.remove(1)
print(settt)
a=int(input())
if a in settt:
    settt.remove(a)
    print(settt)
else:
    settt.add(a)
    print(settt)    
print(settt)
