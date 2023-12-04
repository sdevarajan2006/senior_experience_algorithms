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

def dfs_recursive(n, time, timedict, ad, depth):
    timedict[n][0] = time
    time += 1
    
    # Check if the node is a leaf node
    if len(ad[n]) == 1:
        # Increment the depth for external nodes
        depth[0] += time
    
    # Check if the node has two children (internal node)
    if len(ad[n]) == 2 and n != 0:
        time += 1
    
    for i in ad[n]:
        if timedict[i][0] == 0:
            time = dfs_recursive(i, time, timedict, ad, depth)
    
    timedict[n][1] = time
    return time

def td(ad):
    timedict = {}
    for i in ad.keys():
        timedict[i] = [0, 0]
    return timedict

def external_path_length(n, ad):
    timedict = td(ad)
    depth = [0]  # To accumulate the external path length
    time = dfs_recursive(n, 1, timedict, ad, depth)
    print("External Path Length:", depth[0])

ex = {
  0: [1, 2],
  1: [0, 3],
  2: [0, 4, 5],
  3: [1],
  4: [2, 6],
  5: [2],
  6: [4]
}

external_path_length(0, ex)
