from collections import deque


def is_palindrome(input_string):
    # Normalize the string by making it lowercase and removing spaces
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Initialize a deque with the characters of the normalized string
    char_deque = deque(normalized_string)

    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        # Pop characters from both ends and compare
        if char_deque.popleft() != char_deque.pop():
            return False  # If any pair doesn't match, it's not a palindrome
    return True  # All characters matched


test_string = "Паліндром — і ні морд, ні лап"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
