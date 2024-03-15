from typing import List

"""
Problem statement:
Given an integer array nums of length n, and an integer target, find the sum of three integers in
nums that comes closest to the target. Return the sum.
"""

test = [0, 3, 97, 102, 200]  # target=300 expected output 300


def closest_three_sum(nums: List, target: int):
    # sort array, use out to in scan with the two pointers, boundary condition left < right
    nums.sort()
    closest = float("inf")

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = sum([nums[left], nums[right], nums[i]])
            if abs(target - curr_sum) < abs(target - closest):
                closest = curr_sum
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return closest
    return closest


print(closest_three_sum(test, 300))
