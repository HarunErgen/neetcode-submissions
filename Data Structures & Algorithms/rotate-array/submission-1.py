class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        e = len(nums) - k

        while e > 0:
            for i in range(k):
                nums[e+i], nums[e-1+i] = nums[e-1+i], nums[e+i]
            e -= 1