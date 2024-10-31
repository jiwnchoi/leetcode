class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            arr = [dp[i-coin] + 1 for coin in coins if i-coin > -1 and dp[i-coin] != -1]
            dp[i] = min(arr) if arr else -1

        return dp[amount]