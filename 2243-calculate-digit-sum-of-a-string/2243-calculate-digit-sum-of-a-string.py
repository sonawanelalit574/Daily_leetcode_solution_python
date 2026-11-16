class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """
        Repeatedly groups string into segments of size k and replaces each segment
        with the sum of its digits until the string length is at most k.
      
        Args:
            s: Input string containing only digit characters
            k: Maximum segment size for grouping
          
        Returns:
            Final string after all transformations
        """
        # Continue processing while string length exceeds k
        while len(s) > k:
            # List to store the sum of each segment
            segment_sums = []
            string_length = len(s)
          
            # Process string in segments of size k
            for start_index in range(0, string_length, k):
                # Calculate sum for current segment
                segment_sum = 0
              
                # Add all digits in current segment (handle last segment which may be smaller)
                for index in range(start_index, min(start_index + k, string_length)):
                    segment_sum += int(s[index])
              
                # Convert sum to string and add to results
                segment_sums.append(str(segment_sum))
          
            # Join all segment sums to form new string for next iteration
            s = "".join(segment_sums)
      
        return s
