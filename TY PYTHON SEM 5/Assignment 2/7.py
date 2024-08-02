#Write a python program to print even length words in a string
def print_even_length_words(s):
    words = s.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

input_string = "Hello world this is a test"
print_even_length_words(input_string)
