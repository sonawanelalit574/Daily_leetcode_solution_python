class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Check if a string with parentheses and wildcards can be valid.
        '*' can be treated as '(', ')', or empty string.
      
        Args:
            s: Input string containing '(', ')', and '*'
      
        Returns:
            True if the string can form valid parentheses, False otherwise
        """
        n = len(s)
      
        # dp[i][j] represents whether substring s[i:j+1] can be valid
        # Initialize a 2D DP table with False values
        dp = [[False] * n for _ in range(n)]
      
        # Base case: single character substrings
        # Only '*' can be valid (as empty string)
        for i, char in enumerate(s):
            dp[i][i] = (char == '*')
      
        # Fill the DP table for substrings of increasing length
        # Process from right to left for starting position
        for i in range(n - 2, -1, -1):
            # Process from left to right for ending position
            for j in range(i + 1, n):
                # Case 1: Check if s[i] and s[j] can form a matching pair
                # s[i] can be '(' or '*' (acting as '(')
                # s[j] can be ')' or '*' (acting as ')')
                # The substring between them should be valid (or empty)
                is_matching_pair = (
                    s[i] in '(*' and 
                    s[j] in '*)' and 
                    (i + 1 == j or dp[i + 1][j - 1])
                )
              
                # Case 2: Try to split the substring at any position k
                # Both parts should be independently valid
                can_split = any(
                    dp[i][k] and dp[k + 1][j] 
                    for k in range(i, j)
                )
              
                # Substring is valid if either case works
                dp[i][j] = is_matching_pair or can_split
      
        # Return whether the entire string can be valid
        return dp[0][n - 1]
