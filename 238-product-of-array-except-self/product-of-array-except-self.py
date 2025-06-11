class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
            
        prod = 1
        for i in range(1, len(nums)+1):
            result[-i] *= prod
            prod *= nums[-i]

        return result