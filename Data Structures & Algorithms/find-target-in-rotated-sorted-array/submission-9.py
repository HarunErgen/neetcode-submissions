class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
             
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
                    



"""
3, 15


[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

[15,16,17,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

[5,6,7,8,9,10,11,12,13,14,15,16,17,1,2,3,4]
"""