#1
def n1(i,j):
    arr = []
    for x in range i:
        for y in range j:
            ls = []
            if euclid(i,j) == 1:
                ls.append(True)
            else:
                ls.append(False)
            arr.append(ls)
#2
def movenexttofront(t,link):
  place = link.index(t)
  if (place >= link.len() - 1):
    return
  elif (place == (link.len() - 2)):
    nd = t + 1
  else:
    nd = t + 2
  v = link.value_at(nd)
  n = linkedList.Node(v)
  link.prepend(n)
  link.pop(nd)
#3
def exchange(t, u, link):
    current = link.head
    if t == current.value:
        link.pop(0)
        link.prepend(u)
        print('a')
    if u == current.value:
        link.pop(0)
        link.prepend(t)
        print('b')
    while current.next:
      if current.next.value == t:
        nu = linkedList.Node(u)
        ph = current.next
        current.next = nu
        nu.next = ph
        print('c')
      elif current.next.value == u:
        nt = linkedList.Node(t)
        ph = current.next.next
        current.next = nt
        nt.next = ph
        current = current.next
        print('d')
      current = current.next
#4 
def josephus(n, m):
    people = list(range(1, n + 1))
    result = []
    index = 0
    while people:
        index = (index + m - 1) % len(people)
        result.append(people.pop(index))
    return result[0]

#5
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

#difference between regular and doubly linked list?

#6
#done in the pushdown_stack file

#7 
Give the contents of the stack after the operation EAS*Y**QUE***ST***I*ON**
'''
[E]
[E,A]
[E,A,S]
[E,A]
[E,A,Y]
[E,A]
[E]
[E,Q]
[E,Q,U]
[E,Q,U,E]
[E,Q,U]
[E,Q]
[E,Q,S]
[E,Q,S,T]
[E,Q,S]
[E,Q]
[E]
[E,I]
[E]
[E,O]
[E,O,N]
[E,O]
[E]
'''

#8 
Give the contents of the queue after the operation EAS*Y**QUE***ST***I*ON**

'''
[E]
[E,A]
[E,A,S]
[A,S]
[A,S,Y]
[S,Y]
[Y]
[Y,Q]
[Y,Q,U]
[Y,Q,U,E]
[Q,U,E]
[U,E]
[U,E,S]
[U,E,S,T]
[E,S,T]
[S,T]
[T]
[T,I]
[I]
[I,O]
[I,O,N]
[O,N]
[N]
'''

# 9
#?

#10
#
#To "put" into a queue, we can use the linked list operation prepend:
def prepend(self,value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
#To "get" from a queue, we need to remove the last value
def get(self):
  current = self.head
  while True:
    if current.next.next == None:
      current.next = None
      return
    current = current.next

