Explanation from chatGPT for reference:

The function uses a while loop to iteratively narrow down the search range until either the target value is found or the search range is empty (i.e., l > r). The algorithm calculates the middle index of the current search range using the formula mid = l + (r - l) // 2.

If the middle element of the search range is equal to the target value, the function returns its index. If the middle element is greater than the target value, the search range is updated to the left half of the current search range, excluding the middle element. Otherwise, the search range is updated to the right half of the current search range, excluding the middle element.

If the target value is not found within the search range, the function returns -1 to indicate that the value was not found in the list.