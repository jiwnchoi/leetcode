from collections import defaultdict


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        answer = 0

        for a in arr:
            for k, v in c2.items():
                if k + a == target:
                    answer += v

            for k, v in c1.items():
                c2[k+a] += v

            c1[a] += 1
        return int(answer % (1e9 + 7))