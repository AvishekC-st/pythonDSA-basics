"""
Time Space Complexity
We know that we have to visit every node in the tree, and if there are
n nodes in the tree, the algorithm will run in O(n).

Another interesting point is that we could actually sort an array by making use of a binary tree.
First, we would need to build the tree and insert each value. We know that there are
n values and inserting a value in the binary tree takes
log n time. Therefore, the whole process of building the tree will be
O(n log n). Traversing the tree will only take

n steps, so in total it will be
O(n+n log n).

We have mentioned before that we do not take constants into consideration. We also know that
O(n log n) will grow faster than O(n), so we can set our upper bound to O(n log n).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
