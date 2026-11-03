class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert word list to set for O(1) lookup
        word_set = set(wordDict)
        n = len(s)
      
        # dp[i] represents whether s[0:i] can be segmented into words from dictionary
        # dp[0] = True means empty string can always be segmented
        dp = [True] + [False] * n
      
        # Build up the dp table
        for i in range(1, n + 1):
            # Check if s[0:i] can be segmented
            # For each position j from 0 to i-1:
            #   - dp[j] checks if s[0:j] can be segmented
            #   - s[j:i] checks if the substring from j to i is in dictionary
            # If both conditions are true for any j, then s[0:i] can be segmented
            dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
      
        # Return whether the entire string can be segmented
        return dp[n]
