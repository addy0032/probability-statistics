from math import comb, factorial

not_fav = 0

for k in range(1, 21):
    not_fav += comb(20, k) * factorial(20-k) * (-1)**(k+1)

not_fav *= factorial(20)
total = factorial(20) * factorial(20)

print(1 - not_fav/total)