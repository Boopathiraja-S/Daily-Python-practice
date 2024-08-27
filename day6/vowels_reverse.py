input_list = input().split()  # Takes input and splits it into a list of strings
vowels = ["a", "e", "i", "o", "u"]  # List of vowels

# List comprehension that reverses the string if it contains any vowel
output_list = [i[::-1] for i in input_list if any(vowel in i for vowel in vowels)]

print(output_list)  # Prints the resulting list