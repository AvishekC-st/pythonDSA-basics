"""
1. The _search_helper method takes two arguments: node and key. node represents the current node being examined in the
   search process, and key is the value being searched for in the binary search tree.

2. The method first checks whether node is None. If node is None, then the method returns None,
   indicating that the key is not in the tree.

3. If node is not None, then the method checks whether the value of node is equal to key. If the values are equal,
   then the method returns node, indicating that the key has been found in the tree.

4. If the values are not equal, then the method checks whether key is less than the value of node. If key is less than
   the value of node, then the method calls itself recursively with the left child of node as the new node argument.

5. If key is greater than the value of node, then the method calls itself recursively with the right child of node as
   the new node argument.

6. Steps 2-5 are repeated until the key is found in the tree, or it is determined that the key is not in the tree.

Time Complexity

If we have a balanced binary tree, our search algorithm will run in O(log n)
O(log n) time. Balanced binary tree means that the height of the left-subtree is equal to the height of the
right-subtree, or there is a difference of 1.

In a balanced tree, we can eliminate half the nodes each time, which results in
O(log n), for reasons we discussed in the merge sort chapter.

If we had a skewed binary tree, this would result in a time complexity of
O(n). This is also the worst case scenario.

Closing Notes
The main benefit of binary search trees compared to sorted arrays is that we are able to insert, delete and search in
O(log n) time.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


def search_helper(self, val, node):
    if node is None or node.val == val:
        return node
    elif val < node.val:
        return search_helper(val, node.left)
    else:
        return search_helper(val, node.right)


def search(self, val):
    return search_helper(val, self.root)
