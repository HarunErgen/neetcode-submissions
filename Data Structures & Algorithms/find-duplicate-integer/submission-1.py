class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0
        f = nums[nums[f]]
        s = nums[s]

        while f != s:
            f = nums[nums[f]]
            s = nums[s]
        
        start = 0
        while start != s:
            start = nums[start]
            s = nums[s]
        
        return s

