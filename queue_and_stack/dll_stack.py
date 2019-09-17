import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stack is last-in, first-out
class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()
    
  def push(self, value):
    pass
  
  def pop(self):
    pass

  def len(self):
    pass
