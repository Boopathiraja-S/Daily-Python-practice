# my code
input_list1 = input().split()
output_list1 = [i[::-1] for i in input_list1 if "a" in (i[0])]
print(output_list1)

# solution
input_list = input("Enter a list of words separated by spaces: ").split()

# Using list comprehension to reverse words that start with 'a'
output_list = [word[::-1] for word in input_list if word.startswith('a')]

print(output_list)
