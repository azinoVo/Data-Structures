import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stack is last-in, first-out
class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()
# Add to top of stack
  def push(self, value):
    self.size += 1
    self.storage.add_to_tail(value)

# Remove from top
  def pop(self):
    if self.size > 0:
        self.size -= 1
        return self.storage.remove_from_tail()
    else:
        return None

  def len(self):
    # return self.storage.__len__() or
    return self.size
