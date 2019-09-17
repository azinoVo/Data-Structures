from doubly_linked_list import DoublyLinkedList

# First In, First Out
class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

# Add an item to the back of the queue
  def enqueue(self, value):
    self.size += 1
    self.storage.add_to_tail(value)

# Remove and return an item from the front of the queue
  def dequeue(self):
    if self.size > 0:
        self.size -= 1
        self.storage.remove_from_head()
    else:
        pass

# Returns the number of items in the queue
  def len(self):
    return self.size

Queue().enqueue(3)
print(Queue().storage.head)
