#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the formd = dict((i,i*i) for i in range(1,n+1))(x, x*x)
n = int(input("Input a number "))
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print(d) 
