import pytest
#1 Write a recursive program to draw a binary tree so that the root appears at the center of the page, 
#the root of the left subtree is at the center of the left hlaf of the page, etc. 

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

#Write a recursive program to compute the external path length of a binary tree

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


#write a program to compute the path length of a tree represented by a binary tree 

#outline
#the binary tree has to have a left node and right node, rather than just being represented by an adjacency dict 
#so that it is clear which is the child and which is the sibling. 
#For example if a node had a child but no sibling it's adjacency dict would be [child,none]
#similarly, if a node had s sibling but no child it's adjacency dict would be [none, child]

ex = {1: [2, None],
      2: [None,3],
      3: [4, None],
      4: [7,5],
      5: [8,6],
      6: [None, None],
      7: [None, None],
      8: [9, None],
      9: [None, 10],
      10: [None,None]}

#The leaf nodes are the ones that are either [None, None] or [None, n], meaning if the first
# number in the adjacency dict is "none"
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
    #elif n is in the child of someone: 
        #sum += 1
        #recursive_path_length(parent, ad, sum)
    #else( n is the sibling of someone):
       # recursive_path_length(sibling, ad, sum)
    
def external_path_length(ad):
    leaf_nodes = find_leaf_nodes(ad)
    total = 0
    for i in leaf_nodes:
         
#we can use this to recursively find the path length back up to the parent(1) and calculate the EPL
#For each leaf node, we check if its the child of anything. 
#If it isn't we check who it is the sibling of
#keep going sibling until a parent is found 
# †he three lines above will be recursive 
   


        



