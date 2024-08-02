#Write a Python program to remove an item from a tuple

my_tuple = ('bobby', 'hadz', 'com', 'abc')
idx = my_tuple.index('hadz')
new_tuple = my_tuple[:idx] + my_tuple[idx+1:]
print(new_tuple)  # ('bobby', 'com', 'abc')


my_tuple = ('bobby', 'hadz', 'com', 'abc')
new_tuple = tuple(item for item in my_tuple if item != 'bobby')
print(new_tuple)  # ('hadz', 'com', 'abc')


