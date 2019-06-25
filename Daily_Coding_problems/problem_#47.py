'''

Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

time complexity : O(n**2)

'''

def maxProfit(array):
    max_profit = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[j] - array[i]) > max_profit:
                max_profit = array[j] - array[i]
    return max_profit

array = [9, 8, 5, 7, 10, 11]
print(maxProfit(array))