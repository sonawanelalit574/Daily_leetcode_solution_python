class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()      
        option1 = nums[-1] - nums[2]  # Change 2 smallest elements
        option2 = nums[-3] - nums[0]  # Change 2 largest elements
        option3 = nums[-2] - nums[1]  # Change 1 smallest and 1 largest
      
        # Return the minimum difference among all three strategies
        return min(option1, option3, option2)
