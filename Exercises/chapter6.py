#Implementation of algorithms

#1 How long does it take to count to 100,000? Estimate how long the program j:=0; from i:=1 to 100000do j := j+ 1 should take on your programming 
#environment, then run the program to test your estimate 
def count_to_100k():
    j = 0
    for i in range (1,100001):
        j = j + 1
    return(j)
  
#Estimate: ~2 seconds 
#It took less than a second- nearly immediate

#2 Answer the previous question using repeat and while
# There isn't a 'repeat' in Python so I will do while 

def count_to_100k_while():
    i = 1
    j = 0
    while i < 100001:
        j += 1
        i += 1
    return(j)
#This function also ran nearly immediately- from 100,000 iterations, it is hard to say which is more efficient. 

#3 
#By running on small values, estimate how long it would take the sieve of Eratosthenes implementation in Chapter 3 to run with n = 1,000,000
def erat(n):
    dict = {key: True for key in range(1, n+1)}
    dict[1] = False
    for i in range(2, n + 1):
        j = 2 
        if dict[i]:
            while (i * j) <= n:
                dict[i * j] = False
                j += 1
    primes = [key for key, value in dict.items() if value is True]
    return(primes)

#Estimation - ~2 seconds 
#This took about 2 seconds. 10,000,000 took about 13-15 seconds 

#4
def erat_optimized(n):
    printed = []
    dict = {key: True for key in range(1, n+1)}
    dict[1] = False
    for i in range(2, n + 1):
        j = 2 
        if dict[i]:
            while (i * j) <= n:
                dict[i * j] = False
                j += 1
        for key in range(i*2, 0, -1):
            if key <= len(dict):
                if dict[key] and not(key in printed):
                    print(key)
                    printed.append(key)
                    break


#5 Test the assertion in the text that removing recursion from the preorder tree traversal algorithm from chapter 5 (with procedure calls to the
# stack operation) makes the program slower. 

def preorder_recursive(tree, node,processed):
    processed.append(node)
    children = tree[node]
    for i in children:
        preorder_recursive(tree,i,processed)

def preorder(tree):
    node = 0
    processed = []
    preorder_recursive(tree,node,processed)
    return(processed)

def preorder_nonr(tree):
    todo = []
    processed = []
    todo.append(0)
    while todo:
        node = todo.pop()
        processed.append(node)
        children = tree[node]
        while children:
            todo.append(children.pop())
    return(processed)

#for 100 nodes, the nonrecursive implementation runs slower than the recursive implementation 



#6 Test the assertion in the text that removing recursion from the preorder tree traversal algorithm from chapter 5 (and implementing 
# stack operations inline) makes the program slower. 

def preorder_recursive(tree, node, processed):
    processed.append(node)
    children = tree[node]
    for i in children:
        preorder_recursive(tree,i,processed)
    return(processed)

#7 Examine the assembly-language program produced by the pascal compiler in your local programming environment for the recursive preorder tree traersal algorithm
# in chapter 5 

#8 design an experiment to test which of the linked list or array implementation of a pushdown stack is more efficient in your programming environment


from ll import linkedList
from ll import Node


def llps():
    linked_list_pushdown_stack = linkedList()
    for i in range(10000):
        linked_list_pushdown_stack.append(i)
    for i in range(9999,-1,-1):
        linked_list_pushdown_stack.pop(i)
    return(linked_list_pushdown_stack.display())

print(llps())
#This took 12 seconds to run


def aps():
    array_pushdown_stack = []
    for i in range(10000):
        array_pushdown_stack.append(i)
    for i in range (9999,1,-1):
        array_pushdown_stack.pop()
    return(array_pushdown_stack)
#this took 54 ms

#The reason that the array was more efficient was because I made my own linked list class, as there is not linked list object in python. 
#My linked list class implementation seems to be significantly slower than the array implementation of a pushdown stack. 




#9 Which is more efficient, the recursive or nonrecursive method for drawing a ruler in chapter 5?
# The recursive implementation is more efficient because it doesn't need to go into casework in order to determine the length of the mark that should 
# be placed depending on what we are marking for the ruler. 

# 10 Exactly how many extraneous stack pushes are used by the nonrecursive implementation given in chapter 5 when traversing a complete tree 
# of 2^n - 1 nodes in preorder. 

# 0- Each node in the entire tree is pushed onto the stack once and is pulled once 








