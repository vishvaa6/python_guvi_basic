vowels = 'aeiou'
input_string = "Guvi Geeks Network Private Limited"
vowel_count = 0
vowel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Convert the input string to lowercase for case-insensitive counting
input_string = input_string.lower()

for char in input_string:
  # Check if the character is a vowel
  if char in vowels:
    vowel_count += 1
    vowel_dict[char] += 1

# Print the total number of vowels
print("Total number of vowels:", vowel_count)

# Print the count of each individual vowel
for key, value in vowel_dict.items():
  print(f"Count of vowel {key}:", value)


