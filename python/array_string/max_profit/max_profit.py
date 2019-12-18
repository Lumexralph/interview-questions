"""The algorithm assumes the input will only be a list
it solves the question with a time complexity of O(n)
and a space complexity of O(1)
"""
# from __future__ import annotations


class Solution:
    def max_profit(self, prices: [int]) -> int:
        if not isinstance(prices, list) or len(prices) < 1:
            return 0

        buy_price = float("inf")
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > profit:
                profit = price - buy_price

        return profit
