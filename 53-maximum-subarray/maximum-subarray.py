class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        dp = [-1e5 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i] ,nums[i])
            result = max(result, dp[i])
        return result