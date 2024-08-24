# Take input from the user, split into a list of strings, then map each string to an integer
input_list = list(map(int, input().split()))

# Create a new list containing the square of each number at an even index
output_list = [pow(input_list[i], 2) for i in range(len(input_list)) if i % 2 == 0]

# Print the resulting list
print(output_list)
