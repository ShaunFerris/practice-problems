import random
from typing import List


# base case len < 2, partition around the pivot, recur on partitions
def quicksort(arr: List) -> List:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    lessers = [i for i in arr[1:] if i < pivot]
    greaters = [i for i in arr[1:] if i > pivot]
    return quicksort(lessers) + [pivot] + quicksort(greaters)


print(test_arr := random.choices(range(1, 100000), k=20))
print(quicksort(test_arr))
