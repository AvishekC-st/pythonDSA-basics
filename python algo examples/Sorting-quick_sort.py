def quickSort(arr, start_index, end_index):
    if end_index - start_index + 1 <= 1:
        return

    pivot = arr[end_index]
    left_pointer = start_index

    # Partition: elements smaller than pivot on left side
    for current_pointer in range(start_index, end_index):
        if arr[current_pointer] < pivot:
            tmp = arr[left_pointer]
            arr[left_pointer] = arr[current_pointer]
            arr[current_pointer] = tmp
            left_pointer += 1

    # Move pivot in-between left & right sides
    arr[end_index] = arr[left_pointer]
    arr[left_pointer] = pivot

    # Quick sort left side
    quickSort(arr, start_index, left_pointer - 1)

    # Quick sort right side
    quickSort(arr, left_pointer + 1, end_index)

    return arr
