from pulp import *
model = LpProblem(name = "Solution",sense = LpMinimize)
x=LpVariable(name="x",lowBound=0)
y=LpVariable(name="y",lowBound=0)
model +=(x>=6)
model +=(y>=6)
model +=(x+y<=11)
model +=x+y
model
print('\n')
print(model.solve())
print('\nModel Objective Value = ',model.objective.value())
print('\nValue Of x = ',x.value())
print('\nValue Of y = ',y.value())
