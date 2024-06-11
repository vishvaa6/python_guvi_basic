def count_words(text):
  words = text.split()
  return len(words)

# Here's an example of how to use the function

text = "This is a string with five words."
number_of_words = count_words(text)
print(f"The text has {number_of_words} words.")