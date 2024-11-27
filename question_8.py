def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare
    return sorted(str1) == sorted(str2)


# Example usage
string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))  # Output: True
