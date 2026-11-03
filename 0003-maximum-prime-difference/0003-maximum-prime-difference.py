from typing import List
from math import sqrt

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        """
        Find the maximum difference between indices of two prime numbers in the array.
        Returns the maximum value of (j - i) where nums[i] and nums[j] are both prime.
        """
      
        def is_prime(n: int) -> bool:
            """
            Check if a number is prime.
          
            Args:
                n: Integer to check for primality
              
            Returns:
                True if n is prime, False otherwise
            """
            # Numbers less than 2 are not prime
            if n < 2:
                return False
          
            # Check divisibility from 2 to sqrt(n)
            # If n is divisible by any number in this range, it's not prime
            for divisor in range(2, int(sqrt(n)) + 1):
                if n % divisor == 0:
                    return False
          
            return True
      
        # Find the first prime number from the left
        for left_index, num in enumerate(nums):
            if is_prime(num):
                # Once we find the first prime, search for the last prime
                # Start from the end of the array and move backwards
                for right_index in range(len(nums) - 1, left_index - 1, -1):
                    if is_prime(nums[right_index]):
                        # Return the maximum difference between indices
                        return right_index - left_index
      
        # This line should never be reached if the input guarantees at least one prime
        return 0
