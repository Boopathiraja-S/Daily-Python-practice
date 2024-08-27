# my solution
input_list = list(map(int, input().split()))
output_list = [[i*j for j in range(1, 10+1)] for i in input_list]
print(output_list)

# chatgpt
input_list = list(map(int, input().split()))

# Iterate over each number in input_list
for i in input_list:
    # Generate and print the multiplication table for the current number
    table = [i * j for j in range(1, 11)]
    print(table)