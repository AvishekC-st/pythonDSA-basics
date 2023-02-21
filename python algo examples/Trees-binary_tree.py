"""
Initialize a Binary Tree Node which has a root node val and two nodes named left and right
which are equal to None.

Properties

Root Node
Root node is the highest node in the tree and has no parent node. All of the nodes in the tree can be reached by the
root node.

Leaf Nodes
Leaf nodes are nodes with no children. The nodes at the last level of the tree are guaranteed to be leaf nodes but
they can also be found on other levels.

Ancestor
A node connected to all the nodes below it is considered an ancestor to those nodes.

Descendant
The descendant of a node is either child of the node or child of some other descendant of the node.

Children
The children of a node are its left child and right child.


"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None