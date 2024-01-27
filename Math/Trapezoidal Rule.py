def f(x):
    return 1/(1+x)
def trapezoidal_rule(a,b,n):
    h=(b-a)/n
    integral=f(a)+f(b)
    for i in range(1,n):
        integral +=2*f(a+i*h)
    integral *=h/2
    return integral
a=2
b=10
n=8
result=trapezoidal_rule(a,b,n)
print(f"resultis:",result)
