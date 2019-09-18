from doubly_linked_list import DoublyLinkedList

# We are using the dictionary as a way to give an index value toward the linked-list because
# Linked Lists do not have an index

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
    if key in self.dict:
      # self.list.move_to_end({key:{self.dict[key]}})
      node = self.dict[key]
      self.list.move_to_front(node)
      return node.value[1]
    else:
      return None
      
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
    # if self.current < self.limit:
    #   # If key already exist - replace old with new value for that key
    #   if key in self.dict:
    #       node = self.dict[key]
    #       node.value = (key, value)
    #       self.list.move_to_front(node)
    #       return
    #   else:
    #     self.list.add_to_head((key, value))
    #     self.dict[key] = self.list.head
    #     self.current += 1

    # elif self.current == self.limit:
    #   if key in self.dict:
    #       node = self.dict[key]
    #       node.value = (key, value)
    #       self.list.move_to_front(node)
    #       return
    #   else:
    #     del self.dict[self.list.tail.value[0]]
    #     self.list.remove_from_tail()
    #     self.current -= 1
    
    # Implementation from Lecture

    # If key already exist, it doesn't matter if it's less or equal to ten because
    # it will be changed or updated anyway
    if key in self.dict:
      node = self.dict[key]
      node.value = (key, value)

      self.list.move_to_front(node)
      return self.list

    # If current is equal to limit
    if self.current == self.limit:
      del self.dict[self.list.tail.value[0]]
      self.list.remove_from_tail()
      self.current -= 1

    # This instance is anything less than limit and key is not in dict already
    self.list.add_to_head((key, value))
    self.dict[key] = self.list.head
    self.current += 1


