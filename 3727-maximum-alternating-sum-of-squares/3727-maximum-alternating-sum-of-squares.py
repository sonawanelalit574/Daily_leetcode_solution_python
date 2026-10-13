class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Sort the numbers in ascending order based on their squared values
        nums.sort(key=lambda x: x * x)

        # Total count of elements
        n = len(nums)

        # Sum of squares of the smaller half (first half after sorting)
        smaller_half_sum = sum(x * x for x in nums[: n // 2])

        # Sum of squares of the larger half (second half after sorting)
        larger_half_sum = sum(x * x for x in nums[n // 2:])

        # The result is the difference between the larger and smaller halves
        return larger_half_sum - smaller_half_sum
