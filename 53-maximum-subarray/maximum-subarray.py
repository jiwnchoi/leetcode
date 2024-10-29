class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = nums[0]

        for n in nums[1:]:
            current = max(current + n, n)
            result = max(current, result)

        return result