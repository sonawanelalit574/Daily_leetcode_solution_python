class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Calculate minimum number of parentheses to add to make the string valid.
        A valid string has all parentheses properly matched.
      
        Args:
            s: Input string containing only '(' and ')' characters
          
        Returns:
            Minimum number of parentheses needed to make string valid
        """
        # Use stack to track unmatched parentheses
        stack = []
      
        # Process each character in the string
        for char in s:
            # If current char is ')' and top of stack is '(', we have a match
            if char == ')' and stack and stack[-1] == '(':
                # Remove the matched opening parenthesis
                stack.pop()
            else:
                # Add unmatched parenthesis (either '(' or unmatched ')')
                stack.append(char)
      
        # Remaining items in stack are all unmatched parentheses
        # Each needs a corresponding parenthesis to be valid
        return len(stack)
