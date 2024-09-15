class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        has_stock = -prices[0]
        no_stock = 0

        for price in prices[1:]:
            has_stock = max(has_stock,  no_stock - price)
            no_stock = max(no_stock, has_stock + price - fee)

        return no_stock