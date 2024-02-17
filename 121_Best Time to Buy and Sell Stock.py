class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # l:buy r:sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


prices = [7, 6, 4, 3, 1]
sol = Solution()
print(sol.maxProfit(prices))
