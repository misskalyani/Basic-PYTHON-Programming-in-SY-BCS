#Write a Python script to sort (ascending and descending) a dictionary by value
print("Ascending")
d={"rno":56,"name":"sai","per":98.7}
for k in sorted(d.keys(),reverse=True):
    print(k)



print("Decending")
d={"rno":56,"name":"sai","per":98.7}
for k in sorted(d.keys(),reverse=False):
    print(k)
