# Taking input as a list of integers
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Using list comprehension to filter odd numbers and increment them by 1
output_list = [i + 1 for i in input_list if i % 2 != 0]

# Printing the output list
print(output_list)
