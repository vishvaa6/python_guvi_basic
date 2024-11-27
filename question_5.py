def is_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Test cases
print(is_palindrome("madam"))       # True
print(is_palindrome("hello"))       # False

