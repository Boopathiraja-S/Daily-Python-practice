input_list = list(map(int, input().split()))  # Convert input into a list of integers
output_list = [i for i in input_list if i % 2 != 0]  # List comprehension to filter odd numbers
print(output_list)  # Print the list of odd numbers
