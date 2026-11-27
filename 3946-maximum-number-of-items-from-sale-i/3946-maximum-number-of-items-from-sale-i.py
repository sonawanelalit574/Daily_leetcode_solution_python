from typing import List
from math import inf


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # dp[j] = maximum value achievable using a subset of items
        # whose total price does not exceed j (each item used at most once)
        dp = [0] * (budget + 1)

        # min_price tracks the cheapest item price; used later so that any
        # leftover budget can keep buying the cheapest item to gain extra value
        min_price = inf

        for factor, price in items:
            # update the cheapest price seen so far
            min_price = min(min_price, price)

            # value of taking this item = number of items whose factor is
            # divisible by the current item's factor
            value = sum(other_factor % factor == 0 for other_factor, _ in items)

            # standard 0/1 knapsack: iterate budget from high to low so each
            # item is only counted once
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + value)

        # for each budget point i, spend the remaining (budget - i) on the
        # cheapest item, gaining one unit of value per purchase; take the max
        return max(
            value + (budget - i) // min_price
            for i, value in enumerate(dp)
        )
