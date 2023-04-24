'''
Write a function to flatten the contents of a provided array,
which may or may not contain other nested arrays.
'''

'''
Solution one:
Iterate through the list, and for items that are instances of the list
object, call the function recursively. For items that are not lists,
yield the item.
'''
def steamroller(arr):
    for i in arr:
        if isinstance(i, list):
            for j in steamroller(i):
                yield j
        else:
            yield i

test_arr = [1,2,[3,4,[5,6],7,[8,[9,91]],10],11,12]

print(list(steamroller(test_arr)))