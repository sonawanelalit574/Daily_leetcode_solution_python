class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the largest rectangle area in a histogram.
      
        Uses a monotonic stack to find the nearest smaller elements on both sides
        for each bar, which determines the maximum width for rectangles with
        that bar's height.
      
        Args:
            heights: List of non-negative integers representing histogram bar heights
          
        Returns:
            The area of the largest rectangle in the histogram
        """
        n = len(heights)
      
        # Stack to maintain indices of bars in increasing height order
        stack = []
      
        # left[i] stores the index of the nearest smaller element to the left of i
        # Initialize to -1 (no smaller element on the left)
        left_boundaries = [-1] * n
      
        # right[i] stores the index of the nearest smaller element to the right of i
        # Initialize to n (no smaller element on the right)
        right_boundaries = [n] * n
      
        # Single pass to find both left and right boundaries
        for i, current_height in enumerate(heights):
            # Pop elements from stack that are >= current height
            # These elements have found their right boundary (current index)
            while stack and heights[stack[-1]] >= current_height:
                right_boundaries[stack[-1]] = i
                stack.pop()
          
            # The remaining top of stack (if exists) is the left boundary for current element
            if stack:
                left_boundaries[i] = stack[-1]
          
            # Add current index to stack
            stack.append(i)
      
        # Calculate maximum rectangle area
        # For each bar, the rectangle width is (right_boundary - left_boundary - 1)
        # and height is the bar's height
        max_area = max(
            height * (right_boundaries[i] - left_boundaries[i] - 1) 
            for i, height in enumerate(heights)
        )
      
        return max_area
