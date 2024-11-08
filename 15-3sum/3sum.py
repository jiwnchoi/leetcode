from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        visited= set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            hashmap = {}

            for j in range(i+1, len(nums)):
                if (-nums[i] - nums[j]) in hashmap:
                    continue
                hashmap[-nums[i] - nums[j]] = j

            for k in range(i+1, len(nums)):
                if nums[k] in hashmap and k > hashmap[nums[k]]:
                    result.add((
                        nums[i], nums[k], nums[hashmap[nums[k]]]
                    ))

        return [list(r) for r in result]



            