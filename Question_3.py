def remove_vowels(text):
  vowels = 'aeiouAEIOU'
  return ''.join([char for char in text if char not in vowels])

text = "Hello, world!"
text_without_vowels = remove_vowels(text)
print(text_without_vowels)
