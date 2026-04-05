class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # O(nlogn)

        intervals = deque(intervals)

        result = []
        while intervals:
            f, s = intervals.popleft(), None
            if intervals:
                s = intervals.popleft()

            if not s:
                result.append(f)
                continue
            
            if s[0] <= f[1]:
                temp = [min(s[0], f[0]), max(s[1], f[1])]
                intervals.appendleft(temp)
            else:
                result.append(f)
                intervals.appendleft(s)

        return result




        