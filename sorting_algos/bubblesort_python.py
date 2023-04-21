'''
Bubble sort implementation. Examine each set of adjacent elements
from left to right, and switch their poistions if they are out
of order.
'''

test = [13, 12, 145, 61, 2, 2, 4, 19, 75, 7]

def bubble(arr):
    for i in range(len(arr)):
        flag = True
        for j in range(1, len(arr)):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j - 1], arr[j]
                flag = False
        #If no swap happened the sort is finished so break
        if flag:
            break
    return arr

print(bubble(test))