class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:      
        def merge_overlap(intervals: list[list[int]]) -> list[int]:
            if not intervals:
                return []

            return [
                min([i[0] for i in intervals]),
                max([i[1] for i in intervals])
            ]

        result = []

        added = False

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                if not added:
                    result.append(newInterval)
                    added = True
                result.append(interval)

            
            if newInterval[0] > interval[1]:
                result.extend([
                    interval,
                ])

            if interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                newInterval = merge_overlap([interval, newInterval])

        if not added:
            result.append(newInterval)

        return result