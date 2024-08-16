def flatten_matrix(matrix):
    # Using nested list comprehension to flatten the matrix
    return [element for row in matrix for element in row]


# Taking input, splitting by newlines for rows and spaces for elements
input_matrix = [
    list(map(int, input("Enter row elements separated by spaces: ").split()))
    for _ in range(int(input("Enter the number of rows: ")))
]

flattened_list = flatten_matrix(input_matrix)
print(flattened_list)
