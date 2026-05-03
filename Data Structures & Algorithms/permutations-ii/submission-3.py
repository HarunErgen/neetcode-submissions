class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(nums, idx):
            if idx == len(nums):
                res.append(nums.copy())
                return

            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                nums[i], nums[idx] = nums[idx], nums[i]
                bt(nums, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        bt(nums, 0)
        return res                    

        