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

def main():
    binary_tree = generate_binary_tree(3, 200)
    print_tree(binary_tree)

if __name__ == "__main__":
    main()

