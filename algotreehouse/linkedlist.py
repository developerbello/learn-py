class Node:
  """
    An object for storing a single node in a linked list.
    Models two attribute - data and link to the next node in the list.
  """
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data
  
  def __repr__(self):
    return "<Node data: %s>" % self.data

class LinkedList:
  """
  A singly linked list
  """

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def size(self):
    """ 
    Returns the number of node in list
    Takes O(n) time
    """

    count = 0
    current = self.head

    while current:
      count += 1
      current = current.next_node

      return count

  def add(self, data):
    """
    Adds new node containing data at the head of the list.
    Takes O(1) times
    """

    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

