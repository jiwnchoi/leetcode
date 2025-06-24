from collections import Counter
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        c = Counter(nums)
        for fr, to in zip(moveFrom, moveTo):
            if fr not in c:
                continue
            if fr == to:
                continue

            if to in c:
                c[to] += c[fr]
            else:
                c[to] = c[fr]

            del c[fr]

        return sorted(c.keys())