from math import comb

total = comb(37, 5)

print("(a):", (comb(15, 3) * comb(22, 2))/total)

fav = comb(37, 5) - (comb(22, 5) + comb(25, 5) + comb(27, 5)) + (comb(10, 5) + comb(12, 5) + comb(15, 5))
print("(b):", fav/total)