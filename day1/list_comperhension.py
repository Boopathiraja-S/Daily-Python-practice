def even_num_power():
    # Using list comprehension to square even numbers in the list
    print([even_number ** 2 for even_number in convert_int if even_number % 2 == 0])


# Taking input, splitting by spaces, and converting to a list of integers
list_input = input("Enter a list of integers separated by spaces: ").split()
convert_int = list(map(int, list_input))

even_num_power()
