# my solution
input_list = input().split()
vowels = ["a", "e", "i", "o", "u"]
output_list = []
for i in input_list:
    for j in vowels:
        if j in i:
            output_list.append(i)
print(list(set(output_list)))

# chatgpt solution
input_list = input().split()
vowels = ["a", "e", "i", "o", "u"]

# Create a new list containing only strings that have at least one vowel
output_list = [word for word in input_list if any(vowel in word for vowel in vowels)]

# Remove duplicates by converting the list to a set and back to a list
output_list = list(set(output_list))

# Print the resulting list
print(output_list)
