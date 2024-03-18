from typing import List
import random


# implement selection sort using the inbuilt python min function


def select_sort(arr: List):
    # use values.index(min(values))
    output = []
    for i in range(len(arr)):
        small_idx = arr.index(min(arr))
        output.append(arr.pop(small_idx))
    return output


test_arr = random.choices(range(1, 10000), k=15)
print(select_sort(test_arr))
