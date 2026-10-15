class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        array_length = len(nums)
      
        # Iterate through all possible starting positions of subarrays
        for start_index in range(array_length):
            # Set to track distinct elements in current subarray
            distinct_elements = set()
          
            # Extend the subarray from start_index to each possible ending position
            for end_index in range(start_index, array_length):
                # Add current element to the set of distinct elements
                distinct_elements.add(nums[end_index])
              
                # Calculate square of distinct count and add to total
                distinct_count = len(distinct_elements)
                total_sum += distinct_count * distinct_count
              
        return total_sum
