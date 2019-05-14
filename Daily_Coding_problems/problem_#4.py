'''

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

'''

'BRUTE FORCE METHOD'

def minPositiveInt(array):
    n= len(array)
    minValue = 0
    for i in array:
        if i > 0 and minValue == 0:
            minValue = i
        elif i > 0 and i <= minValue:
            minValue = i
    return minValue
print(minPositiveInt([1, 2, 0]))

def minValNotInArray(minValue, array):
    arraySet = set(array)
    if minValue > 1 or minValue == 0:
        return 1
    else:
        for i in range(2, minValue+len(array)):
            if i not in arraySet:                   # instead of checking from the list check from the set
                return i
array = [1, 2, 0]
minValue = minPositiveInt(array)
print(minValNotInArray(minValue, array))
