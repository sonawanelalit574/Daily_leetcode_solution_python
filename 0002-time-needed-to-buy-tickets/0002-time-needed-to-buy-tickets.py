class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Calculate the time required for person at position k to buy all their tickets.
      
        Each person takes 1 second to buy 1 ticket, and they go to the back of the line
        after buying 1 ticket. The process continues until person k buys all their tickets.
      
        Args:
            tickets: List where tickets[i] is the number of tickets person i wants to buy
            k: The index of the person we're tracking
      
        Returns:
            Total time in seconds for person k to buy all their tickets
        """
        total_time = 0
      
        # Iterate through each person in the queue
        for index, ticket_count in enumerate(tickets):
            # For people before or at position k:
            # They can buy at most tickets[k] tickets before person k finishes
            if index <= k:
                total_time += min(ticket_count, tickets[k])
            # For people after position k:
            # They can buy at most tickets[k] - 1 tickets before person k finishes
            # (because person k will leave after buying their last ticket)
            else:
                total_time += min(ticket_count, tickets[k] - 1)
      
        return total_time
