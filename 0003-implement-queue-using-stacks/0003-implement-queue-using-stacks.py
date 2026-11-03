class MyQueue:
    """
    Implement a queue using two stacks.
    The queue follows FIFO (First In First Out) principle.
    """
  
    def __init__(self):
        """Initialize two stacks for queue implementation."""
        self.input_stack = []   # Stack for enqueue operations
        self.output_stack = []  # Stack for dequeue operations

    def push(self, x: int) -> None:
        """
        Add an element to the rear of the queue.
        Time Complexity: O(1)
      
        Args:
            x: The element to be added to the queue
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Remove and return the element from the front of the queue.
        Time Complexity: Amortized O(1), Worst case O(n)
      
        Returns:
            The front element of the queue
        """
        self._transfer_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        """
        Return the front element without removing it.
        Time Complexity: Amortized O(1), Worst case O(n)
      
        Returns:
            The front element of the queue
        """
        self._transfer_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        Check if the queue is empty.
        Time Complexity: O(1)
      
        Returns:
            True if queue is empty, False otherwise
        """
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def _transfer_if_needed(self) -> None:
        """
        Transfer elements from input_stack to output_stack when needed.
        This maintains the FIFO order by reversing the stack order.
        """
        # Only transfer when output_stack is empty
        if not self.output_stack:
            # Move all elements from input_stack to output_stack
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
