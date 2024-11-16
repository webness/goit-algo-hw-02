def check_delimiters(expression):
    # Map each closing delimiter to its corresponding opening delimiter
    matching_delimiters = {')': '(', ']': '[', '}': '{'}
    # Stack to track open delimiters as we go through the expression
    stack = []

    # Go through each character in the input string
    for char in expression:
        # If the character is an opening delimiter, add it to the stack
        if char in "({[":
            stack.append(char)
        # If the character is a closing delimiter
        elif char in ")}]":
            # Verify if there is a matching opening delimiter at the top of the stack
            if stack and stack[-1] == matching_delimiters[char]:
                stack.pop()  # Match found, remove the top item from the stack
            else:
                # Mismatch detected; delimiters are not balanced
                return "Asymmetric"

    # If stack is empty, all delimiters were matched correctly
    if not stack:
        return "Symmetrical"
    else:
        # If stack still has items, there are unmatched opening delimiters
        return "Asymmetric"


expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(f"{expr}: {check_delimiters(expr)}")
