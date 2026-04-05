class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_added = result[-1]
            current = intervals[i]

            if current[0] <= last_added[1]:
                last_added[1] = max(last_added[1], current[1])
            else:
                result.append(current)

        return result