import pytest
#1 Write a recursive program to draw a binary tree so that the root appears at the center of the page, 
#the root of the left subtree is at the center of the left half of the page, etc. 

def generate_binary_tree(depth, length, x=0, y=0):
    if depth == 0:
        return {"position": (x, y), "children": {}}
    else:
        left_child = generate_binary_tree(depth - 1, length / 2, x - length / 2, y - length)
        right_child = generate_binary_tree(depth - 1, length / 2, x + length / 2, y - length)
        node = {"position": (x, y), "children": {"left": left_child, "right": right_child}}
        return node

def print_tree(tree, indent=0):
    print(" " * indent + str(tree["position"]))
    for child_key, child_node in tree["children"].items():
        print_tree(child_node, indent + 4)

#2 Write a recursive program to compute the external path length of a binary tree

def dfs_recursive(n, time, parent_dict, ad):
    time += 1
    for i in ad[n]:
        if (i not in parent_dict.keys()):
            parent_dict[i] = n  
            time = dfs_recursive(i, time, parent_dict, ad)
    time += 1
    return time

def dfs(n, ad):
    leaves = []
    half_leaves = []
    parent_dict = {0: None}
    time = dfs_recursive(n, 1, parent_dict, ad)
    for i in ad.keys():
        if list(parent_dict.values()).count(i) == 0:
            leaves.append(i)
        elif list(parent_dict.values()).count(i) == 1:
            half_leaves.append(i)
    return(leaves, half_leaves, parent_dict)

def epll(leaves,pd):
    count = 0
    for i in leaves:
        subcount = 0
        current = i
        while current != 0:
            current = pd[current]
            subcount += 1
        subcount += 1
        subcount *= 2
        count += subcount
    return count
def eplhl(half_leaves,pd):
    count = 0
    for i in half_leaves:
        subcount = 0
        current = i
        while current != 0:
            current = pd[current]
            subcount += 1
        subcount += 1
        count += subcount
    return count

def epl(ad):
    leaves, half_leaves, parent_dict = dfs(0, ad)
    half_leaf_count =  eplhl(half_leaves,parent_dict)
    leaf_count = epll(leaves,parent_dict)
    print(half_leaf_count + leaf_count)

ex1 = {
  0: [1, 2],
  1: [0, 3],
  2: [0, 4, 5],
  3: [1],
  4: [2, 6],
  5: [2],
  6: [4]
}
ex2 = {0: [1],
       1: [0,2],
       2: [1,3,4],
       3: [2],
       4: [2,5],
       5: [4,6],
       6: [5]}
def test_n2():
    assert epl(ex1) == 25
    assert epl(ex2) == 32


#3 Write a program to compute the path length of a tree represented by a binary tree 
def find_leaf_nodes(adj):
    leaf_nodes = []
    for i in adj.keys():
        child = adj[i][0]
        if child == None:
            leaf_nodes.append(i)
    return(leaf_nodes)

def recursive_path_length(n, ad,sum):
    if n == 0:
        return(sum)
    children = [values[0] for values in ad.values()]
    siblings = [values[1] for values in ad.values()]
    if n in children:
        sum += 1
        place = children.index(n)
    elif n in siblings:
        place = siblings.index(n)
    ssum = recursive_path_length(list(ad.keys())[place], ad, 0)
    sum += ssum
    return(sum)
        
    
def external_path_length(ad):
    leaf_nodes = find_leaf_nodes(ad)
    total = 0
    for i in leaf_nodes:
        s = recursive_path_length(i, ad, 0)
        total += s
    return(total)  
ex_dict1 = {0: [1,None],
           1: [4,2],
           2: [None, 3],
           3: [8, None],
           4: [5, None],
           5: [6,7],
           6: [None, None],
           7: [None, None],
           8: [10,9],
           9: [None, None],
           10: [None,None]}   
ex_dict2 = {0: [1,None],
            1: [10,2],
            2: [3,None],
            3: [9,4],
            4: [6,5],
            5: [None, None],
            6: [7,None],
            7: [8,None],
            8: [None,None],
            9: [None,None],
            10: [None,None]}

ex_dict3 = {0: [1,None],
            1: [2,None],
            2: [3,None],
            3: [None,4],
            4: [None,5],
            5: [None,6],
            6: [None,7],
            7: [8,None],
            8: [None,9],
            9: [None,10],
            10: [None,11],
            11: [None,None]}


def test_n3():
    assert external_path_length(ex_dict1) == 13
    assert external_path_length(ex_dict2) == 12
    assert external_path_length(ex_dict3) == 28
   
#4 Give the coordinates produced when the recursive tree-drawing procedure given in the text is applied to the binary tree in figure 4.2
'''
P - (0,0)
L - (100,-200)
E - (150, -300)
R - (175, -350)
T - (162.5, -375)
E - (187.5, -375)
E - (181.25, -387.5)
M - (-100,-200)
S - (-150, -300)
A - (-175, -350)
A - (-125, 350)
'''

#5
#Mechanically remove the recursion from the Fibonacci program given in the text to get a to get a nonrecursive implementation
def fibonacci(n):
    fib = [0, 1]
    if n == 1:
        return 1
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def test_n5():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(2) == 1


#6
#Mechanically remove the recursion from the recursive inorder tree traversal algorithm to get a nonrecursive implementation


        



