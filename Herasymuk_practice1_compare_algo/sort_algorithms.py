import copy


def selection_sort(start_arr):
    array = copy.copy(start_arr)
    if_operations = 0

    # Traverse through all array elements
    for i in range(len(array)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            if_operations += 1
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]

    return if_operations


def insertion_sort(start_arr):
    arr = copy.copy(start_arr)
    if_operations = 0

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            if_operations += 1
            arr[j + 1] = arr[j]
            j -= 1

        if_operations += 1

        arr[j + 1] = key

    return if_operations


def start_merge_sort(start_arr, if_operations):
    arr = copy.copy(start_arr)

    if_operations = merge_sort(arr, if_operations)
    return if_operations


def merge_sort(arr, if_operations):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        if_operations = merge_sort(L, if_operations)  # Sorting the first half
        if_operations = merge_sort(R, if_operations)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if_operations += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return if_operations

    return if_operations


def shell_sort(start_arr):
    arr = copy.copy(start_arr)
    if_operations = 0

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                if_operations += 1
                arr[j] = arr[j - gap]
                j -= gap

            if_operations += 1

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2

    return if_operations


if __name__ == '__main__':
    array = [64, 25, 12, 22, 11]
    print("Start array is -- ", array)
    selection_sort(array)

    insertion_sort(array)

    print(start_merge_sort(array, 0))

    shell_sort(array)
