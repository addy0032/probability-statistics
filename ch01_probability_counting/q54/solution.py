from math import comb

total = comb(30, 7)
two_two_one_one_one = comb(5, 2) * comb(6, 2) * comb(6,2) * (6**3)
three_one_one_one_one = comb(5, 1) * comb(6, 3) * (6**4)

print((two_two_one_one_one + three_one_one_one_one)/total)

not_fav = comb(5, 1) * comb(24, 7) - comb(5, 2) * comb(18, 7) + comb(5, 3) * comb(12, 7)
print(1 - not_fav/total)