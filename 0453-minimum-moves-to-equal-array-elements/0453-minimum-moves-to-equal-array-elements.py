class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the minimum value in the array
        min_value = min(nums)
      
        # Calculate total sum of all elements
        total_sum = sum(nums)
      
        # The number of moves equals the total difference from minimum
        # This is equivalent to: sum of (each element - min_value)
        return total_sum - min_value * len(nums)
