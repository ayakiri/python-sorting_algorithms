def build_max_heap(array):
    heapsize = len(array)

    for i in range(heapsize // 2, -1, -1):
        max_heapify(array, heapsize, i)

    for i in range(heapsize - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, i, 0)


def max_heapify(array, heapsize, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapsize and array[left] > array[i]:
        largest = left

    if right < heapsize and array[right] > array[largest]:
        largest = right

    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])
        max_heapify(array, heapsize, largest)
