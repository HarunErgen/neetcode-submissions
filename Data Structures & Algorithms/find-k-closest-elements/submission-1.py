class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            mid_index = l + (r - l) // 2

            if abs(arr[mid_index] - x) > abs(arr[mid_index+k] - x):
                l = mid_index + 1
            else:
                r = mid_index

        return arr[l:l+k]