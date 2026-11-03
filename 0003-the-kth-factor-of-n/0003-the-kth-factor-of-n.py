class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Find the kth factor of n in ascending order.
      
        Args:
            n: The number to find factors of
            k: The position of the factor to return (1-indexed)
          
        Returns:
            The kth factor of n, or -1 if n has less than k factors
        """
        # Iterate through all potential factors from 1 to n
        for i in range(1, n + 1):
            # Check if i is a factor of n
            if n % i == 0:
                # Decrement k for each factor found
                k -= 1
                # If we've found the kth factor, return it
                if k == 0:
                    return i
      
        # If we've checked all numbers and k > 0, n has fewer than k factors
        return -1
