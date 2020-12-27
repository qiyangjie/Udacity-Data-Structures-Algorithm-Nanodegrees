# Trees are just extention of linked list
# The indivial element in Tree called Nodes
# 1. Must completed connected
# 2. Must no cycles in the tree
# 3. Each child node can only have one parent node, while parent node could have any number of child

# Tree Traversal
# Depth first search(DFS)
## Pre-order
## In-order
## Post-order
# Breadth first search (BFS)
## Level order search

# Binary Tree
# Search O(n)
# Delete: You could put a leaf in the deleted node position. O(n)
# Insert: O(log(n))

# Binary Search Tree(BST)
## BST are sorted
## search: O(log(n))
## Insert: O(log(n))
## Unbalanced BST

# Create a binary tree

# Traverse a tree
## Depth first
## Breadth first

# Create a Binary Search Tree
## Insert
## Search
## Delete

# Average Time Complexity
## log(n)


# Define a Node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    # DFS- Pre-Order Traversal


# We need a stack to help keep track of the tree nodes
class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
        visited_left: {self.visited_left}
        visited_right: {self.visited_right}
        """
        return s


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while node:
        if debug_mode:
            print(f"""
            loop count: {count}
            current node: {node}
            stack:
            {stack}
            """)
        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
        loop count: {count}
        current node: {node}
        stack: {stack}
            """)
    return visit_order


def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_value())

            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


def in_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # visit node
            visit_order.append(node.get_value())

            # traverse right sub-tree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


def post_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

            # visit node
            visit_order.append(node.get_value())

    traverse(tree.get_root())

    return visit_order


def test():
    # Create a Tree and add some nodes
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    # check Stack
    stack = Stack()
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    stack.push("dates")
    print(stack.pop())
    # print("\n")
    # print(stack)

    # pre_order_with_stack(tree, debug_mode=True)

    pre_order(tree)


if __name__ == '__main__':
    test()
