#Write a python program to Reverse words in a given String

string = "geeks quiz practice code"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))
