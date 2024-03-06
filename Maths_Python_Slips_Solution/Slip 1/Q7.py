from pulp import *
model = LpProblem(name = "Solution",sense = LpMaximize)
x = LpVariable(name = "x",lowBound = 0)
y = LpVariable(name = "y",lowBound = 0)
model += (4*x+6*y<=24)
model +=(5*x+3*y<=15)
model +=150*x+75*y
model
print('\n')
print(model.solve())
print('\nModel Objective Value = ',model.objective.value())
print('\nValue Of x = ',x.value())
print('\nValue Of y = ',y.value())
