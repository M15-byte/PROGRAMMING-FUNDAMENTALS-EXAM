# Question 2 (a)
# Palindrome check: True when a word reads the same in both directions,
# ignoring case.

def is_palindrome(word):
    """Return True if word is spelt the same in both directions,
    ignoring case."""
    lowered = word.lower()
    return lowered == lowered[::-1]      # [::-1] gives the string reversed

# Main program
entered = input("Enter a word: ")
print(f'"{entered}" is a palindrome: {is_palindrome(entered)}')
