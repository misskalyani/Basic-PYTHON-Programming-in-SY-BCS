#2. Write a python program to accept the strings which contains all vowels

def contains_all_vowels(s):
  
    s = s.lower()

    vowels = ['a', 'e', 'i', 'o', 'u']


    for vowel in vowels:
        if vowel not in s:
            return False
    return True


input_string = input("Enter a string: ")


if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
