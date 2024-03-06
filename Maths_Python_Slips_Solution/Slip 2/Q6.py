from pulp import*
model = LpProblem(name ="Solution",sense=LpMaximize)
x = LpVariable(name ="x",lowBound=0)
y = LpVariable(name ="y",lowBound=0)
model += (x+y<=7)
model += (2*x+5*y<=1)
model +=5*x+3*y
print('\n',model)
print('\n',model.solve())
print('\nModel Objective Value = ',model.objective.value())
print('\nValue Of x = ',x.value())
print('\nValue Of y = ',y.value())
