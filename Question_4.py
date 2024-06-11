def count_unique_characters(string):
  
  return len(set(string))


string = "hello world"
unique_characters = count_unique_characters(string)
print(f"The string '{string}' has {unique_characters} unique characters.")
