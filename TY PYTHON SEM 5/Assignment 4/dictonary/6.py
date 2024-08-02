#Write a Python program to get a dictionary from an object's fields
class A:
    def __init__(self):
        self.A = 1
        self.B = 2
        self.C = 3
        self.D = 4

obj = A()
print(vars(obj))
