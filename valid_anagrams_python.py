'''
Create a function that takes two inputs and returns true if they are anagrams
or false if they are not.
'''
import time

w1 = 'garden'
w2 = 'danger'

#Solution one, my blind attempt at solving this problem.
def is_anagram(w1, w2):
    let_list1, let_list2 = [*w1], [*w2]
    if len(let_list1) != len(let_list2):
        return False
    else:
        for i in let_list1:
            if i not in let_list2:
                return False
        return True

start = time.time()
print(is_anagram(w1, w2))
end = time.time()
print(f'Function is_anagram completed in {(end - start)*1000} ms.')