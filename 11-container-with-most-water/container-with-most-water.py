class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        def get_area(start: int, end: int) -> int:
            return (end - start) * min(height[end], height[start])

        max_area = get_area(start, end)

        while start < end:
            area = get_area(start, end)
            max_area = max(max_area, area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

        