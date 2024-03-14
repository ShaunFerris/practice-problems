import random
import time
from typing import Tuple, Set


sol_one = True
sol_two = True


def lcs(strx: str, stry: str) -> Tuple[int, Set]:
    """
    This is the naive solution, in O(n^3) time
    It generates every possible substring of one input and checks if it is a substring of the other
    This version is modified to give the length and a set of all possible substrings of that length
    Replace the k comparison if blocks with `return max(k, count)` to revert to simple vers.
    """

    result = 0
    strings = set()

    for i in range(len(strx)):
        for j in range(len(stry)):
            k = 0
            while (
                (i + k) < len(strx)
                and (j + k) < len(stry)
                and strx[i + k] == stry[j + k]
            ):
                k += 1
            if k > result:
                strings = set()
                strings.add(strx[i : i + k])
                result = k
            if k == result:
                strings.add(strx[i : i + k])
    return (result, strings)


def dynamiclcs(strx: str, stry: str) -> int:
    """
    This is the better solution, running in O(n*m) time.
    This solution uses a matrix to represent the length of a common substring that ends at
    a given x,y coordinate where x is the index in the range len(str1)+1 and y is the index in
    the range len(str2)+1. Then by finding the largest value in the matrix, you can find where
    it ends in either of the input strings. By calculating the length of any substring > 1 from
    the length of previous substrings, you save computation.
    """
    n, m = len(strx), len(stry)
    suffix_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    longest = 0
    terminus = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if strx[i - 1] == stry[j - 1]:
                suffix_matrix[i][j] = (suffix_matrix[i - 1][j - 1]) + 1
                if suffix_matrix[i][j] > longest:
                    longest = suffix_matrix[i][j]
                    terminus = i
            else:
                suffix_matrix[i][j] = 0
    return strx[(terminus - longest) : (terminus)]


if __name__ == "__main__":
    # use range(97, 122) if you want the whole alphabet
    print(
        "string_a: ",
        testx := "".join(map(lambda x: chr(x), random.choices(range(97, 100), k=202))),
    )
    print(
        "string_b: ",
        testy := "".join(map(lambda x: chr(x), random.choices(range(97, 100), k=190))),
    )
    if sol_one:
        starta = time.time()
        print("longest_common_substring: ", lcs(testx, testy))
        print(f"sol_one took {time.time() - starta} seconds")

    if sol_two:
        startb = time.time()
        print(dynamiclcs(testx, testy))
        print(f"sol_one took {time.time() - startb} seconds")
