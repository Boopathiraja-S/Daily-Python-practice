# Read the number of rows
rows = int(input())

# Initialize an empty list to store the maximum values of each row
m = []

# Iterate over the number of rows
for i in range(rows):
    # Read a row of integers and convert it to a list of integers
    row_value = list(map(int, input(f"row:{i + 1 }: ").split()))
    # Find the maximum value in the current row and append it to the list 'm'
    m.append(max(row_value))

# Print the list of maximum values from each row
print(m)