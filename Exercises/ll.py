import unittest

class Node:
 def __init__(self, value):
    self.value = value
    self.next = None


class linkedList:
  def __init__(self):
    self.head = None
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
  def prepend(self,value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
  def delete(self, value):
    if not self.head:
      return
    if self.head.value == value:
      self.head = self.head.next
      return
    current = self.head
    while current.next:
      if current.next.value == value:
        current.next = current.next.next
        return
      current = current.next
  def display(self):
    current = self.head
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    result.append("None")
    return " -> ".join(result)
  def clear(self):
    self.head = None
  def count(self, val):
    n = 0
    current = self.head
    while current:
      if current.value == val:
        n += 1
      current = current.next
    return(n)
  def extend(self, ll):
    current = ll.head
    while current:
      self.append(current.value)
      current = current.next
  def index(self,val):
    counter = 0
    current = self.head
    while current:
      if current.value == val:
        return (counter)
      current = current.next
      counter += 1
    return(None)
  def insert(self, place, val):
    if place == 0:
      self.prepend(val)
      return
    ci = 0
    current = self.head
    while current:
      if (ci + 1) == place:
        new_node = Node(val)
        v = current.next
        current.next = new_node
        new_node.next = v
        break
      current = current.next
      ci += 1
  def pop(self, place):
    current = self.head
    if place == 0:
      self.head = current.next
      return
    ci = 0
    while True:
      if (ci + 1 == place):
        n = current.next
        if n.next:
          current.next = n.next
          return
        else:
          current.next = None
          return
      ci += 1
      current = current.next
  def remove(self, value):
    current = self.head
    if (current.value == value):
      self.head = current.next
      return
    while current.next:
      if current.next.value == value:
        v = current.next
        if v.next:
          current.next = v.next
          return
        else:
          current.next = None
          return
        current = current.next
  def reverse(self):
    current = self.head
    prev = None
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev
  def len(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count
  def value_at(self, n):
    if n < 0:
      return None  # Index out of range
    current = self.head
    index = 0
    while current:
      if index == n:
        return current.value
      current = current.next
      index += 1
    return None

class testLinkedList(unittest.TestCase):
  def setUp(self):
    self.mylist = linkedList()
  def test_append(self):
    self.mylist.append(1)
    self.assertEqual(self.mylist.display(), "1 -> None")
  def test_prepend(self):
    self.mylist.prepend(2)
    self.assertEqual(self.mylist.display(),"2 -> None")
  def test_delete(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(3)
    self.mylist.delete(2)
    self.assertEqual(self.mylist.display(), "1 -> 3 -> None")
  def test_clear(self):
    self.mylist.append(1)
    self.mylist.clear()
    self.assertEqual(self.mylist.display(), "None")
  def test_count(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(1)
    count = self.mylist.count(1)
    self.assertEqual(count, 2)
  def test_extend(self):
    otherlist = linkedList()
    otherlist.append(3)
    otherlist.append(4)
    self.mylist.extend(otherlist)
    self.assertEqual(self.mylist.display(), "3 -> 4 -> None")
  def test_insert(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(3)
    self.mylist.insert(2, 8)
    self.assertEqual(self.mylist.display(), '1 -> 2 -> 8 -> 3 -> None')
  def test_pop(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(3)
    self.mylist.pop(2)
    self.assertEqual(self.mylist.display(), '1 -> 2 -> None')
  def test_remove(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(3)
    self.mylist.remove(3)
    self.assertEqual(self.mylist.display(), '1 -> 2 -> None')
  def test_reverse(self):
    self.mylist.append(1)
    self.mylist.append(2)
    self.mylist.append(3)
    self.mylist.reverse()
    self.assertEqual(self.mylist.display(), '3 -> 2 -> 1 -> None')
if __name__ == '__main__':
  unittest.main()
    
