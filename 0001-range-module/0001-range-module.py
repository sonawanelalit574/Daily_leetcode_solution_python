class SegmentTreeNode:
    """Node for the dynamic segment tree."""
    __slots__ = ['left', 'right', 'lazy_tag', 'is_covered']
  
    def __init__(self):
        self.left = None  # Left child node
        self.right = None  # Right child node
        self.lazy_tag = 0  # Lazy propagation tag: 1 for add, -1 for remove, 0 for none
        self.is_covered = False  # Whether this range is fully covered


class DynamicSegmentTree:
    """Dynamic segment tree for range operations."""
    __slots__ = ['root']
  
    def __init__(self):
        self.root = SegmentTreeNode()
  
    def modify(self, query_left: int, query_right: int, operation: int, 
               tree_left: int = 1, tree_right: int = 10**9, node: SegmentTreeNode = None) -> None:
        """
        Modify a range in the segment tree.
      
        Args:
            query_left: Left boundary of the query range
            query_right: Right boundary of the query range
            operation: 1 for add operation, -1 for remove operation
            tree_left: Left boundary of current tree node's range
            tree_right: Right boundary of current tree node's range
            node: Current tree node
        """
        if node is None:
            node = self.root
      
        # If current range is completely within query range
        if tree_left >= query_left and tree_right <= query_right:
            if operation == 1:
                # Mark range as covered
                node.lazy_tag = 1
                node.is_covered = True
            else:
                # Mark range as not covered
                node.lazy_tag = -1
                node.is_covered = False
            return
      
        # Push down lazy tag before going to children
        self._push_down(node)
      
        # Recursively update children
        mid = (tree_left + tree_right) >> 1
        if query_left <= mid:
            self.modify(query_left, query_right, operation, tree_left, mid, node.left)
        if query_right > mid:
            self.modify(query_left, query_right, operation, mid + 1, tree_right, node.right)
      
        # Update current node based on children
        self._push_up(node)
  
    def query(self, query_left: int, query_right: int, 
              tree_left: int = 1, tree_right: int = 10**9, node: SegmentTreeNode = None) -> bool:
        """
        Query whether a range is fully covered.
      
        Args:
            query_left: Left boundary of the query range
            query_right: Right boundary of the query range
            tree_left: Left boundary of current tree node's range
            tree_right: Right boundary of current tree node's range
            node: Current tree node
          
        Returns:
            True if the entire range is covered, False otherwise
        """
        if node is None:
            node = self.root
      
        # If current range is completely within query range
        if tree_left >= query_left and tree_right <= query_right:
            return node.is_covered
      
        # Push down lazy tag before querying children
        self._push_down(node)
      
        # Query children and combine results
        mid = (tree_left + tree_right) >> 1
        result = True
      
        if query_left <= mid:
            result = result and self.query(query_left, query_right, tree_left, mid, node.left)
        if query_right > mid:
            result = result and self.query(query_left, query_right, mid + 1, tree_right, node.right)
      
        return result
  
    def _push_up(self, node: SegmentTreeNode) -> None:
        """
        Update parent node based on children nodes.
      
        Args:
            node: Current node to update
        """
        # A node is covered only if both children exist and are covered
        node.is_covered = bool(node.left and node.left.is_covered and 
                              node.right and node.right.is_covered)
  
    def _push_down(self, node: SegmentTreeNode) -> None:
        """
        Push down lazy tag to children nodes.
      
        Args:
            node: Current node whose lazy tag needs to be pushed down
        """
        # Create children if they don't exist
        if node.left is None:
            node.left = SegmentTreeNode()
        if node.right is None:
            node.right = SegmentTreeNode()
      
        # Push down lazy tag if it exists
        if node.lazy_tag:
            # Apply lazy tag to children
            node.left.lazy_tag = node.right.lazy_tag = node.lazy_tag
            node.left.is_covered = (node.lazy_tag == 1)
            node.right.is_covered = (node.lazy_tag == 1)
            # Clear current node's lazy tag
            node.lazy_tag = 0


class RangeModule:
    """
    Module for managing ranges with add, query, and remove operations.
    """
  
    def __init__(self):
        self.tree = DynamicSegmentTree()
  
    def addRange(self, left: int, right: int) -> None:
        """
        Add a range [left, right) to the module.
      
        Args:
            left: Start of the range (inclusive)
            right: End of the range (exclusive)
        """
        # Convert to inclusive range [left, right-1]
        self.tree.modify(left, right - 1, 1)
  
    def queryRange(self, left: int, right: int) -> bool:
        """
        Check if the range [left, right) is fully covered.
      
        Args:
            left: Start of the range (inclusive)
            right: End of the range (exclusive)
          
        Returns:
            True if the entire range is covered, False otherwise
        """
        # Convert to inclusive range [left, right-1]
        return self.tree.query(left, right - 1)
  
    def removeRange(self, left: int, right: int) -> None:
        """
        Remove a range [left, right) from the module.
      
        Args:
            left: Start of the range (inclusive)
            right: End of the range (exclusive)
        """
        # Convert to inclusive range [left, right-1]
        self.tree.modify(left, right - 1, -1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
