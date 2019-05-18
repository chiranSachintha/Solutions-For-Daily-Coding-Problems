'''

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''

def largestSumNonAjacent(array):
    n = len(array)
    sum1_1 = 0
    sum1_2 = 0
    sum1_3 = 0
    for i in range(2, n, 2):
        sum1_1 = sum1_1 + array[i]
    for i in range(3, n, 2):
        sum1_2 = sum1_2 + array[i]
    for i in range(4, n, 2):
        sum1_3 = sum1_3 + array[i]
    sum1_max = max(sum1_1 + array[0], sum1_2 + array[0], sum1_2 + array[1], sum1_3 + array[1])
    return sum1_max

print(largestSumNonAjacent([5, 1, 1, 5]))

