def bubblesort(arr):
    have_swapped = False

    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                have_swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not have_swapped:
            return
