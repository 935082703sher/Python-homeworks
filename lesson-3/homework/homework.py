fruits=['Apple','orange','banana','ananas']
fruits[3]
numbers=[1,2,34,4,5,6,6]
numbers2=[23,4,5,66,6,7,8,9,9,90]
numbers+numbers2
numbers.append(numbers2)
numbers.extend(numbers2)
numbers.insert(7,numbers2)
numbers
newnumbers=str(numbers[0])+ ' '+str(numbers[-1])+ ' ' +str(numbers[int(len(numbers)/2)])
newnumbers32=newnumbers.split(' ')
type(newnumbers32)
movies=['avatar','moana','Forest Gump','Johny English','Alpomish']
movit=tuple(movies)
movit
cities = [
    "New York", "London", "Tokyo", "Paris", "Berlin",
    "Moscow", "Beijing", "Dubai", "Sydney", "Istanbul",
    "Mumbai", "São Paulo", "Mexico City", "Toronto", "Johannesburg",
    "Seoul", "Singapore", "Buenos Aires", "Bangkok", "Cairo"
]
for c in cities:
    if 'Paris' in c:
        print(c)
        break
    else:
        print('no') 
cities.index('Paris')      
print(cities[cities.index('Paris') ])
if 'Paris' in cities:
    print("yeas Paris")
numbers = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500]
numbers12=[]
numbers12.extend(numbers)
numbers12=numbers[:]
numbers12=numbers.copy()
numbers12=list(numbers)
numbers12
j=numbers[-1]
h=numbers[0]
numbers[0]=j
numbers[-1]=h
numbers
numbers_tuple = tuple(range(1, 11))
print(numbers_tuple)
numbers_tuple[3:7]
colors = ["Red", "Blue", "Green", "Yellow", "Red", "Blue", "Orange", "Purple", "Green", "Yellow"]
colors.count('Red')
animals = ("Lion", "Tiger", "Elephant", "Giraffe", "Zebra", "Monkey", "Kangaroo", "Panda", "Wolf", "Bear")
animals.index('Lion')
for c in animals:
    if 'Lion' in c:
        print(c)
        break
    else:
        print('no') 
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
n=tuple(tuple1+tuple2)
type(n)
my_list = [10, 20, 30, 40, 50]
my_tuple = (60, 70, 80, 90, 100)
print(len(my_list))
print(len(my_tuple))
my_list.extend(my_tuple)
my_list
max(my_tuple)
min(my_tuple)
my_tuple[::-1]
