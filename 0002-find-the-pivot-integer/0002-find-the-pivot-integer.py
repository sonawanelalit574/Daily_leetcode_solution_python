class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        Find the pivot integer x where sum(1 to x) equals sum(x to n).
      
        Args:
            n: The upper bound of the range [1, n]
          
        Returns:
            The pivot integer if it exists, otherwise -1
        """
        # Iterate through all possible pivot values from 1 to n
        for x in range(1, n + 1):
            # Check if sum from 1 to x equals sum from x to n
            # Left sum: 1 + 2 + ... + x = (1 + x) * x / 2
            # Right sum: x + (x+1) + ... + n = (x + n) * (n - x + 1) / 2
            # We can omit division by 2 on both sides for comparison
            if (1 + x) * x == (x + n) * (n - x + 1):
                return x
      
        # No pivot found in the range
        return -1
