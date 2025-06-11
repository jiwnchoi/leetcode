class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1 for _ in nums]
        suffix_prod = [1 for _ in nums]

        prefix_prod[0] = nums[0]
        suffix_prod[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i]
            suffix_prod[-i-1] = suffix_prod[-i] * nums[-i-1]

        return [
            (1 if i == 0 else prefix_prod[i-1]) * (1 if i == len(nums)-1 else suffix_prod[i+1])
            for i in range(len(nums))
        ]
