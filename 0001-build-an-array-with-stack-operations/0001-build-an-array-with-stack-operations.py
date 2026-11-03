class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        Build an array using a stack machine with Push and Pop operations.
        The stack machine pushes numbers from 1 to n sequentially.
      
        Args:
            target: Target array to build (sorted in ascending order)
            n: Maximum number that can be pushed (1 to n)
      
        Returns:
            List of operations ("Push" or "Pop") to build the target array
        """
        operations = []
        current_number = 1
      
        # Iterate through each target number
        for target_number in target:
            # Push and immediately pop all numbers before the target number
            # These numbers are not needed in the final array
            while current_number < target_number:
                operations.extend(["Push", "Pop"])
                current_number += 1
          
            # Push the target number (it will stay in the stack)
            operations.append("Push")
            current_number += 1
      
        return operations
