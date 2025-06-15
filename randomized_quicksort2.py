import random

def randomized_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def deterministic_partition(arr, low, high):
    mid = (low + high) // 2
    arr[low], arr[mid] = arr[mid], arr[low]  # move pivot to front
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

import time

def time_sort(func, arr):
    start = time.time()
    func(arr, 0, len(arr) - 1)
    return time.time() - start

if __name__ == "__main__":
    import random

    size = 1000  # change this to 5000 or more to observe timing differences
    test_cases = {
        "Random": [random.randint(0, 10000) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reversed": list(range(size, 0, -1)),
        "Repeated": [random.choice([1, 2, 3]) for _ in range(size)]
    }

    for name, data in test_cases.items():
        arr1 = data.copy()
        arr2 = data.copy()
        t_rqs = time_sort(randomized_quicksort, arr1)
        t_dqs = time_sort(deterministic_quicksort, arr2)
        print(f"{name} Array:")
        print(f"  Randomized Quicksort Time:   {t_rqs:.6f} seconds")
        print(f"  Deterministic Quicksort Time: {t_dqs:.6f} seconds\n")



