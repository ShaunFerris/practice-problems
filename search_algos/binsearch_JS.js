/*
Basic implementation of the binary search algorithm in python.
*/

function binarySearch(arr, l, r, val) {
    /*
    Args:
    arr: a sorted list of integers to search for the target value.
    l: the index of the leftmost element in the search range.
    r: the index of the rightmost element in the search range.
    val: the value to be searched for in the list.
    */
   while (l <= r) {
    let mid = Math.floor(l + (r - l) / 2);
    if (arr[mid] === val) return mid;
    else if (arr[mid] > val) {
        r = mid - 1;
    } else l = mid + 1;
   }
   return -1
}

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(binarySearch(arr, 0, arr.length - 1, 3))