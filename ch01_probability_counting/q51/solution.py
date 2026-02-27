from math import comb

not_fav = comb(4, 1) * 3**7 - comb(4, 2) * 2**7 + comb(4, 3) * 1**7
total = 4**7

print(1 - not_fav/total)