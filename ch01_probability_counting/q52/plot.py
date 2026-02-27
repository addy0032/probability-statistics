from math import comb, factorial
from plotly.express import scatter

STUDENTS = 100

not_fav_prob_lst = []

for num_students in range(1, STUDENTS+1):
    not_fav = 0

    for k in range(1, num_students):
        not_fav += comb(num_students, k) * factorial(num_students-k) * (-1)**(k+1)

    not_fav_prob_lst.append(not_fav/factorial(num_students))

y = tuple((1-not_fav_prob) for not_fav_prob in not_fav_prob_lst)
x = tuple(x for x in range(1, STUDENTS+1))

fig = scatter(x=x, y=y)
fig.show()

# the value approaches a constan because the number of
# derangements is approximately equal to n!/e
# so prob of getting a derangement = (n!/e)/n! = 1/e