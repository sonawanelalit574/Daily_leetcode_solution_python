class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Concatenate the array with itself using list addition
        # This creates a new list with all elements of nums appearing twice in order
        return nums + nums
