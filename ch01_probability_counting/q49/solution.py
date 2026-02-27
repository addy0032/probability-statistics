import plotly.express as px

# n = 5

# print((6*(5**n + 1) - 15*(4**n + 2**n) + 20*(3**n))/6**n)

LIMIT = 150

x = (n for n in range(1, LIMIT+1))
y = ((6*(5**n + 1) - 15*(4**n + 2**n) + 20*(3**n))/6**n for n in range(1, LIMIT+1))

fig = px.scatter(x=tuple(x), y=tuple(y))
fig.show()