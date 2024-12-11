def are_anagrams(str1, str2):
    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Taking input from the user
str1 = input("Enter the first string: ")  # First string
str2 = input("Enter the second string: ")  # Second string

# Check if the strings are anagrams and print the result
if are_anagrams(str1, str2):
    print("Anagrams")
else:
    print("Not Anagrams")
