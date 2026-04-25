class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_loc = m+n-1
        num1_end = m-1
        num2_end = n-1
        while num1_end > -1 and num2_end > -1:
            n1, n2 = nums1[num1_end], nums2[num2_end]

            if n2 > n1:
                nums1[merge_loc] = n2
                num2_end -= 1
            else:
                nums1[merge_loc] = n1
                num1_end -= 1
            merge_loc -= 1
                    
        while num2_end > -1:
            nums1[num2_end] = nums2[num2_end]
            num2_end -= 1

