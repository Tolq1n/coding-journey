#122. Best Time to Buy and Sell Stock II
def maxProfit(prices):
    profit = 0
    buy = prices[0]
    days = len(prices)
    for i in range(1, days):
        if buy < prices[i]:
            profit += prices[i] - buy
        buy = prices[i]
    return profit