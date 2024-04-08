import random
import datetime
import pytest
#8- Quicksort 
#1 Implement a recursive Quicksort with a cutoff to insertion sort for subfiles with less than M elements and empirically determine the value 
# of M for which it runs fastest on a random file of 1000 elements. 

def insertion_sort(arr):
  last_key = len(arr) - 1
  key = 1
  while key <= last_key:
    i = key
    while i > 0 and arr[i - 1] > arr[i]:
      stor = arr[i]
      arr[i] = arr[i - 1]
      arr[i - 1] = stor
      i -= 1
    key += 1
  return arr

def quicksort(l):
  if len(l) == 0:
    return []
  if len(l) <= cutoff:
    return insertion_sort(l)
  partitioning_element = l.pop()
  pels = [partitioning_element]
  smaller = []
  larger = []
  for i in l:
    if i < partitioning_element:
      smaller.append(i)
    elif i > partitioning_element:
      larger.append(i)
    else:
      pels.append(i)
  sm = quicksort(smaller)
  lg = quicksort(larger)
  return sm + pels + lg

#testing it

def test_quicksort():
  l1 = [23,4,3,12,3,4]
  assert quicksort(l1) == [3,3,4,4,12,23]
  l2 = [1,2,3,4,5,6,7,2,4234,64,6,2,234,213,8,9,10]
  assert quicksort(l2) == [1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 64, 213, 234, 4234]
  l3 = [1,1]
  assert quicksort(l3) == [1,1]

# experiment for smallest value of M 
random_list = [random.randint(1, 100) for _ in range(1000)]

shortest_time = None 
for cutoff in range(1000):
  rl = random_list.copy()
  st = datetime.datetime.now()
  quicksort(rl)
  et = datetime.datetime.now()
  elapsed_time = et - st
  print(cutoff,'- Execution time:', elapsed_time, 'seconds')
  if shortest_time is None or elapsed_time < shortest_time:
    shortest_time = elapsed_time
    shortest_cutoff = cutoff
print(shortest_cutoff)


#shortest_cutoff ranges from 10-20 

#2 Solve the previous problem for a nonrecursive implementation
# nonrecursive quicksort

def quicksortnr(l, cutoff=10):
  stack = [(0, len(l) - 1)]
  while stack:
      start, end = stack.pop()
      if end - start <= cutoff:
          l[start:end + 1] = insertion_sort(l[start:end + 1])
      else:
          pivot = l[start + (end - start) // 2]
          left, right = start, end
          while left <= right:
              while l[left] < pivot:
                  left += 1
              while l[right] > pivot:
                  right -= 1
              if left <= right:
                  l[left], l[right] = l[right], l[left]
                  left += 1
                  right -= 1
          if start < right:
              stack.append((start, right))
          if left < end:
              stack.append((left, end))
  return l

def test_quicksortnr():
  assert quicksortnr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 2, 3, 3, 3, 4, 4, 5, 12, 23, 23]
  assert quicksortnr([23,21,2,3,3,5,6,76,8,9,2]) == [2, 2, 3, 3, 5, 6, 8, 9, 21, 23, 76]
  assert quicksortnr([5,4,3,2,1]) == [1, 2, 3, 4, 5]

random_list = [random.randint(1, 100) for _ in range(1000)]

shortest_time = None 
for cutoff in range(1000):
  rl = random_list.copy()
  st = datetime.datetime.now()
  quicksortnr(rl,cutoff)
  et = datetime.datetime.now()
  elapsed_time = et - st
  print(cutoff,'- Execution time:', elapsed_time, 'seconds')
  if shortest_time is None or elapsed_time < shortest_time:
    shortest_time = elapsed_time
    shortest_cutoff = cutoff
print(shortest_cutoff)

# shortest cutoff = 24

#3 Solve the previous problem also incorporating the median-of-three improvement
# The median-of-three improvement is a method in which you take the first, middle, and last element of the list, and pick the median of the 
# three values as the pivot point 
# My code already uses this 

#4
#About how long will quicksort take to sort a file of N equal elements?
#O(N)

#5 What is the maximum number of times during the execution of quicksort that the largest element can be moved? 

#6 Show how the file ABABABA is partitioned, using the two methods suggested in the text

# How many comparisons does 
'''
EASYQUESTION (12)
N

1- EAEI (4)
  I
  1.1- EAE (3)
  EE
    1.11- A (2)
    1.12- [](0)
  1.2- [] (0)

2- SYQUSTO (7)
  O
  2.1- [] (0)
  2.2- SYQUST (6)
    T
    2.21- SQS (3)
      SS
      2.211- [](0)
      2.212- Q (2)
    2.22- YU (2)
      U
      2.221- [] (0)
      2.222- Y (1)

34 comparisons
'''









