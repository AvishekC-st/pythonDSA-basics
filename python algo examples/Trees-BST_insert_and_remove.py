"""
INSERT
1.  The insert method takes a single argument, val, which is the value to be inserted into the binary search tree.

2.  The method first checks whether the root node of the tree is None. If the root node is None, then the method creates a
    new node with the value val and sets it as the root of the tree.

3.  If the root node is not None, then the method calls the _insert_helper method with the root node and the value to be
     inserted as its arguments.

INSERT_HELPER
1.  The _insert_helper method takes two arguments: node and val. node represents the current node being examined in the
    insertion process, and val is the value to be inserted into the binary search tree.

2.  The method first checks whether val is less than the value of node. If val is less than the value of node, then the
    method checks whether the left child of node is None.

3. If the left child of node is None, then the method creates a new node with the value val and sets it as the left child
    of node.

4. If the left child of node is not None, then the method calls _insert_helper recursively with the left child of node and
    val as its arguments.

5. If val is greater than or equal to the value of node, then the method checks whether the right child of node is None.

6. If the right child of node is None, then the method creates a new node with the value val and sets it as the right
    child of node.

7. If the right child of node is not None, then the method calls _insert_helper recursively with the right child of node
    and val as its arguments.

8. Steps 5-10 are repeated until the value has been inserted into the tree.

"""


"""
REMOVE
1. The remove method takes a single argument, val, which is the value to be removed from the binary search tree.

2. The method first checks whether the root node of the tree is None. If the root node is None, then the method returns
 None as the tree is empty and there is nothing to remove.

3. If the root node is not None, then the method calls the _remove_helper method with the root node and the value to be
 removed as its arguments.


REMOVE_HELPER
1. The _remove_helper method takes two arguments: val and node. val represents the value to be removed from the binary 
    search tree, and node represents the current node being examined in the removal process.

2. The method first checks whether node is None. If node is None, then the method returns None as the value to be
    removed was not found in the tree.

3. If val is less than the value of node, then the method calls _remove_helper recursively with val and the left child
    of node as its arguments.

4. If val is greater than the value of node, then the method calls _remove_helper recursively with val and the right
    child of node as its arguments.

5. If val is equal to the value of node, then the method checks whether node is a leaf node (i.e., it has no children).

6. If node is a leaf node, then the method simply removes it by returning None.

7. If node has only one child (either a left child or a right child), then the method returns that child as the
    replacement node for node.

8. If node has two children, then the method finds the successor of node, which is the smallest value in the right
    subtree of node.

9. The method replaces the value of node with the value of its successor.

10. The method calls _remove_helper recursively with the value of the successor and the right child of node as its
    arguments to remove the successor from the tree.

11. Steps 6-14 are repeated until the value has been removed from the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_helper(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert_helper(val, node.left)
        elif val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert_helper(val, node.right)
        else:
            print("Node already exists")

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_helper(val, self.root)

    def remove_helper(self, val, node):
        if node is None:
            return node

        if val < node.val:
            node.left = self.remove_helper(val, node.left)
        elif val > node.val:
            node.right = self.remove_helper(val, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.right
                node = None
                return temp
            temp = self.get_min_value_node(node.right)
            node.val = temp.val
            node.right = self.remove_helper(temp, val, node.right)
        return node

    def remove(self, val):
        self.root = self.remove_helper(val, self.root)

    def get_min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left
        return current
