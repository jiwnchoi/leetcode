import math

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        left_pos = [1 for _ in nums]
        left_neg = [-1 for _ in nums]
        right_pos = [1 for _ in nums]
        right_neg = [-1 for _ in nums]


        for i, n in enumerate(nums):
            if i ==0:
                left_pos[i] = n
                left_neg[i] = n
            if i > 0:
                left_pos[i] = max(left_pos[i-1], n)
                left_neg[i] = min(left_neg[i-1], n)


        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_pos[i] = nums[i]
                right_neg[i] = nums[i]
            if i < len(nums)-1:
                right_pos[i] = max(right_pos[i+1], nums[i])
                right_neg[i] = min(right_neg[i+1], nums[i])

        answer = -math.inf

     
        for i in range(len(nums) -m+1):
            answer = max(
                answer,
                left_pos[i] * right_pos[i+m-1],
                left_neg[i] * right_neg[i+m-1]
            )

        return answer
