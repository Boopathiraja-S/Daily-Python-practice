# Taking input as a list of strings
input_list = input("Enter a list of words separated by spaces: ").split()

# Using list comprehension to filter words with more than 3 characters and convert them to uppercase
output_list = [word.upper() for word in input_list if len(word) > 3]

# Printing the output list
print(output_list)
