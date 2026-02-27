from math import comb

fav = comb(4, 1) * comb(39, 13) - comb(4,2) * comb(26, 13) + comb(4, 3) * comb(26, 26)
total = comb(52, 13)

print(fav/total)