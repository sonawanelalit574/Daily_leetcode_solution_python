class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
      
        for char in s:
            if char == ")":
                # Found closing parenthesis, need to reverse content within matching pair
                temp_chars = []
              
                # Pop characters until we find the matching opening parenthesis
                while stack[-1] != "(":
                    temp_chars.append(stack.pop())
              
                # Remove the opening parenthesis
                stack.pop()
              
                # Add reversed content back to stack (temp_chars is already in reverse order)
                stack.extend(temp_chars)
            else:
                # For opening parenthesis or regular characters, just add to stack
                stack.append(char)
      
        # Join all remaining characters to form the final result
        return "".join(stack)
