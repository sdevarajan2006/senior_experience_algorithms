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


   


        



