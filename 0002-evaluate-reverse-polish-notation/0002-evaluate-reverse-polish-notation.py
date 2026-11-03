from typing import List
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
      
        Args:
            tokens: List of strings representing numbers and operators (+, -, *, /)
          
        Returns:
            Integer result of the evaluated expression
        """
        # Define operator mapping to corresponding functions
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
      
        # Initialize stack to store operands
        stack = []
      
        # Process each token in the expression
        for token in tokens:
            if token in operators:
                # Pop two operands from stack (order matters for non-commutative operations)
                second_operand = stack.pop()
                first_operand = stack.pop()
              
                # Apply operator and push result back to stack
                # Use int() to truncate towards zero for division
                result = int(operators[token](first_operand, second_operand))
                stack.append(result)
            else:
                # Token is a number, push it to stack
                stack.append(int(token))
      
        # Final result is the only element left in stack
        return stack[0]
