# Taking input as a list of words
input_list = input("Enter a list of words separated by spaces: ").split()

# Using list comprehension to get the length of each word
output_list = [len(word) for word in input_list]

# Printing the output list
print(output_list)
