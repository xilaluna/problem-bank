# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def stocks(nums):
    l, r = 0, 1
    max_profit = 0

    while r < len(nums):
        if nums[l] < nums[r]:
            profit = nums[r] - nums[l]
            max_profit = max(max_profit, profit)
        else:
            l = r

        r += 1

    return max_profit
