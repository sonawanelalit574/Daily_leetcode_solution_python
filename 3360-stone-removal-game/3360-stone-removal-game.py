class Solution:
    def canAliceWin(self, n: int) -> bool:
        """
        Determines if Alice can win the game.
      
        Game rules:
        - Players take turns removing stones from a pile
        - First removal is 10 stones, then 9, then 8, and so on
        - The player who cannot make a valid move loses
        - Alice goes first
      
        Args:
            n: Initial number of stones in the pile
          
        Returns:
            True if Alice wins, False otherwise
        """
        # Start with removing 10 stones in the first turn
        stones_to_remove = 10
      
        # Count the total number of turns played
        total_turns = 0
      
        # Continue playing while there are enough stones to remove
        while n >= stones_to_remove:
            # Remove stones from the pile
            n -= stones_to_remove
          
            # Next turn requires removing one less stone
            stones_to_remove -= 1
          
            # Increment turn counter
            total_turns += 1
      
        # Alice wins if the total number of turns is odd
        # (Alice plays on odd turns: 1st, 3rd, 5th, etc.)
        return total_turns % 2 == 1
