import statistics

data = [21, 19, 18, 46, 30, 18]
mid = statistics.mean(data)
mod = statistics.mode(data)

print(mid)
print(mod)

newList =[]
for i in data:
    newList.append(i*5)

print(data)
print(newList)
