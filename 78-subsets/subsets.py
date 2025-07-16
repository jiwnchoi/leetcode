class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def f(current: list[int], ns: list[int]):
            answer.append(current)
            return sum([
                f([*current, num], ns[i+1:]) for i, num in enumerate(ns)
            ], [])

        f([], nums)
        return answer


