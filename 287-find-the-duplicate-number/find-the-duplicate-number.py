class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        inclusive = set()

        for n in nums:
            if n in inclusive:
                return n
            inclusive.add(n)