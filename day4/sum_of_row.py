# Take input for the number of rows
num_rows = int(input("Enter the number of rows: "))

# Initialize the 2D list (input_matrix)
input_matrix = []

# Loop to take input for each row
for _ in range(num_rows):
    # Take input as a space-separated string and convert it to a list of integers
    row = list(map(int, input(f"Enter the elements of row {_ + 1}, separated by spaces: ").split()))
    # Add the row to the input_matrix
    input_matrix.append(row)

# Use list comprehension to sum each sub-list (row) in the input_matrix
output_list = [sum(row) for row in input_matrix]

# Print the output list
print("The sum of each row is:", output_list)
