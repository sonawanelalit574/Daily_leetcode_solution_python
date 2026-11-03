class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
      
        # Reverse half of the number
        reversed_half = 0
        while reversed_half < x:
            # Build the reversed number digit by digit
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
      
        # For even length numbers: x == reversed_half
        # For odd length numbers: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10
