import random


# Standard Randomized QuickSort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# Median-of-Three QuickSort
def median_of_three(arr):
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    return sorted([first, middle, last])[1]


def median_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = median_of_three(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return median_quicksort(left) + middle + median_quicksort(right)


# Testing (optional)
if __name__ == "__main__":
    arr = [random.randint(1, 1000) for _ in range(1000)]

    sorted1 = randomized_quicksort(arr)
    sorted2 = median_quicksort(arr)

    print("Sorted correctly:", sorted1 == sorted2)