from typing import List
import random


def mergesort(arr: List):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


def merge(left_arr: List, right_arr: List):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            merged.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged.append(right_arr[right_idx])
            right_idx += 1
    merged += left_arr[left_idx:]
    merged += right_arr[right_idx:]
    return merged


test_arr = random.choices(range(1, 10000), k=15)
print(test_arr)
print(mergesort(test_arr))
