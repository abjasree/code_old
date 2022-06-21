class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for price in prices:
            current_price = price - minimum
            if  current_price > profit:
                profit = current_price
            if price < minimum:
                minimum = price
                
        return profit
                