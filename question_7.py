from collections import Counter


def most_frequent_char(input_string):
    # Remove spaces and lowercase all characters for uniformity
    input_string = input_string.replace(" ", "").lower()

    # Count frequency of each character in the string
    char_count = Counter(input_string)

    # Find the most frequent character
    most_frequent = char_count.most_common(1)[0]

    # Return the most frequent character and its frequency
    return most_frequent


# Example usage:
input_string = input("Enter a string: ")
result = most_frequent_char(input_string)
print(f"The most frequent character is '{result[0]}' with {result[1]} occurrences.")
