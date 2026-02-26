import random

k = 23

fav =  0
n = 1000000
for _ in range(n):
    fav += int((len(set(random.randint(1, 365) for i in range(k))) != k))

print(fav/n)