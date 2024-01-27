def func(x):
    return x**3-2*x-5

def regula_falsi(func,a,b,tol=1e-6,max_iter=100):
    if func(a)*func(b)>=0:
        return None
    for i in range(max_iter):
        c =(a * func(b) - b * func(a))/(func(b) - func(a))
        if abs(func(c))<tol:
            return c
        if func(c) * func(a)<0:
            b=c
        else:
            a=c
    return None
a=2
b=3
root=regula_falsi(func,a,b)
if root is not None:
    print(f"real root:",root)
else:
    print("not find")
        
