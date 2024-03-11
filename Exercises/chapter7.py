import pytest 
#1 Give a sequence of "compare exchange" operations for sorting four records 

#Bubble sort 
# 31 25 33 -1
# 25 31 33 -1
# 25 31 33 -1
# 25 31 -1 33
# 25 31 -1 33
# 25 -1 31 33
# -1 25 31 33

#2 Which of the 3 elementary methods (selection sort, insertion sort, or bubble sort) runs fastest for an already sorted file?
# Insertion sort, because each element is determined to be in the right place and requires no further comparison

#3 Which of the three elementary methods runs fastest for a file in reverse order?
#bubble sort would take a long time, as we'd need to keep switching adjacent keys until the entire file is reversed
#Insertion sort would take a similar number of switches, as the very last element needs to be compared with every other element
#selection sort would take the shortest amount of time

#4 Test the hypothesis that selection sort is the fastest of the three elementary methods (for sorting integers), then insertion sort, then bubble sort

#selection sort


def selection_sort(arr):
  last_key = len(arr) - 1
  key = 0
  while key < last_key:
    min = key
    for i in range(key, last_key + 1):
      if arr[i] < arr[min]:
        min = i
    stor = arr[key]
    arr[key] = arr[min]
    arr[min] = stor
    key += 1
  return arr

#insertion sort 
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

#bubble sort 
def bubble_sort(arr):
  last_key = len(arr) 
  while last_key > 1:
    for i in range(0, last_key - 1):
      n1 = arr[i] 
      n2 = arr[i + 1] 
      if n1 > n2:
        stor = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = stor
    last_key -= 1
  return arr

#for a randomly generated array of length 10,000, selection sort took 12s, insertion sort took 25s, and bubble sort took 33s to run

#5 Give a good reason why it might be inconvenient to use a sentinel key for insertion sort (aside from the one that comes up in the implementation o
# shellsort)

#If you insert the smallest value in the front of the sorted array to avoid checking if index j < 0, if the array is long and in reversed order,
# it will take quite a long time to find the smallest value. 

#6 How many comparisons are used by Shallsort to 7-sort, then 3-sort the keys EASYQUESTION
'''
E A S Y Q U E S T I O N
1 2 3 4 5 6 7 8 9 1 1 1
                  0 1 2
----------- 7 sort -----------------------
Comparison 1: E(1) and S(8) -----> NO SWAP
Comparison 2: A(2) and T(9) -----> NO SWAP
Comparison 3: S(3) and I(10) ----> SWAP
Comparison 4: Y(4) and O(11) ----> SWAP
Comparison 5: Q(5) and N(12) ----> SWAP
---------- results -----------------------
E A I O N U E S T S Y Q
1 2 3 4 5 6 7 8 9 1 1 1
                  0 1 2
----------- 3 sort -----------------------
Comparison 6: E(1) and O(4) -----> NO SWAP
Comparison 7: A(2) and N(5) -----> NO SWAP
Comparison 8: I(3) and U(6) -----> NO SWAP
Comparison 9: O(4) and E(7) -----> SWAP
Comparison 10: N(5) and S(8) ----> NO SWAP
Comparison 11: U(6) and T(9) ----> SWAP
Comparison 12: O(7) and S(10) ---> NO SWAP
Comparison 13: S(8) and Y(11) ---> NO SWAP
Comparison 14: U(9) and Q(12) ---> SWAP
---------- results -----------------------
E A I E N T O S Q S Y U
1 2 3 4 5 6 7 8 9 1 1 1
                  0 1 2
----------- 1 sort -----------------------
11 more comparisons of adjacent keys
---------- results -----------------------
A E E I N O S T Q S U Y
1 2 3 4 5 6 7 8 9 1 1 1
                  0 1 2
------------------------------------------
It is still not fully sorted, but this took 25 comparisons
'''

#7 Give an example to show why 8,4,2,1 would not be a good way to finish off a shell sort increment sequence 

'''
L A L A U A U A V A V A Z A Z A Z

sorted:
A L A L A U A U A V A V A Z A Z Z 
'''

#8 Is selection sort stable? What about insertion sort and bubble sort?
#selection sort is stable because we always need to make the same number of comparisons every time
# Insertion sort is not stable because its complexity depends on how sorted the list already is
# Bubble sort is not stable because the # of swaps depends on how sorted the list already is (if it is already sorted it only needs one pass)

#9 Give a specialized version of distribution counting for sorting files where elements have only one of two values (either x or y)

def sort_with_2_vals(l):
  val1 = l[0]
  nv1 = l.count(val1)
  for i in l:
    if i != val1:
      val2 = i
      break
    val2 = val1
  nv2 = len(l) - nv1
  if val1 < val2:
    return(([val1] * nv1) + ([val2] * nv2))
  return(([val2] * nv2) + ([val1] * nv1))

def test_sort_with_2_vals():
  assert sort_with_2_vals([0,0]) == [0, 0]
  assert sort_with_2_vals([0,2,0,2,2,2,0,2,0,0]) == [0, 0, 0, 0, 0, 2, 2, 2, 2, 2]
  assert sort_with_2_vals([2,3,2,3,2,2,3,3,2,2,2,3,3,3,2,2,3,3,2,3,2,2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

#10 Experiment with different increment sequences for shell sort: find one that runs faster than the one given for a random file of 1000 elements.

import random


def shell_sort(list_given):
  l = list_given
  n = len(l)
  gap = n // 2
  while gap > 0:
    for i in range(gap, n):
      temp = l[i]
      j = i
      while j >= gap and l[j - gap] > temp:
        l[j] = l[j - gap]
        j -= gap
      l[j] = temp
    gap //= 2
  return l


def shell_sort_knuth(list_given):
  l = list_given
  n = len(l)
  gap = 1
  while gap < n / 3:
    gap = 3 * gap + 1
  while gap > 0:
    for i in range(gap, n):
      temp = l[i]
      j = i
      while j >= gap and l[j - gap] > temp:
        l[j] = l[j - gap]
        j -= gap
      l[j] = temp
    gap //= 3  
  return l

def shell_sort_sedgewick(list_given):
  l = list_given
  n = len(l)
  k = 0
  gap = 1
  while gap < n:
      if k % 2 == 0:
          gap = 9 * (4 ** k) - 9 * (2 ** k) + 1
      else:
          gap = 2 ** (k + 2) * (2 ** (k + 2) - 3) + 1
      k += 1
  while gap > 0:
      for i in range(gap, n):
          temp = l[i]
          j = i
          while j >= gap and l[j - gap] > temp:
              l[j] = l[j - gap]
              j -= gap
          l[j] = temp
      k -= 1
      if k % 2 == 0:
          gap = 9 * (4 ** k) - 9 * (2 ** k) + 1
      else:
          gap = 2 ** (k + 2) * (2 ** (k + 2) - 3) + 1
  return l



random_numbers = [random.randint(1, 1000) for _ in range(1000)]

#shell_sort(random_numbers)
#shell_sort_knuth(random_numbers)
#shell_sort_sedgewick(random_numbers)

#knuth seems to run the fastest 
