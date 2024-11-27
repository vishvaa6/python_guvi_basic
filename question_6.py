def longest_common_substring(str1, str2):
    # Initialize a matrix to store the lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_pos = 0  # Position of the end of the longest common substring in str1

    # Build the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i

    # Extract the longest common substring
    longest_substring = str1[end_pos - max_length:end_pos]
    return longest_substring

# Test cases
str1 = "abcdef"
str2 = "zabcfgh"
result = longest_common_substring(str1, str2)
print(f"Longest common substring: '{result}'")
