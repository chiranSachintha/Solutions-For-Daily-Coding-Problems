'''
Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''
def withDiv(array):
    newArray = []
    count = 1
    for i in array:
        count = count * i
    for i in array:
        newArray.append(count/i)
    return newArray

print(withDiv([1, 2, 3, 4, 5]))

def withoutDiv(array):
    newArray = []
    count = 1
    for i in array:
        for j in array:
            if i == j :
                continue
            count = count * j
        newArray.append(count)
        count = 1
    return newArray

print(withoutDiv([1, 2, 3, 4, 5]))