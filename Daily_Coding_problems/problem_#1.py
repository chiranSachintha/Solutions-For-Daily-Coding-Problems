def sumOfNum(array, value):

    array.sort()
    count_1 = 0
    count_2 = 0
    for i in range(len(array)):
        if array[count_1] + array[len(array)-1-count_2] < value:
            count_1 = count_1 + 1
        elif array[count_1] + array[len(array)-1-count_2] > value:
            count_2 = count_2 + 1
        else:
            return [array[count_1], array[len(array)-1-count_2]]

print(sumOfNum([10, 15, 3, 7,2,1], 4))