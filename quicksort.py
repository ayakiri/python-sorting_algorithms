def quicksort(array, start, stop):
    if start < stop:
        q = partition(array, start, stop)
        quicksort(array, start, q - 1)
        quicksort(array, q + 1, stop)


def partition(array, start, stop):
    pivot = array[stop]
    smaller = start
    for j in range(start, stop):
        if array[j] <= pivot:
            (array[j], array[smaller]) = (array[smaller], array[j])
            smaller = smaller + 1
    (array[smaller], array[stop]) = (array[stop], array[smaller])
    return smaller
