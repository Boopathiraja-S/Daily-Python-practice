def is_prime(n):
    # Return False for numbers less than or equal to 1
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Taking input as a list of integers
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Using list comprehension to filter prime numbers
output_list = [num for num in input_list if is_prime(num)]

# Printing the output list
print(output_list)
