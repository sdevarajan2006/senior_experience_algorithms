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

