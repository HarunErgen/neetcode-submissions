class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0

        l, r = 0, 1
        best_min = None
        cur_sum = nums[l]

        while r < len(nums)+1:
            if cur_sum >= target:
                if best_min is None: best_min = r-l
                else: best_min = min(best_min, r-l)
                if best_min == 1: return 1
                cur_sum -= nums[l]
                l += 1
            else:
                if r == len(nums): break
                cur_sum += nums[r]
                r += 1
        return best_min if best_min else 0
