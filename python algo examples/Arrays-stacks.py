"""
A stack is a data structure that follows the Last-In-First-Out (LIFO) principle, meaning that the last element added
to the stack is the first element to be removed. Here's an implementation of a stack in Python using a list:
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack.
        If the stack is empty, return None.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it.
        If the stack is empty, return None.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0
