import heapq
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reverse_nums = nums[::-1]

        rechable = []
        heapq.heappush(rechable, 0)

        for i, num in enumerate(reverse_nums):
            if i == 0:
                continue
            
            if i - (-rechable[0]) <= num:
                heapq.heappush(rechable, -i)

        return True if rechable[0] == -len(nums)+1 else False
