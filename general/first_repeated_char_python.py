"""
Write a function that returns the first repeated character in a given string.
Eg: in the string "YABCFDFAB" A is the first repeated character, because it is 
the earliest appearing character that is repeated. If no characters repeat, return None.
"""
import time

TEST_INPUT = "YABCFDFAB"
TEST_INPUT_2 = "ABCDEFGHIJJK"


def slow_solution(input_str):
    for index, c in enumerate(input_str):
        for c2 in input_str[index + 1 :]:
            if c == c2:
                return c
    return None


start = time.time()
print(slow_solution(TEST_INPUT_2))
end = time.time()
print(f"Function slow_solution took {end - start} seconds")


# Better solution that only iterates through the sequence once, and uses counts
def better_solution(input_str):
    counts = {}
    for c in input_str:
        if c in counts:
            return c
        else:
            counts[c] = 1
    return None


start = time.time()
print(better_solution(TEST_INPUT_2))
end = time.time()
print(f"Function better_solution took {end - start} seconds")
