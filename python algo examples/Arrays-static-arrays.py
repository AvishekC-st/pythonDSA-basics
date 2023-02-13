"""
time complexity of the various functions in the StaticArray class are as follows:

insertEnd: O(1)

removeEnd: O(1)

insertMiddle: O(n), where n is the number of elements in the array. This is because when inserting an element in the
middle of the array, all elements to the right of the insertion index need to be shifted one position to the right,
 which takes n operations.

removeMiddle: O(n), where n is the number of elements in the array. This is because when removing an element from the
 middle of the array, all elements to the right of the removal index need to be shifted one position to the left,
which takes n operations.

get: O(1)

set: O(1)
"""

class StaticArray:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.count = 0

    def get(self, index):
        """Get the value at a specified index in the array
        :param index: The index of the value to get.
        :return: The value t the specified index, or None if the index is
                 out of bounds"""
        if 0 <= index < self.count:
            return self.array[index]
        else:
            return None

    def set(self, index, value):
        """Set the value at the specified index in the array.
        :param index: The index at which to set the value.
        :param value: The value to be set.
        :return: True if the value was set successfully,False otherwise."""
        if 0 <= index < self.size:
            self.array[index] = value
            return True
        else:
            return False

    def display(self):
        """
        Display The values in the array.
        """
        print(self.array[:self.count])

    def insert_end(self, value):
        """
        Insert a value at the end of the array
        :param value: the value to insert.
        :return: True if the value was inserted successfully, False otherwise
        """
        if self.count < self.size:
            self.array[self.count] = value
            self.count += 1
            return True
        else:
            return False

    def remove_end(self):
        """
        remove the value at the end of the array.
        :return: True if the value was removed successfully, false otherwise
        """
        if self.count > 0:
            self.count -= 1
            self.array[self.count] = None
            return True
        else:
            return False

    def insert_middle(self, index, value):
        """
        Insert a value at a specified index in the middle of the array
        :param index: The index at which to insert the value
        :param value:  to insert
        :return: true if the value was inserted successfully, False otherwise
        """
        if self.count < self.size and index >= 0 and index < self.count:
            for i in range(self.count - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value
            self.count += 1
            return True
        else:
            return False

    def remove_middle(self, index):
        """
        Remove the value at a specified index in the middle of the array
        :param index: The index of the value to remove
        :return: True if the value was removed successfully, False otherwise
        """
        if self.count > 0 and index >= 0 and index < self.count:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
            self.array[self.count - 1] = None
            return True
        else:
            return False


# Create a StaticArray object with size 5
arr = StaticArray(10)

# Insert elements 1, 2, 3, 4, and 5 at the end of the array
arr.insert_end(1)
arr.insert_end(2)
arr.insert_end(3)
arr.insert_end(4)
arr.insert_end(5)

# Verify that the array now contains [1, 2, 3, 4, 5]
print(arr.array)

arr.set(5, 6)
print(arr.array)

