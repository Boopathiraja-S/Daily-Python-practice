# my method
input_list1 = list(map(int, input().split()))
output_list1 = [j * i for i in input_list1 for j in range(len(input_list1)) if j + 1 == i]
print(output_list1)

# Actual solution
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Using list comprehension to multiply each element by its index
output_list = [num * index for index, num in enumerate(input_list)]

print(output_list)
