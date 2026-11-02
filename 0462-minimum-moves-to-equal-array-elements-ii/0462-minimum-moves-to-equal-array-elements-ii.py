class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array to find the median
        nums.sort()
      
        # Find the median element (middle element for odd length, 
        # or either middle element for even length)
        # Using bit shift (>> 1) is equivalent to integer division by 2
        median = nums[len(nums) >> 1]
      
        # Calculate total moves as sum of absolute differences from median
        # Each absolute difference represents the number of moves for that element
        total_moves = sum(abs(num - median) for num in nums)
      
        return total_moves
