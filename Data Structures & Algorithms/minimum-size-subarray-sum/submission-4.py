class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        best_min = float('inf')

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                best_min = min(best_min, r - l + 1)
                cur_sum -= nums[l]
                l += 1

        return best_min if best_min != float('inf') else 0