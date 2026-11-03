class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # Initialize variables for tracking sums and maximum values
        total_sum = 0  # Running sum of the array
        max_prefix_sum = 0  # Maximum prefix sum seen so far
        min_prefix_sum = 0  # Minimum prefix sum seen so far
        max_subarray_sum = 0  # Maximum subarray sum (Kadane's algorithm)
      
        # Single pass through the array to calculate all necessary values
        for num in arr:
            total_sum += num
            # Update maximum prefix sum
            max_prefix_sum = max(max_prefix_sum, total_sum)
            # Update minimum prefix sum
            min_prefix_sum = min(min_prefix_sum, total_sum)
            # Update maximum subarray sum using the formula: max_sum = current_sum - min_prefix
            max_subarray_sum = max(max_subarray_sum, total_sum - min_prefix_sum)
      
        # Start with the maximum subarray sum from a single array
        result = max_subarray_sum
        MOD = 10**9 + 7
      
        # If k = 1, return the maximum subarray sum from single array
        if k == 1:
            return result % MOD
      
        # Calculate maximum suffix sum (total_sum - minimum prefix sum)
        max_suffix_sum = total_sum - min_prefix_sum
      
        # For k >= 2, consider connecting suffix of first array with prefix of second array
        result = max(result, max_prefix_sum + max_suffix_sum)
      
        # If total array sum is positive, we can include (k-2) complete arrays in between
        if total_sum > 0:
            result = max(result, (k - 2) * total_sum + max_prefix_sum + max_suffix_sum)
      
        return result % MOD
