import plotly.express as px

PEOPLE = 366

result = 1
y = []
for i in range(365, 365-PEOPLE, -1):
    result *= i
    y.append(result/(365**(365 - i + 1)))

fig = px.scatter(x=tuple(x for x in range(1, PEOPLE+1)), y=y)
fig.show()
