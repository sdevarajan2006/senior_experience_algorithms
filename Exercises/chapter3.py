#1
#Preorder: E,O,[Blank],A,C,P,M,L,T,E,T,[Blank],E,R,E
#Inorder: A,[Blank],C,O,P,M,L,E,T,E,T,[Blank],E,R,E
#Postorder: A,[Blank],C,O,P,M,L,E,T,E,T,[Blank],E,R,E
#Level order: E,O,T,[Blank],P,E,E,A,C,M,L,T,[Blank],R,E

#2
# What is the height of a 2-way tree with n-nodes?
# ??

#3
#           *
#         /   \
#        +     +
#       / \   / \
#      A   B C   +
#               / \
#              D   E

#4
# On paper

#5
'''
[]
[P]
[M L P]
[S M L P]
[K A S M L P]
[A S M L P]
[S M L P]
[M L P]
[L P]
[E L P]
[R E L P]
[T E R E L P]
[E R E L P]
[E E R E L P]
[E R E L P]
[R E L P]
[E L P]
[L P]
'''

#6
'''
[P]
[P M L]
[M L]
[M L S]
[L S]
[L S E]
[S E]
[S E A]
[S E A A]
[E A A]
[E A A R]
[A A R]
[A R]
[R]
[R T]
[R T E]
[T E]
[E]
[E E]
[E]
[E]
'''

#10
#Level order traversal
from collections import deque
def lot(ex, start, end):
  und = set(ex.keys())
  ds = deque()
  ps = set()
  ds.append(und.pop())
  p = {}
  while (len(ds) > 0):
    v = ds[0]
    edges = ex[v]
    for i in edges:
      if (not (i in ps) or (i in ds)):
        ds.append(i)
        if not (i in p):
          p[i] = v
    ps.add(v)
    ds.remove(v)
  e = end
  ans = deque([e])
  while (e != 0):
    ans.appendleft(p[e])
    e = p[e]
  return(list(ans))

