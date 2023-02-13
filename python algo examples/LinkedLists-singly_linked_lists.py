"""
insert_front: O(1)
delete_front: O(1)
search: O(n), where n is the number of nodes in the linked list.
insert_end : O(n)
delete_node: O(n), where n is the number of nodes in the linked list.
"""

class Node:
    def __init__(self, data):
        """Initialize a node with the given data."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """Initialize a linked list with a dummy node."""
        self.dummy = Node(None)
        self.head = self.dummy
        self.tail = self.dummy

    def insert_front(self, data):
        """Insert a node with the given data at the front of the list."""
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_end(self, data):
        """Insert a node with the given data at the end of the list."""
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def delete_node(self, key):
        """Delete the first node in the list with the given key."""
        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def search(self, key):
        """Return True if a node with the given key exists in the list,
        otherwise False.
        """
        current = self.head.next
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        """Print the linked list."""
        current = self.head.next
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
