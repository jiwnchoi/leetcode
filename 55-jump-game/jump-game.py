import heapq

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0

        for i, num in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + num)
        
        if max_idx >= len(nums)-1:
            return True
        return False