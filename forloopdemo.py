
from statistics import mean, median, mode

#Stings forloop
mystring = 'abcabc'

for c in mystring:
    if c == 'a':
        print('A', end = ' ')
    else:
        print(c, end =' ')



#List Forloop
cars = ['bmw' , 'benz' , 'honda']

print()
print("*" * 30)

for car in cars:
    print(car)

print("*" * 30)

nums = [1, 2, 3]

for n in nums:
    print(n * 10)

print("*" * 30)
# dictionary Forloop

d = {'one': 1, 'two': 2, 'three': 3}

for k in d:
    print(k + " " + str(d[k]))

print("*" * 30)

for k,v in d.items():
    print(v,k)
    #    print(v)
print("*" * 30)

like = []
L = [(1, 2, 3), (4, 5, 6), (7, 8, 9, 10)]
for x in L:
    for y in x:
        like.append(y)
        print(y)
        # print(y, end=' ')
print(like)

max = max(like)
min = min(like)


print("The max is " + str(max) + " The min is  " + str(min))
