# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    new_node = BinarySearchTree(value)
    # If there's nodes
    if value >= self.value: # Greater than current node, traverse and go right - check again
      # if there isn't a right, set self.right equal new_node
      if not self.right:
          self.right = new_node
      else:
        self.right.insert(value)  
    elif value < self.value: # Less than current node, traverse and go left - check again
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    # Traverse and check left and right nodes depending on current_node
    # Make sure there is a node left or right ***
    if target == self.value:
      return True
    else:
      if target > self.value:
        return self.right.contains(target)
      elif target < self.value:
        return self.left.contains(target)

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    # Go to the node all the way to the right
    if self.right:
      return self.right.get_max()
    else:
      return self.value

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    if self.left:
      self.left.for_each(cb)