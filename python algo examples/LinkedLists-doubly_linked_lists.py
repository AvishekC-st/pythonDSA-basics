class DoublyLinkedNode:
    def __init__(self, data):
        # Each node contains a value and pointers to the previous and next nodes in the list
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # The dummy node is used as a placeholder and to simplify the implementation of the linked list
        self.dummy = DoublyLinkedNode(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def insert_front(self, data):
        # Insert a new node at the front of the list by pointing its next pointer to the current first node
        # and updating the previous pointer of the current first node to point to the new node
        new_node = DoublyLinkedNode(data)
        new_node.next = self.dummy.next
        self.dummy.next.prev = new_node
        self.dummy.next = new_node
        new_node.prev = self.dummy

    def insert_end(self, data):
        # Insert a new node at the end of the list by pointing its previous pointer to the current last node
        # and updating the next pointer of the current last node to point to the new node
        new_node = DoublyLinkedNode(data)
        new_node.prev = self.dummy.prev
        self.dummy.prev.next = new_node
        self.dummy.prev = new_node
        new_node.next = self.dummy

    def delete_front(self):
        # Delete the first node by updating the next pointer of the dummy node to point to the next node
        # and updating the previous pointer of the next node to point to the dummy node
        if self.dummy.next == self.dummy:
            return None
        node_to_delete = self.dummy.next
        self.dummy.next = node_to_delete.next
        node_to_delete.next.prev = self.dummy
        return node_to_delete.data

    def delete_end(self):
        # Delete the last node by updating the previous pointer of the dummy node to point to the previous node
        # and updating the next pointer of the previous node to point to the dummy node
        if self.dummy.prev == self.dummy:
            return None
        node_to_delete = self.dummy.prev
        self.dummy.prev = node_to_delete.prev
        node_to_delete.prev.next = self.dummy
        return node_to_delete.data
