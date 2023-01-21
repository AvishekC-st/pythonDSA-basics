"""Initialize left_index, right_index, and result_index to 0.

1) While left_index is less than the length of the left sub-array and
   right_index is less than the length of the right sub-array:

2) Compare the element at the current left_index of the left sub-array with
   the element at the current right_index of the right sub-array.

3) If the element in the left sub-array is smaller, add it to the
   input array at the current result_index and increment left_index.

4) If the element in the right sub-array is smaller, add it to the
   input array at the current result_index and increment right_index.

5) Increment result_index in both cases.

6)  While left_index is less than the length of the left sub-array, add
    the remaining elements of the left sub-array to the input array and
    increment left_index and result_index.

7)  While right_index is less than the length of the right sub-array,
    add the remaining elements of the right sub-array to the input array
    and increment right_index and result_index.

8)   The input array is now sorted."""

"""The runtime complexity of the merge sort algorithm is O(n log n)
because it divides the input array in half recursively, and then 
performs a linear operation (the merge operation) on the two
sub-arrays. The divide-and-conquer strategy results in a logarithmic
number of recursive calls (log n), each of which takes linear time (n)
 to merge the sub-arrays.

The space complexity of the merge sort algorithm is O(n) because it
creates two new arrays for each recursive call, one for the left
sub-array and one for the right sub-array, and it uses a small 
amount of additional memory for the indices and temporary 
variables used in the merge operation. This will require O(n)
extra space to store the two sub-arrays.

The merge sort algorithm is a stable sort, meaning that elements that
compare as equal will not be reordered as a result of the sorting.
It also is not an in-place sort, so it will require some 
extra space."""

import random

random.seed("ABC")


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2

    left_subarray, right_subarray = array[:midpoint], array[midpoint:]

    merge_sort(left_subarray)
    merge_sort(right_subarray)

    left_index = right_index = result_index = 0

    while left_index < len(left_subarray) and right_index < len(right_subarray):
        if left_subarray[left_index] < right_subarray[right_index]:
            array[result_index] = left_subarray[left_index]
            left_index += 1
        else:
            array[result_index] = right_subarray[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left_subarray):
        array[result_index] = left_subarray[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right_subarray):
        array[result_index] = right_subarray[right_index]
        right_index += 1
        result_index += 1


def main():
    array = [random.randint(0, 1000) for _ in range(100)]
    print("Original array:", array)

    merge_sort(array)
    print("Sorted array:", array)


if __name__ == "__main__":
    main()
