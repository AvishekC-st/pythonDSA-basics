import random
random.seed("ABC")


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left, right = array[:midpoint], array[midpoint:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

def main():
    array = [random.randint(0, 1000) for _ in range(100)]
    print("Original array:", array)

    merge_sort(array)
    print("Sorted array:", array)

if __name__ == "__main__":
    main()
