
# Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [2, 4, 10, 20, 5, 2, 20, 4]
result = remove_duplicates(my_list)
print(result) 
