from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.current = 0
    self.list = DoublyLinkedList()
    self.dict = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Does the key exist in our queue?
    # If it exist, return the value associated with key
    # Then, move that key:value pair to the end of the linked list
    pass

    # Else - return None


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # Conditions for adding values: Is the queue full?
    if self.current < 10:
      # Is the key already in the queue?
      # If key already exist - replace old with new value for that key
      pass

      # else - add new key and value
    elif self.current == 10:
      # Is the key already in the queue?
      # If key already exist, replace old with new value for that key
      pass

      # else - Remove the oldest entry in the queue and add the new key:value
