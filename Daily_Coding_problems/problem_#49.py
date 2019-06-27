'''

For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

'''

def maxSum(array):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(array)):
        max_ending_here = max_ending_here + array[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

array = [34, -50, 42, 14, -5, 86]
print(maxSum(array))