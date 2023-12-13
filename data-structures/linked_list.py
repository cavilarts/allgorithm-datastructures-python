class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None
    
    
  def traversal(self):
    first = self.head
    while first:
      print(first.data)
      first = first.next
    
  def add_node(self, data):
    if not self.head:
      self.head = Node(data)
    else:
      elem = self.head
      while elem.next:
          elem = elem.next
      
      elem.next = Node(data)
      
  def inser_at_head(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
      
      
  def search(self, data):
    temp = self.head
    while temp is not None:
      if temp.data == data:
        return True
      temp = temp.next
    else:
      return False
    
  def delete_node(self, data):
    temp = self.head
    
    while temp is not None:
      if temp.data == data:
        break
      prev = temp
      temp = temp.next
    prev.next = temp.next      

family = LinkedList()
family.add_node("Bob")
family.add_node("Amy")
family.add_node("Max")
family.add_node("Jenny")
family.inser_at_head("Roger")
family.traversal()
print("*" * 40)
family.delete_node("Bob")

family.traversal()
  