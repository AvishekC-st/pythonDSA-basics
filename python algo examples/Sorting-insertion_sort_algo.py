"""Insertion sort
-Best case run time is O(n)
-Worst case run time is O(n^2)
"""
import random
random.seed("ABC")

def insertion_sort(array):
    """we start at 2nd index of the arr and iterate over length of the arry"""
    for i in range(1, len(array)):
        """we set j to i-1 because it will always be behind i and enver cross it"""
        j = i-1
        """The first part of the while loop ensures that J will never go left out of bounds
         and the second portion compares the two elements and makes sure that
         if the J + 1 element is smaller than J we decrement and swap
         if J+1 is not smaller the loop ends and assumes all elements are sorted"""
        while j >= 0 and array[j+1] < array[j]:
            """swapping notation so that if J+1 is smaller than j we swap the two
            elements then decrement j pointer with j -= 1 """
            array[j+1], array[j] = array[j], array[j+1]
            j -= 1
    return array


arr = [random.randint(0, 1000) for _ in range(100)]
print(arr)

print(insertion_sort(arr))
