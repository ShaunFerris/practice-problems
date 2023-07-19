"""
Answers for the common basic coding interview question of writing a
function to detect wether or not an input string is palindromic.
"""
import time

NOT_PALI = "Hello"
PALI = "civic"


# First approach: Check along the length
def palindrome_check(input_str):
    for index, char in enumerate(input_str):
        if char != input_str[(index + 1) * -1]:
            return False
    return True


# Block commented out to not intefere with timing of the other functions
"""
start = time.time()
print(palindrome_check(PALI))
end = time.time()
print(f'Function palindrome_check took {end - start} seconds')
"""


# Second approach: only looping through half the string
def palindrome_short(input_str):
    length = len(input_str)
    for i in range(0, length // 2):
        if input_str[i] != input_str[(length - 1) - i]:
            return False
    return True


# Block commented out to not intefere with timing of the other functions
"""
start = time.time()
print(palindrome_short(PALI))
end = time.time()
print(f'Function palindrome_short took {end - start} seconds')
"""


# Third approach: reverse the input string and compare - the most concise method
def palindrome_reverse(input_str):
    return input_str == input_str[::-1]


start = time.time()
print(palindrome_reverse(PALI))
end = time.time()
print(f"Function palindrome_reverse took {end - start} seconds")

"""
All three functions run in about the same time at 0.02ms when timed independently,
ie: with the other function call and timing blocks commented out.
If you run two or more functions and their timers together, one or more of the 
functions will take about 4 times as long. All functions appear to have the same efficiency.
"""
