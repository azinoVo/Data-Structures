import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

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
        if self.right:
          return self.right.contains(target)
        else:
          return False
      elif target < self.value:
        if self.left:
          return self.left.contains(target)
        else:
          return False

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

 # DAY 2 Project ---------------------------------------------------------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Same concept but manage the order
    # Recursion left and right

  def in_order_dft(self, node):
    if node == None:
      return

    if node.left:
      print(node.value)
      node.left.in_order_dft(node.left)

    if node.right:
      print(node.value)
      node.right.in_order_dft(node.right)


#--------------------------------------------------------------------------------------

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Breadth first search - queue - first in first out

    # check each level one at a time
    # create a queue
    # put root in queue
    # while queue is not empty
    # pop first item in queue
    # check left and right add to queue
    # shift 
    # go to head of queue and continue

    # use Queue from import

  def bft_print(self, node):    
      # Tree is not empty to start, traverse and apply to queue
      # Print value as one remove it from the queue
      # top to bottom, left to right - queue
      queue_list = Queue()
      queue_list.enqueue(node)

      while queue_list.len() > 0:
        current_node = queue_list.dequeue() 
        print(current_node.value)
        if current_node.left:
          queue_list.enqueue(current_node.left)
        if current_node.right:
          queue_list.enqueue(current_node.right)

#--------------------------------------------------------------------------------------
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Notes for DEPTH FIRST TRAVERSAL  - stack - last in first out
    # create a stack
    # put root in stack
    # while stack is not empty
    # pop first item in stack
    # check root.left and put it in stack
    # check root.right and put it in stack
    # go to top of stack and continue

    # use Stack from import

  def dft_print(self, node):
    # same as bft but the functions are different pop/push instead of queue, dequeue
      # Tree is not empty to start, traverse and apply to stack
      # Print value as one remove it from the stack
      # Does dequeue automatically return the item that is removed?
      stack_list = Stack()
      stack_list.push(node)

      while stack_list.len() > 0:
        current_node = stack_list.pop() 
        print(current_node.value)
        if current_node.left:
          stack_list.push(current_node.left)
        if current_node.right:
          stack_list.push(current_node.right)
   
# STRETCH Goals --------------------------------------------------------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

    # Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass