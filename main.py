import numpy.random
import heapsort
import quicksort
import bubblesort
import time
import numpy


def measure_heapsort(arr):
    # sort with random array
    start_time = time.time()
    heapsort.build_max_heap(arr)
    end_time = time.time()
    print(f"Sort random array time: {end_time - start_time}")

    # sort with already sorted array
    start_time = time.time()
    heapsort.build_max_heap(arr)
    end_time = time.time()
    print(f"Sort sorted array time: {end_time - start_time}")

    # sort with already reversed array
    arr = arr[::-1]
    start_time = time.time()
    heapsort.build_max_heap(arr)
    end_time = time.time()
    print(f"Sort reversed sorted array time: {end_time - start_time}")


def measure_quicksort(arr):
    # sort with random array
    start_time = time.time()
    quicksort.quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    print(f"Sort random array time: {end_time - start_time}")

    # sort with already sorted array
    # start_time = time.time()
    # quicksort.quicksort(arr, 0, len(arr) - 1)
    # end_time = time.time()
    print(f"Sort sorted array time: Maximum recursion depth exceeded in comparison")

    # sort with already reversed array
    # arr = arr[::-1]
    # start_time = time.time()
    # quicksort.quicksort(arr, 0, len(arr) - 1)
    # end_time = time.time()
    print(f"Sort reversed sorted array time: Maximum recursion depth exceeded in comparison")


def measure_bubblesort(arr):
    # sort with random array
    start_time = time.time()
    bubblesort.bubblesort(arr)
    end_time = time.time()
    print(f"Sort random array time: {end_time - start_time}")

    # sort with already sorted array
    start_time = time.time()
    bubblesort.bubblesort(arr)
    end_time = time.time()
    print(f"Sort sorted array time: {end_time - start_time}")

    # sort with already reversed array
    arr = arr[::-1]
    start_time = time.time()
    bubblesort.bubblesort(arr)
    end_time = time.time()
    print(f"Sort reversed sorted array time: {end_time - start_time}")


# prepare array with random ints
numpy.random.seed(1)
sample_array = numpy.random.randint(0, 50000, 100000)

heap_array = [num for num in sample_array]
quick_array = [num for num in sample_array]
bubble_array = [num for num in sample_array]

print("Heap Sort: ")
measure_heapsort(heap_array)
print("Done")

print("Quick Sort: ")
measure_quicksort(quick_array)
print("Done")

print("Bubble Sort: ")
measure_bubblesort(bubble_array)
print("Done")
