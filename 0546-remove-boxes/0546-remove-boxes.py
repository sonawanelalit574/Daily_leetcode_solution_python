class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        Remove boxes to maximize points. When removing k consecutive boxes of the same color,
        you get k * k points.
      
        Args:
            boxes: List of integers representing box colors
          
        Returns:
            Maximum points obtainable by removing all boxes
        """
        from functools import cache
      
        @cache
        def dfs(left: int, right: int, extra_count: int) -> int:
            # Base case: no boxes left
            if left > right:
                return 0
          
            # Optimization: merge consecutive boxes of same color at the right end
            # This reduces redundant states in memoization
            while left < right and boxes[right] == boxes[right - 1]:
                right -= 1
                extra_count += 1
          
            # Option 1: Remove boxes[right] along with extra_count boxes of same color
            max_points = dfs(left, right - 1, 0) + (extra_count + 1) * (extra_count + 1)
          
            # Option 2: Try to merge boxes[right] with boxes[mid] where they have same color
            # Split the problem into two subproblems
            for mid in range(left, right):
                if boxes[mid] == boxes[right]:
                    # Remove boxes between mid and right first, then merge boxes[mid] with boxes[right]
                    points = (dfs(mid + 1, right - 1, 0) + 
                             dfs(left, mid, extra_count + 1))
                    max_points = max(max_points, points)
          
            return max_points
      
        # Calculate result for entire array
        n = len(boxes)
        result = dfs(0, n - 1, 0)
      
        # Clear cache to free memory
        dfs.cache_clear()
      
        return result
