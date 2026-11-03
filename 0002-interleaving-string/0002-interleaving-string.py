class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Determine if s3 is formed by interleaving of s1 and s2.
      
        Args:
            s1: First string
            s2: Second string
            s3: Target string to check if it's an interleaving of s1 and s2
          
        Returns:
            True if s3 is an interleaving of s1 and s2, False otherwise
        """
        from functools import cache
      
        # Get lengths of input strings
        len_s1, len_s2 = len(s1), len(s2)
      
        # Early termination: if lengths don't match, s3 cannot be an interleaving
        if len_s1 + len_s2 != len(s3):
            return False
      
        @cache
        def dfs(index_s1: int, index_s2: int) -> bool:
            """
            Recursively check if remaining portions can form valid interleaving.
          
            Args:
                index_s1: Current index in string s1
                index_s2: Current index in string s2
              
            Returns:
                True if remaining portions can form valid interleaving
            """
            # Base case: reached end of both strings
            if index_s1 >= len_s1 and index_s2 >= len_s2:
                return True
          
            # Calculate current index in s3
            index_s3 = index_s1 + index_s2
          
            # Try taking character from s1 if possible
            if index_s1 < len_s1 and s1[index_s1] == s3[index_s3]:
                if dfs(index_s1 + 1, index_s2):
                    return True
          
            # Try taking character from s2 if possible
            if index_s2 < len_s2 and s2[index_s2] == s3[index_s3]:
                if dfs(index_s1, index_s2 + 1):
                    return True
          
            # No valid path found
            return False
      
        # Start DFS from beginning of both strings
        return dfs(0, 0)
