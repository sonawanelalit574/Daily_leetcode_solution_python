class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array in ascending order
        arr.sort()
      
        # Calculate the common difference using first two elements
        common_difference = arr[1] - arr[0]
      
        # Check if all consecutive pairs have the same difference
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_difference:
                return False
      
        return True
