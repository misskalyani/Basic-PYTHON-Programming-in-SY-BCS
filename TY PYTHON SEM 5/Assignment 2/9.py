#3. Write a python program to Count the Number of matching characters in a pair of string

def count_matching_characters(str1, str2):
    # Convert both strings to sets to get unique characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find the intersection of both sets to get common characters
    common_characters = set1 & set2
    
    # Return the number of common characters
    return len(common_characters)

# Example usage
str1 = "aabcddekll12@"
str2 = "bb2211@55k"
print("Number of matching characters:", count_matching_characters(str1, str2))
