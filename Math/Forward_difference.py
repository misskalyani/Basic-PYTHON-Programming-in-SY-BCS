from math import factorial
x=[0,1,2,3]
y=[11,10,11,21]
x_eval=2.4
def forward_difference_interpolation(x,y,x_eval):
    h=x[1]-x[0]
    u=(x_eval-x[0])/h
    result = y[0]

    for i in range(1,len(y)):
       for j in range(len(y)-1,i-1,-1):
         y[j] = y[j] - y[j - 1]
       result +=(u*y[i]/factorial(i))
    return result
    result=forward_difference_interpolation(x,y,x_eval)
    print(f"f({x_eval})=",result)            
