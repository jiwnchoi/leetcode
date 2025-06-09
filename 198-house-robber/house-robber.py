class Solution:
    def rob(self, nums: List[int]) -> int:
        output = -1

        dp = [0 for _ in nums]

        for i, num in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = num
            if i == 2:
                dp[i] = dp[i-2] + num
            if i > 2:
                dp[i] = max(dp[i-2], dp[i-3]) + num

            output = max(dp[i], output)
        print(dp)
        return output
            
            